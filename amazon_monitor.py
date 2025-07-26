
import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Defina a URL do produto que você deseja monitorar
AMAZON_PRODUCT_URL = "https://www.amazon.com.br/Bundle-Nintendo-Switch-Mario-World/dp/B0F67B2D45/?_encoding=UTF8&pd_rd_w=prLir&content-id=amzn1.sym.8fbb3d34-c3f1-46af-9d99-fd6986f6ec8f&pf_rd_p=8fbb3d34-c3f1-46af-9d99-fd6986f6ec8f&pf_rd_r=X8XZGN3W2EWVQ7MXFXS6&pd_rd_wg=d0FtF&pd_rd_r=6c13af7c-e1d2-4eac-a1c1-d9f20a8f96b7&ref_=pd_hp_d_btf_crs_zg_bs_7791985011"

# Defina o preço abaixo do qual você deseja ser notificado
TARGET_PRICE = 150.00  # Em BRL

# Configurações de e-mail (use variáveis de ambiente para segurança)
SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))
SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")
RECIPIENT_EMAIL = os.environ.get("RECIPIENT_EMAIL")

def check_price():
    """Verifica o preço do produto na Amazon e envia um e-mail se estiver abaixo do alvo."""
    if AMAZON_PRODUCT_URL == "URL_DO_SEU_PRODUTO_AQUI":
        print("Por favor, defina a variável AMAZON_PRODUCT_URL no arquivo amazon_monitor.py")
        return

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9,pt;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Connection": "keep-alive"
    }

    try:
        response = requests.get(AMAZON_PRODUCT_URL, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar a página do produto: {e}")
        return

    soup = BeautifulSoup(response.content, "html.parser")

    price_span = soup.select_one('.a-price-whole')
    price_fraction = soup.select_one('.a-price-fraction')

    if price_span and price_fraction:
        try:
            price_str = f"{price_span.get_text().strip()}{price_fraction.get_text().strip()}"
            current_price = float(price_str.replace("R$", "").replace(".", "").replace(",", ".").strip())

            print(f"Preço atual: R${current_price:.2f}")

            if current_price < TARGET_PRICE:
                print("O preço está abaixo do alvo! Enviando e-mail...")
                send_email(AMAZON_PRODUCT_URL, current_price)
            else:
                print("O preço ainda está acima do alvo.")
        except (ValueError, AttributeError) as e:
            print(f"Não foi possível extrair o preço: {e}")
    else:
        print("Não foi possível encontrar o elemento de preço na página. O layout da Amazon pode ter mudado.")

def send_email(product_url, price):
    """Envia um e-mail de notificação de preço baixo."""
    if not all([SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL]):
        print("As credenciais de e-mail não estão configuradas. Verifique seu arquivo .env. Não é possível enviar o e-mail.")
        return

    subject = "Alerta de Preço Baixo na Amazon!"
    body = f"O preço do produto em {product_url} caiu para R${price:.2f}! Corra para comprar!"
    
    message = f"Subject: {subject} {body}"

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, message.encode('utf-8'))
        print("E-mail enviado com sucesso!")
    except smtplib.SMTPException as e:
        print(f"Erro ao enviar e-mail: {e}")

if __name__ == "__main__":
    check_price()

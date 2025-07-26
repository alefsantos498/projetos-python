# Monitor de Preços da Amazon

Este é um script Python que monitora o preço de um produto na Amazon. Se o preço do produto cair abaixo de um valor definido por você, o script enviará um e-mail de notificação.

Este projeto demonstra habilidades em web scraping, manipulação de HTML e integração com serviços de e-mail, tornando-o uma ótima adição a um portfólio de desenvolvedor.

## ✨ Funcionalidades

-   **Web Scraping:** Extrai o nome e o preço do produto de uma página da Amazon.
-   **Monitoramento de Preço:** Compara o preço atual com um preço-alvo definido pelo usuário.
-   **Notificação por E-mail:** Envia um alerta por e-mail quando o preço cai abaixo do alvo.
-   **Configuração Segura:** Utiliza variáveis de ambiente para armazenar informações sensíveis, como senhas de e-mail.

## 🚀 Como Usar

Siga os passos abaixo para configurar e executar o monitor de preços.

### **Pré-requisitos**

-   Python 3.x
-   Uma conta de e-mail com acesso SMTP (por exemplo, Gmail, com uma "senha de aplicativo").

### **1. Instalação**

Primeiro, clone este repositório (ou simplesmente baixe os arquivos) e navegue até o diretório do projeto.

Crie e ative um ambiente virtual:

```bash
# Cria o ambiente virtual
python3 -m venv .venv

# Ativa o ambiente virtual (Linux/macOS)
source .venv/bin/activate

# Ativa o ambiente virtual (Windows)
# .\.venv\Scripts\activate
```

Instale as dependências necessárias a partir do arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### **2. Configuração**

#### **a) Variáveis de Ambiente**

Crie um arquivo chamado `.env` na raiz do projeto, copiando o exemplo abaixo. Este arquivo armazenará suas credenciais de e-mail de forma segura.

```ini
# .env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=seu_email@gmail.com
SENDER_PASSWORD=sua_senha_de_app_do_email
RECIPIENT_EMAIL=email_destino@exemplo.com
```

-   **`SENDER_EMAIL`**: O e-mail que enviará a notificação.
-   **`SENDER_PASSWORD`**: A senha do seu e-mail. **Importante:** Se você usa o Gmail com 2FA, você precisará gerar uma "Senha de App".
-   **`RECIPIENT_EMAIL`**: O e-mail que receberá o alerta de preço.

#### **b) Configuração do Script**

Abra o arquivo `amazon_monitor.py` e configure as seguintes variáveis no topo do arquivo:

-   **`AMAZON_PRODUCT_URL`**: Coloque a URL completa do produto da Amazon que você deseja monitorar.
-   **`TARGET_PRICE`**: Defina o preço (em BRL, formato float, ex: `250.50`) abaixo do qual você deseja ser notificado.

### **3. Execução**

Com o ambiente virtual ativado e os arquivos de configuração preenchidos, execute o script:

```bash
python amazon_monitor.py
```

O script irá verificar o preço do produto. Se o preço estiver abaixo do seu alvo, ele enviará um e-mail e imprimirá uma mensagem no console.

## 🛠️ Como Funciona

1.  **Requisição HTTP:** O script usa a biblioteca `requests` para fazer uma requisição GET para a URL do produto da Amazon, simulando um navegador para obter o conteúdo da página.
2.  **Parsing de HTML:** A biblioteca `BeautifulSoup4` é usada para analisar o HTML da página e encontrar os elementos que contêm o preço do produto (especificamente, as classes CSS `.a-price-whole` e `.a-price-fraction`).
3.  **Comparação de Preço:** O preço extraído é convertido para um número e comparado com o `TARGET_PRICE`.
4.  **Envio de E-mail:** Se o preço atual for menor que o preço-alvo, a função `send_email` é chamada. Ela se conecta a um servidor SMTP (usando a biblioteca `smtplib`) com as credenciais fornecidas no arquivo `.env` e envia o e-mail de alerta.

## 📚 Bibliotecas Utilizadas

-   [requests](https://docs.python-requests.org/en/latest/): Para fazer requisições HTTP.
-   [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): Para extrair dados de arquivos HTML.
-   [python-dotenv](https://github.com/theskumar/python-dotenv): Para gerenciar variáveis de ambiente.
-   [smtplib](https://docs.python.org/3/library/smtplib.html): Para enviar e-mails usando o protocolo SMTP.
>>>>>>>>
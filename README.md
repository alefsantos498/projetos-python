# Calculadora de Gorjetas

Este é um simples aplicativo de linha de comando em Python que calcula o valor da gorjeta e o total da conta por pessoa.

## O Código (`main.py`)

O script `main.py` contém uma única função `main()` que:

1.  **Recebe as entradas do usuário:**
    *   O valor total da conta.
    *   A porcentagem de gorjeta desejada (10%, 12% ou 15%).
    *   O número de pessoas para dividir a conta.

2.  **Calcula o valor final:**
    *   Adiciona a gorjeta ao total da conta.
    *   Divide o valor total pelo número de pessoas.

3.  **Exibe o resultado:**
    *   Mostra o valor que cada pessoa deve pagar, formatado com duas casas decimais.

O código também inclui tratamento de erros para garantir que as entradas sejam numéricas e que o número de pessoas seja maior que zero.

## Como Usar

1.  Certifique-se de ter o Python 3 instalado.
2.  Abra o seu terminal.
3.  Navegue até o diretório do projeto.
4.  Execute o seguinte comando:

    ```bash
    python main.py
    ```

5.  O programa solicitará que você insira o total da conta, a porcentagem da gorjeta e o número de pessoas para dividir a conta. Após fornecer as informações, ele calculará e exibirá o valor por pessoa.

### Exemplo de Uso

```
Bem-vindo à Calculadora de Gorjetas!
Qual foi o valor total da conta? R$150.50
Qual porcentagem de gorjeta você gostaria de dar? 10, 12 ou 15? 12
Em quantas pessoas a conta será dividida? 5
Cada pessoa deve pagar: R$33.71
```

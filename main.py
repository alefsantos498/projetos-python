# tip_calculator.py

def main():
    """
    Calcula o valor da gorjeta e o total da conta por pessoa.
    """
    print("Bem-vindo à Calculadora de Gorjetas!")

    try:
        total_bill = float(input("Qual foi o valor total da conta? R$"))
        tip_percentage = int(input("Qual porcentagem de gorjeta você gostaria de dar? 10, 12 ou 15? "))
        people_count = int(input("Em quantas pessoas a conta será dividida? "))

        if people_count <= 0:
            print("O número de pessoas deve ser maior que zero.")
            return

        # Calcula o total com a gorjeta
        total_with_tip = total_bill * (1 + tip_percentage / 100)

        # Calcula o valor por pessoa
        bill_per_person = total_with_tip / people_count

        # Arredonda o resultado para 2 casas decimais
        final_amount = round(bill_per_person, 2)
        final_amount_str = f"{final_amount:.2f}" # Formata para garantir duas casas decimais

        print(f"Cada pessoa deve pagar: R${final_amount_str}")

    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")
    except ZeroDivisionError:
        print("Não é possível dividir a conta por zero pessoas.")

if __name__ == "__main__":
    main()

"""Pequeno programa que lê dois números e realiza uma operação simples.

O usuário escolhe entre: soma, subtração, multiplicação, divisão e resto.
Trata entrada inválida e divisão por zero.
"""

def leia_numero(prompt):
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Entrada inválida. Informe um número válido.")


def main():
	print("Operações disponíveis: +  -  *  /  %")
	a = leia_numero("Informe o primeiro número: ")
	b = leia_numero("Informe o segundo número: ")
	op = input("Escolha a operação (+, -, *, /, %): ").strip()

	if op == "+":
		resultado = a + b
	elif op == "-":
		resultado = a - b
	elif op == "*":
		resultado = a * b
	elif op == "/":
		if b == 0:
			print("Erro: divisão por zero.")
			return
		resultado = a / b
	elif op == "%":
		if b == 0:
			print("Erro: divisão por zero.")
			return
		resultado = a % b
	else:
		print("Operação desconhecida.")
		return

	# Exibir resultado com formatação simples
	if resultado.is_integer():
		# mostrar sem .0 quando for inteiro
		print(f"Resultado: {int(resultado)}")
	else:
		print(f"Resultado: {resultado}")


if __name__ == "__main__":
	main()



# crie um dicionário que associa produtos aos seus preços
produtos_precos = {
    "Arroz": 5.99,
    "Feijão": 7.49,
    "Macarrão": 3.79,
    "Óleo": 8.99,
    "Açúcar": 4.29,
    "Café": 10.99,
    "Leite": 6.49,
    "Pão": 2.99,
    "Manteiga": 9.49,
    "Queijo": 15.99
}

# Exemplo de como acessar os preços
for produto, preco in produtos_precos.items():
    print(f"O preço do {produto} é R$ {preco:.2f}")


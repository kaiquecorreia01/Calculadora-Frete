# guarda a informação de quantos kg tem a encomenda
try:
    peso = float(input("Digite o peso da encomenda em kg: "))
    # verificar se o peso é um numero positivo, se o peso for igual ou menor que 0, aparece uma mensagem de erro
    if peso <= 0:
        print("Erro: o peso deve ser maior que zero")
        exit()
    # ========================================
 # aqui gera uma msg de erro caso digite letras em vez de numeros
except ValueError:
    print("Erro: peso invalido. Digite apenas numeros")
    exit()

# escolhe o tipo de encomenda, 1 para comum e 2 para expressa
try:
    entrega = (input(
        "TIPOS DE ENTREGA\n1 - Comum (R$10,00)\n2 - Expressa (R$20,00)\n3 - Relampago (R$30,00)\nSelecione um tipo de entrega: "))
except ValueError:
    exit()

# aqui é a seleção da entrega, comum ou expressa
if entrega == "1":
    custo_frete = 10

elif entrega == "2":
    custo_frete = 20

elif entrega == "3":
    custo_frete = 30
# se os kg digitado na variavel peso for igual ou menor que 1, o custo base sera $20
if peso <= 4:
    cb = 20
# se os kg digitado na variavel peso for igual ou menor que 5, o custo base sera $45
elif peso <= 8:
    cb = 45
# ja se os kg digitado na variavel peso for maior doq , o custo base sera $80
else:
    cb = 80

custo_total = cb + custo_frete

print("O custo total do seu frete é de: R$", custo_total)

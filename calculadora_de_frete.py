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
    entrega = int(input(
        "TIPOS DE ENTREGA\n1 - Comum\n2 - Expresso\nSelecione um tipo de entrega: "))
    # criei uma regra que se o valor digitado na variavel "entrega" for igual ou menor que 0 ou for maior do que 2, ele gera uma mensagem de erro
    if entrega > 2:
        print("Erro: Por favor, escolha somente uma das opções apresentadas")
        exit()
    elif entrega <= 0:
        print("Erro: Por favor, escolha somente uma das opções apresentadas")
        exit()
# aqui é pra se digitar algo alem de numeros
except ValueError:
    print("Erro: Digite somente numeros")
    exit()

# se os kg digitado na variavel peso for igual ou menor que 1, o custo base sera $20
if peso <= 1:
    cb = 20
    print("O custo de entrega para esse peso é de: R$", cb)
# se os kg digitado na variavel peso for igual ou menor que 5, o custo base sera $45
elif peso <= 5:
    cb = 45
    print("O custo de entrega para esse peso é de: R$", cb)
# ja se os kg digitado na variavel peso for maior doq , o custo base sera $80
else:
    cb = 80
    print("O custo de entrega para esse peso é de: R$", cb)
# aqui é a seleção da entrega, comum ou expressa
if entrega == 1:
    print("Voce escolheu a entrega comum ")
if entrega == 2:
    print("Voce escolheu a entrega expressa")

#valor = float(input('Valor do produto é: '))
#desc = float(input('O desconto é: '))
#print(f'O valor do produto é {valor} o desconto é {desc} com desconto fica {(valor*desc)/100} = {valor-desc}')#



preço = float(input('Qual é o preço do produto R$'))
novo = preço - (preço * 5 / 100)
print(f'O produto custava R${preço}, na promoção ficou por R${novo:.2f} ')
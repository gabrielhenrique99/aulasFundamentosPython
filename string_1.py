nome = "GAbriEL"

print(nome.upper()) #GABRIEL
print(nome.lower()) #gabriel
print(nome.title()) #Gabriel


texto = "  Olá mundo!    "

print(texto.strip() + ".") #Olá Mundo!
print(texto.lstrip()+ ".") #Olá mundo!    .
print(texto.rstrip()+ ".") #  Olá mundo.

menu = "Python"

print(menu.center(14)) #(    Python    )
print(menu.center(14,"&")) #(&&&&Python&&&&)
print("-".join(menu))
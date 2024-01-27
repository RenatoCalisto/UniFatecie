largura_garagem = float (input ("Digite a largura da garagem em metros"))
profundidade_garagem = float (input ("Digite a profundidade da garagem em metros"))

area_garagem = largura_garagem * profundidade_garagem

largura_terreno = float (input ("Digite a largura do terreno em metros"))
profundidade_terreno = float (input ("Digite a profundidade do terreno em metros"))

area_terreno = largura_terreno * profundidade_terreno

percentual = ((area_garagem) / (area_terreno)) * 100

zona = input ("Digite a zona: Norte=n Sul=s Leste=l Oeste=o")

print("Imóvel localizado na Zona: ", zona)
print("Percentual de ocupação: ", percentual)

if zona == "n" and percentual <= 25:
    print("Projeto atende as normas")
if zona == "s" and percentual <= 40:
    print("Projeto atende as normas")
if zona == "l" and percentual <= 30:
    print("Projeto atende as normas")

else:
    print("Revisar medidas, Projeto não atende as normas")
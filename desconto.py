resultado = float(input("Digite o valor do resultado: "))

if resultado >= 500:
    desconto = 0.20
       
elif resultado >= 200:
    desconto = 0.10
    
else:
    desconto = 0.0

final = resultado * (1 - desconto)

print("O valor final com desconto é: ",final)
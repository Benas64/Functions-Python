#Esta é uma calculadora feita 100% em python
# Começaremos pelos comandos

#soma
def soma(a,b):
    s=a+b
    print(s)


#diferença
def diferença(a,b):
    d=a-b
    print(d)


#multiplicação
def multiplicaçao(a,b):
    m=a*b
    print(m)  


#divisão
def divisao(a,b):
    div= a/b
    print(div)


#potencia
def potencia(a,b):
    pot=a**b
    print(pot)
#Agora vamos ao programa da calculadora Asimov em si.
print("Olá, seja bem vindo à calculadora Asimov, digite os números e a operação escolhida.")
a=float(input(" Qual o primeiro número?"))
b=float(input("Qual o segundo número?"))
print("Agora escolha a operação a ser realizada")
operaçao=str(input("Qual a operação a ser realizada?"))

if operaçao=='+':
    soma(a,b)
elif operaçao=='-':
    diferença(a,b)
elif operaçao=='*':
    multiplicaçao(a,b)
elif operaçao=='/':
    divisao(a,b)
elif operaçao=='**':
    potencia(a,b)
else:
    print("Essa operação está indisponível,tente novamente")

print("Desejas fazer outra operação?")
resposta=str(input("s ou n?"))
if resposta=='s':
   print("Reinicie o programa.")
else:
    print("A calculadora Asimov agradece o seu uso.")



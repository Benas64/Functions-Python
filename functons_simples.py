#Nesse arquivo será trabalhado a função def do python em algoritmos simples.
#1.Soma entre dois números
def soma(a,b):
    s= a+b
    print(s)



#2.funções financeiras
#2.1 Juros simples
def juros_simples(c,r,n):
    j=c*r*n
    print(j)


#2.2Agora vamos para a parte de captalização composta
# VP=valor presente
def vp(fv,r,n):
    x=fv/(1+(r/100))**n
    print(x)



#FV=valor futuro
def fv(vp,r,n):
    y=vp*(1+(r/100))**n
    print(y)





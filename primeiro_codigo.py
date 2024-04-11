
CONST=2
nome="Willian"
print(f'Hello, {nome}!')
def somar(a,b):
    result=a+b
    print(result)
def ordenar(a):
    j=0
    elementos=len(a)
    for i in a:
        menor=i
        for n in range(elementos):
            if j<n:
                if menor>a[n]:
                    menor=a[n]
                    b=i
                    i=menor
                    a[n]=b
        a[j]=menor
        j=j+1

a=[4,2,3,1,6,0,23,5,7,5,12]
ordenar(a)
print(a)
n=int(input())
s=[]
tradutor={}
for i in range(0, ((n-1)*2) +1 , 2):
    s[i],s[i+1]=input().split()  #isso não dá certo porque [] serve para cessar uma possuição já existente ou alterar a posição já existente
for i in range(0, ((n-1)*2) +1 , 2):
    tradutor[s[i]]=s[i+1]
k=input().split()
for i in range(len(k)):
    print(tradutor[k[i]], end=" ")


#codigo certo
n=int(input())
s=[]
tradutor={}
for i in range(0, n):
    I,P=input().split() #ao inves disso
    s.append(I), s.append(P) #poderia ser apenas: s.extend()=intput().
for i in range(0, 2*n, 2):
    tradutor[s[i]]=s[i+1]
k=input().split()
for i in range(len(k)):
    print(tradutor[k[i]], end=" ")



    #agentes de IA, anti-gravity, mit learn (Pyhton), machine learning supervisionado e nao supervisionado, divisao de data seats, simulacao de redes opticas, atenuacao, etc
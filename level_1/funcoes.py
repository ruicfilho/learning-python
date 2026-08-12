def media(x,y):
    resultado=(x+y)/2
    return resultado
a,b=map(int,input().split())
print(media(a,b))

print("NOVO MÈTODO")

k,p =map(int,input().split())
def new_media(m,n):
    result=(m+n)/2
    return result, m, n 

pedido=new_media(k,p)
print(f"a media entre {pedido[1]} e {pedido[2]} é {pedido[0]}")
print(f"{pedido}")

#seleção do que se deseja armazenar
media, *_ = new_media(k,p) #armazena apenas o primeiro elemento e decarta o resto
media, valor1, *_ = new_media(k,p) #armazena os dois primeiros elementos
 #o que fizemos chma-se enpacotamento
e, *f = (0,1,2,3) #rsulta em e=0 e f=[1,2,3], utiliza-se, por convenção, o _ para representar o nosso lixo

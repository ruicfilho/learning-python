s="Olá, Neps Academy"
print(s)
print(f"Quantos caracteres será que tem nossa string? {len(s)}")
s=s.replace("Neps", "Rui")
s=s.replace("Academy", "Afonso")
print(s)
#uma string em python é imutável, ao usar s=s.replace, substituimos nossa string original por uma nova string
print("-----------------")
print(s.replace("Afonso", "Castro Filho"))
print("ao usar replace em print, nossa string não muda, só é msotrado uma string nova que não é salva em nenhum local:")
print(s)
print("-----------------------------------------------")
v= "Ola rui AFONSO"
print(v.upper())
print(v.lower())
print(v.title())

for letra in v:
    print(letra, end='')
print("-------------")
string= "nepsAcademy"
substring=string[0:4]
print(substring)
substring=string[0:11]
print(substring)
print(substring[11:0:-1])
print(substring[0:11:2])
#o sllicing tb funciona para listas
v=["N", 10, 9, 8, 7, "P"]
new_v=v[6:0:-1]
print(new_v)
new_v=v[6::-1]
print(new_v)
def eh_primo(x):
    from math import isqrt
    if x<=1:
          return False 
    
    for i in range(2, isqrt(x) + 1): #para o caso x=2, o for não é execultado, pois o range será (2, 2), isto é. vazio.
        if(x%i==0):
            return False
    return True

x = int(input())
if eh_primo(x):
	print('S')
else:
	print('N')

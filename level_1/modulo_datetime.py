#DateTime
#vamos ver a classe datetime
from datetime import datetime
data= datetime(2025, 8, 30, 9, 58, 00)
print(data)
#o formado printado é americano, vamos mudar isso
data_br=data.strftime("%d/%m/%Y %H:%M:%S")
print(data_br)
#lendo uma data inserida:
data_inserida="20/02/2008"
data_lida= datetime.strptime(data_inserida, "%d/%m/%Y")
print(data_lida)
#sabendo a data atual 
data_atual=datetime.now()
print(data_atual)
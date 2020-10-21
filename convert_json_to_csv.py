#import pandas as pd

#data = pd.read_json('./json/exemplo/shopping.json')
#data.to_csv('./gerados/shopping.csv')

# Por alguma razão, o script acima mesmo sendo identico ao seu "oposto"
# parece não funcionar, mesmo que crie o arquivo na pasta e formato certos.
# Em suma, parece não converter muito bem o arquivo para CSV


# Dito isso, tentei desenvolver 2 outras lógicas 

import json
import csv

with open('./json/exemplo/shopping.json') as file:
    data = json.load(file)

file_name = 'output.csv'
orders = data['order']


data_file = open(file_name, 'w')
csv_writer = csv.writer(data_file)

count = 0
for order in orders:
    if count == 0:
        header = order.keys()
        csv_writer.writerow(header)
        count += 1

    csv_writer.writerow(order.values())

# Nessa acima, o arquivo é convertido, mas não consegui fazer com que ele fosse
# gerado na pasta "gerados", ou alterar os atributos para adicionar o "total"

# Tenho consciencia de que a lógica giraria em torno de um FOR (algo como "for o in orders") com um loop em cada order, 
# onde adicionariamos tanto um novo atributo "Total" que seria a multiplicação do o[quantity] * o[value], quanto uma variavel
# sum (iniciada antes) valendo sum += o[Total] (pra cada loop do for), dando um append no final do json com o valor de sum para 
# o valor total de todas as ordens. Mas mesmo sabendo disso, me faltou o conhecimento de python para integrar isso de maneira correta. 

# O mais longe que cheguei foi utilizar o json.loads e fazer a logica do for, com o objetivo de utilizar o json.dumps no final. Mas não consegui completar a lógica. 
# Não conseguia fazer a variavel sum receber o valor de order[Total] (mesmo tendo conseguido criar esse valor na memoria) para imprimir no final.



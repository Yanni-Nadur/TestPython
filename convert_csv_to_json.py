import pandas as pd 
from pathlib import Path

outputFile = 'shopping.json'
outputPath = Path('./gerados')

outputPath.mkdir(parents=True, exist_ok=True)

df = pd.read_csv('./csv/exemplo/shopping.csv', encoding= "ISO-8859-1")
df.to_json(outputPath/ outputFile)


# Utilizei da lib "pandas" para realizar a conversão. Tenho consciencia de que esse metodo nao permitiu a alteração do arquivo
# conforme os requisitos, mas novamente, me faltou o conhecimento em python para realizar a tarefa de acessar os atributos do CSV
# e adicionar a soma do "total" deles no final do arquivo. A tarefa foi compreendida, mas não consegui executá-la.
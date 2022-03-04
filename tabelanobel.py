import pandas as pd
dados = pd.read_html('https://www.reclameaqui.com.br/ranking/')

laureados=dados[0]

#laureados.to_excel('laureadosnobel.xlsx', index=False)
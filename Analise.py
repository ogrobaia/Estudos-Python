from flask import Flask, render_template
import pandas as pd
import io
import requests

app = Flask(__name__)

# URL do arquivo do Google Sheets
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQRwcBr3yUZEMDSG-BhArLNXsNm5mG0ePMPSufG3hrVU0_o6kpFk-nYSTcoX7V0GML6ReAyb58Szrzs/pub?output=xlsx"
# Fazer uma solicitação HTTP para obter o conteúdo do arquivo Excel
response = requests.get(url)

# Carregar os dados da planilha em um DataFrame
df = pd.read_excel(io.BytesIO(response.content))

# Limpar os dados - removendo colunas desnecessárias
df = df.drop(columns=["loja", "merchant_id", "id_rede", "rede", "id_loja",
             "sku_original", "ignora_estoque", "ignora_estoque_force", "plataforma", "dt"])

# Excluir linhas com valores vazios
print(df)


@app.route('/')
def index():
    # Renderizar o template HTML e passar o DataFrame para ele
    return render_template('index.html', data=df.to_dict('records'))


if __name__ == '__main__':
    app.run(debug=True)

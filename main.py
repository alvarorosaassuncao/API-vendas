import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

#CONSTRUINDO FUNCIONALIDADES
@app.route('/')
def contatos():
  return 'Essa é a pagina de contatos do site'

@app.route('/pegarvendas')
def pegarvendas():
  tabela = pd.read_csv('apipython.csv')
  total_vendas = tabela ['Vendas'].sum()
  resposta = {'total_vendas': total_vendas}
  return jsonify(resposta)


#RODAR API
app.run(host='0.0.0.0')



#link para verificar vendas 
# https://Minha-API.alvaroassuncao1.repl.co/pegarvendas

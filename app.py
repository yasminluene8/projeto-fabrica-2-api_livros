# No terminal:
# 1) Criamos um ambiente virtual com o comando:
# python -m venv .venv
# 2) Ativamos o ambiente virtual com o comando:
# .\.venv\Scripts\activate
# 3) iInstalamos o flask com o comando:
# pip install flask
# Caso o seu ambienete virtual não seja é precisop pesquisar na
# internet como liberar a execução
# dele no PowerShell e voltar a ativar o ambiente depois

from flask import Flask, jsonify, make_response,request
from bd_livros import livros # Aqui estou importando a listas de livros criado (bando de dados)

# BIBLIOTECAS
#jsonify = transforma lista, dicionários etc em arquivos json. Só funciona com status code 200, ou seja 
# # quando  a requisição é bem sucedida
# make_response = tr4ansforma os json em métodos HTTP e permite que estilizemos nossa resposta
# e trata os erros
# request = faz as requisições 


app = Flask(__name__) # Instanciando o flask, ou seja, estou tornando o molde num objeto
app.config["JSON_SORT_KEYS"]=False

# GET - Listar todos os livros do nosso "banco de dados"
@app.route("/livros", methods=["GET"])
def get_livros():
    return make_response(jsonify(
        mensagem = "Lista de livros Cadastrados",
        dados = livros
    ),200)
# GET - Buscar ´penas um livro pelo ID
@app.route("/livros/<int:id>", methods=["GET"])
def get_livro(id):
    for livro in livros: # Percorrer a lista de livros
        if livro.get("id") == id:
            return make_response(jsonify(
                mensagem=f"livro de ID {id} encontrado.",
                dados = livro
            
            ),200)
    return make_response(jsonify(mensagem="Livro não encontrado"), 404)

# POST - Adicionar um novo livro 
@app.route("/livros",methods=["POST"])
def create_livro():
    novo_livro = request.json
    livros.append(novo_livro)
    return make_response(jsonify(
        mensagem="Novo livro adicionado com sucesso",
        dados = novo_livro
    ),201)

# PUT - Atualizar livro por completo
@app.route("/livros/<int:id>",methods=["PUT"])
def update_livro(id):
    for livro in livros:
        if livro.get("id") == id:
            novo_dados = request.json
            livro.update(novo_dados) # Substitui todos os dados
            return make_response(jsonify(
                mensagem=f"Livro ID{id} atualizado com sucesso (PUT)."
            ),200)
    return make_response(jsonify(mensagem="Livro não encontrado"),404)

# PATCH - Atualizar parcialmente um livro
@app.route("/livros/<int:id>",methods={"PATCH"})
def patch_livro(id):
    for livro in livros:
        if livro.get("id") == id:
            dados = request.json
            livro.update(dados) # Só altera os campos enviados 
            return make_response(jsonify(
                mensagem=f"Livro id {id} atualizado parcialmente (PATCH).",
                dados = livro
            ),200)
    return make_response(jsonify(mensagem="Livro não encontrado"),404)

# Delete - Remover um livro
@app.route("/livros/<int:id>", methods={"DELETE"})
def delete_livro(id):
    for livro in livros:
        if livro.get("id") == id:
            livros.remove(livro)
            return make_response(jsonify(
                mensagem=f"Livro ID {id} foi removido com sucesso."
            ),200)
    return make_response(jsonify(mensagem="Livro não encontrado."),404)
    
if __name__ == "__main__": # Essse comando permite que a api seja executada de maneira independente em outros arquivos
    app.run(debug=True)
from flask import Flask, jsonify, Request

app= Flask(__name__)

livros= [
    {
        'id': 1,
        'título': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor':   'J.R.R Tolkein',
    },
    {
        'id': 2,
        'título': 'O Jardim das Aflições',
        'autor': 'Olavo de Carvalho',
    },
]

#Consultar_todos_os_livros
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

#Consultar_livros_por_iD
@app.route('/livros/<int:id>',methods=['GET'])
def livros_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
#Editar_Livro_por_iD
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_por_id(id):
    alteracao = Request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get(id) == id:
            livros[indice].update(alteracao)
            return jsonify(livros[indice])

#Criando_Novo_Livro
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = Request.get_json()
    livros.append(novo_livro)
    
    return jsonify(livros)

#Excluindo_Livros
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)

#Executar
app.run(port=5000,host='localhost',debug=True)

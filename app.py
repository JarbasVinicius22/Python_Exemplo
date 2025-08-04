from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados dos alunos
alunos = {
    "Jorge": 8,
    "Gregório": 6,
    "Cleber": 4,
    "Wesley": 10
}

# Rota principal que exibe os resultados no navegador
@app.route('/')
def home():
    html = "<h2 style='text-align:center;'>Lista de Alunos e Notas</h2><ul style='font-size:18px;'>"

    for aluno, nota in alunos.items():
        if nota >= 7:
            resultado = "<span style='color:green;'>Aprovado</span>"
        elif nota >= 5:
            resultado = "<span style='color:orange;'>Recuperação</span>"
        else:
            resultado = "<span style='color:red;'>Reprovado</span>"

        html += f"<li>{aluno}: {nota} - {resultado}</li>"


    return html

# Rota para listar usuários - GET
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = [
        {"id": 1, "nome": "Jorge", "nota": 8},
        {"id": 2, "nome": "Gregório", "nota": 6},
        {"id": 3, "nome": "Cleber", "nota": 4},
        {"id": 4, "nome": "Wesley", "nota": 10}
    ]
    return jsonify(usuarios)

# Rota para criar usuário - POST
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.json
    novo_usuario = {
        "id": dados.get('id'),
        "nome": dados.get('nome'),
        "nota": dados.get('nota')
    }
    return jsonify(novo_usuario), 201

# Executar a aplicação
if __name__ == '__main__':
    app.run(debug=True)






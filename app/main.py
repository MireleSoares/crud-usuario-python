from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.json
    campos_obrigatorios = ['nome', 'email', 'senha', 'cpf']
    for campo in campos_obrigatorios:
        if campo not in dados:
            return jsonify({'erro': f'Campo obrigatório ausente: {campo}'}), 400

    usuarios.append(dados)
    return jsonify({'mensagem': 'Usuário criado com sucesso'}), 201

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios), 200

@app.route('/usuarios/<cpf>', methods=['GET'])
def obter_usuario(cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return jsonify(usuario), 200
    return jsonify({'erro': 'Usuário não encontrado'}), 404

@app.route('/usuarios/<cpf>', methods=['DELETE'])
def deletar_usuario(cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuarios.remove(usuario)
            return jsonify({'mensagem': 'Usuário removido com sucesso'}), 200
    return jsonify({'erro': 'Usuário não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
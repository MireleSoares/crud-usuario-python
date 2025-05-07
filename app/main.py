from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []

def adicionar_usuario(nome, email, senha, cpf):
    if any(u['cpf'] == cpf for u in usuarios):
        return None
    usuario = {'nome': nome, 'email': email, 'senha': senha, 'cpf': cpf}
    usuarios.append(usuario)
    return usuario

def buscar_usuario(cpf):
    return next((u for u in usuarios if u['cpf'] == cpf), None)

def remover_usuario(cpf):
    global usuarios
    usuario = buscar_usuario(cpf)
    if usuario:
        usuarios = [u for u in usuarios if u['cpf'] != cpf]
        return True
    return False

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    campos = ['nome', 'email', 'senha', 'cpf']
    if not all(c in dados for c in campos):
        return jsonify({'erro': 'Campos obrigatórios: nome, email, senha, cpf'}), 400

    usuario = adicionar_usuario(dados['nome'], dados['email'], dados['senha'], dados['cpf'])
    if not usuario:
        return jsonify({'erro': 'Usuário com este CPF já existe'}), 409
    return jsonify(usuario), 201

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios), 200

@app.route('/usuarios/<cpf>', methods=['GET'])
def obter_usuario(cpf):
    usuario = buscar_usuario(cpf)
    if usuario:
        return jsonify(usuario), 200
    return jsonify({'erro': 'Usuário não encontrado'}), 404

@app.route('/usuarios/<cpf>', methods=['DELETE'])
def excluir_usuario(cpf):
    if remover_usuario(cpf):
        return jsonify({'mensagem': 'Usuário removido com sucesso'}), 200
    return jsonify({'erro': 'Usuário não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)

from app.main import app, usuarios

def test_criacao_usuario_valido():
    usuarios.clear()
    app.testing = True
    client = app.test_client()
    response = client.post("/usuarios", json={
        "nome": "Maria",
        "email": "maria@email.com",
        "senha": "1234",
        "cpf": "11122233344"
    })
    json_data = response.get_json()
    assert response.status_code == 201
    assert json_data == {"mensagem": "Usuário criado com sucesso"}

def test_listagem_todos_usuarios():
    usuarios.clear()
    app.testing = True
    client = app.test_client()
    client.post("/usuarios", json={
        "nome": "João",
        "email": "joao@email.com",
        "senha": "abcd",
        "cpf": "22233344455"
    })
    response = client.get("/usuarios")
    json_data = response.get_json()
    assert response.status_code == 200
    assert len(json_data) == 1
    assert json_data[0]["nome"] == "João"

def test_busca_usuario_existente():
    usuarios.clear()
    app.testing = True
    client = app.test_client()
    client.post("/usuarios", json={
        "nome": "Ana",
        "email": "ana@email.com",
        "senha": "pass",
        "cpf": "33344455566"
    })
    response = client.get("/usuarios/33344455566")
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["nome"] == "Ana"

def test_busca_usuario_inexistente():
    usuarios.clear()
    app.testing = True
    client = app.test_client()
    response = client.get("/usuarios/00000000000")
    json_data = response.get_json()
    assert response.status_code == 404
    assert "erro" in json_data

def test_exclusao_usuario_existente():
    usuarios.clear()
    app.testing = True
    client = app.test_client()
    client.post("/usuarios", json={
        "nome": "Carlos",
        "email": "carlos@email.com",
        "senha": "senha",
        "cpf": "44455566677"
    })
    response = client.delete("/usuarios/44455566677")
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data == {"mensagem": "Usuário removido com sucesso"}

def test_exclusao_usuario_inexistente():
    usuarios.clear()
    app.testing = True
    client = app.test_client()
    response = client.delete("/usuarios/99988877766")
    json_data = response.get_json()
    assert response.status_code == 404
    assert "erro" in json_data
import pytest
from app.main import app, usuarios

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        usuarios.clear()
        yield client

def test_criar_usuario(client):
    res = client.post('/usuarios', json={
        'nome': 'João', 'email': 'joao@email.com',
        'senha': '1234', 'cpf': '11122233344'
    })
    assert res.status_code == 201
    assert res.get_json()['cpf'] == '11122233344'

def test_usuario_duplicado(client):
    client.post('/usuarios', json={
        'nome': 'Maria', 'email': 'maria@email.com',
        'senha': 'senha123', 'cpf': '00011122233'
    })
    res = client.post('/usuarios', json={
        'nome': 'Maria', 'email': 'maria@email.com',
        'senha': 'senha123', 'cpf': '00011122233'
    })
    assert res.status_code == 409

def test_listar_usuarios(client):
    client.post('/usuarios', json={
        'nome': 'Carlos', 'email': 'carlos@email.com',
        'senha': 'abc', 'cpf': '99988877766'
    })
    res = client.get('/usuarios')
    assert res.status_code == 200
    assert isinstance(res.get_json(), list)

def test_obter_usuario_por_cpf(client):
    client.post('/usuarios', json={
        'nome': 'Ana', 'email': 'ana@email.com',
        'senha': 'xyz', 'cpf': '12345678900'
    })
    res = client.get('/usuarios/12345678900')
    assert res.status_code == 200
    assert res.get_json()['nome'] == 'Ana'

def test_excluir_usuario(client):
    client.post('/usuarios', json={
        'nome': 'Davi', 'email': 'davi@email.com',
        'senha': 'pass', 'cpf': '11122233344'
    })
    res = client.delete('/usuarios/11122233344')
    assert res.status_code == 200

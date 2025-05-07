# CRUD de Usuários em Python

API REST simples feita com Flask para cadastro de usuários em memória (lista de dicionários).

## Funcionalidades

- Criar usuário (`POST /usuarios`)
- Listar todos os usuários (`GET /usuarios`)
- Buscar usuário por CPF (`GET /usuarios/<cpf>`)
- Deletar usuário por CPF (`DELETE /usuarios/<cpf>`)

## Como executar

```bash
pip install -r requirements.txt
python app/main.py

# User Service

Microserviço responsável pelo **gerenciamento de usuários** dentro da arquitetura de microserviços da aplicação.

Ele fornece uma API REST para realizar operações de **CRUD de usuários**, incluindo:

* criação
* consulta
* atualização
* remoção

O serviço foi desenvolvido utilizando **FastAPI**, **SQLAlchemy** e **PostgreSQL**.

---

# Arquitetura

Este serviço faz parte de uma arquitetura baseada em **microservices**, onde cada serviço é responsável por um domínio específico da aplicação.

Exemplo de arquitetura:

```
Client
   │
   ▼
API Gateway
   │
   ├── user_service
   ├── product_service
   └── order_service
```

O **user_service** é responsável exclusivamente pelo **domínio de usuários**.

---

# Tecnologias

* Python 3.10+
* FastAPI
* SQLAlchemy
* Pydantic
* Uvicorn
* PostgreSQL
* Docker

---

# Estrutura do Projeto

```
app/
│
├── main.py
├── database.py
│
├── routers/
│   └── user_router.py
│
├── services/
│   └── user_service.py
│
├── schemas/
│   └── user_schema.py
│
└── models/
    └── user_model.py
```

Responsabilidades:

| Camada   | Responsabilidade                 |
| -------- | -------------------------------- |
| routers  | define endpoints da API          |
| services | lógica de negócio                |
| schemas  | validação e serialização         |
| models   | definição das entidades do banco |
| database | conexão com banco                |

---

# Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/user_service.git
cd user_service
```

Crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente:

Linux/Mac

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# Executando a Aplicação

```bash
uvicorn app.main:app --reload
```

A API ficará disponível em:

```
http://localhost:8000
```

---

# Documentação da API

FastAPI gera documentação automática.

Swagger:

```
http://localhost:8000/docs
```

Redoc:

```
http://localhost:8000/redoc
```

---

# Endpoints

Base URL

```
/users
```

---

# Listar usuários

```
GET /users
```

Response:

```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@email.com"
  }
]
```

---

# Buscar usuário

```
GET /users/{user_id}
```

Exemplo:

```
GET /users/1
```

Response:

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@email.com"
}
```

---

# Criar usuário

```
POST /users
```

Body:

```json
{
  "name": "John Doe",
  "email": "john@email.com",
  "password": "123456"
}
```

Response:

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@email.com"
}
```

---

# Atualizar usuário

```
PUT /users/{user_id}
```

Body:

```json
{
  "name": "John Updated",
  "email": "johnupdated@email.com"
}
```

---

# Deletar usuário

```
DELETE /users/{user_id}
```

Response:

```json
{
  "message": "User deleted"
}
```

---

# Exemplos com cURL

Criar usuário:

```bash
curl -X POST http://localhost:8000/users \
-H "Content-Type: application/json" \
-d '{
"name": "John Doe",
"email": "john@email.com",
"password": "123456"
}'
```

Listar usuários:

```bash
curl http://localhost:8000/users
```

Buscar usuário:

```bash
curl http://localhost:8000/users/1
```

---

# Modelos de Dados

### UserCreate

```python
name: str
email: str
password: str
```

### UserUpdate

```python
name: Optional[str]
email: Optional[str]
password: Optional[str]
```

### UserResponse

```python
id: int
name: str
email: str
```

---

# Executando com Docker (Opcional)

Build da imagem:

```bash
docker build -t user_service .
```

Rodar container:

```bash
docker run -p 8000:8000 user_service
```

---

# Boas práticas utilizadas

* Separação por camadas
* Tipagem com Pydantic
* Injeção de dependência do FastAPI
* Estrutura modular
* Documentação automática

---

# Melhorias Futuras

* autenticação com JWT
* integração com API Gateway
* testes automatizados
* CI/CD
* observabilidade (logs e métricas)

---

# Licença

Este projeto está sob licença MIT.

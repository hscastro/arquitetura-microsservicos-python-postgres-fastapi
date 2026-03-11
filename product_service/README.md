# Product Service

Microserviço responsável pelo **gerenciamento de produtos** dentro da arquitetura de microserviços do sistema de e-commerce.

Este serviço fornece uma API REST para realizar operações de **CRUD de produtos**, permitindo que outros serviços (como `order_service`) consultem os produtos disponíveis no sistema.

---

# Responsabilidade

O **product_service** gerencia:

* criação de produtos
* listagem de produtos
* consulta de produto por ID
* atualização de produtos
* remoção de produtos

---

# Tecnologias Utilizadas

* Python 3.10+
* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic
* Uvicorn
* Docker

---

# Arquitetura

Este serviço faz parte de uma arquitetura baseada em **microservices**.

```text id="h5yx1k"
Client
   │
   ▼
API Gateway
   │
   ├── user_service
   ├── product_service
   └── order_service
```

O **product_service** é responsável exclusivamente pelo **domínio de produtos**.

---

# Estrutura do Projeto

```id="s7l4m2"
app
│
├── main.py
├── database.py
│
├── routers
│   └── product_router.py
│
├── services
│   └── product_service.py
│
├── models
│   └── product_model.py
│
├── schemas
│   └── product_schema.py
│
└── core
    └── config.py
```

---

# Banco de Dados

Tabela: **products**

| Campo       | Tipo     | Descrição                |
| ----------- | -------- | ------------------------ |
| id          | integer  | Identificador do produto |
| name        | string   | Nome do produto          |
| description | string   | Descrição do produto     |
| price       | float    | Preço do produto         |
| created_at  | datetime | Data de criação          |

---

# Executando o Serviço

Instalar dependências:

```bash id="7ar8xg"
pip install -r requirements.txt
```

Executar a aplicação:

```bash id="9fkm1w"
uvicorn app.main:app --reload
```

A API ficará disponível em:

```id="4k0v19"
http://localhost:8000
```

---

# Documentação da API

FastAPI gera documentação automática.

Swagger:

```id="n3y6gh"
http://localhost:8000/docs
```

Redoc:

```id="g5czl8"
http://localhost:8000/redoc
```

---

# Endpoints

Base URL:

```id="x3z6kq"
/products
```

---

# Health Check

Verifica se o serviço está ativo.

```id="v3f9bn"
GET /products/health
```

Response:

```json id="27jv06"
{
  "status": "ok",
  "service": "product_service"
}
```

---

# Listar Produtos

Retorna todos os produtos cadastrados.

```id="8u0vzy"
GET /products
```

Response:

```json id="v4p3h0"
[
  {
    "id": 1,
    "name": "Notebook",
    "description": "Notebook Dell",
    "price": 3500
  }
]
```

---

# Buscar Produto por ID

Retorna um produto específico.

```id="6s6xai"
GET /products/{product_id}
```

Exemplo:

```id="ueox6s"
GET /products/1
```

Response:

```json id="3h9r0n"
{
  "id": 1,
  "name": "Notebook",
  "description": "Notebook Dell",
  "price": 3500
}
```

---

# Criar Produto

Cria um novo produto.

```id="q08k0i"
POST /products
```

Request:

```json id="fkt4y9"
{
  "name": "Mouse Gamer",
  "description": "Mouse RGB",
  "price": 120
}
```

Response:

```json id="fxnytr"
{
  "id": 2,
  "name": "Mouse Gamer",
  "description": "Mouse RGB",
  "price": 120
}
```

---

# Atualizar Produto

Atualiza os dados de um produto.

```id="dfn9ea"
PUT /products/{product_id}
```

Request:

```json id="yqqm6p"
{
  "name": "Mouse Gamer Pro",
  "description": "Mouse RGB atualizado",
  "price": 150
}
```

---

# Deletar Produto

Remove um produto do sistema.

```id="nf1egf"
DELETE /products/{product_id}
```

Response:

```json id="7ntvyf"
{
  "message": "Product deleted"
}
```

---

# Modelos de Dados

## ProductCreate

Usado para criação de produtos.

```id="ysclyq"
name: str
description: str
price: float
```

---

## ProductUpdate

Usado para atualização de produtos.

```id="ef2p9s"
name: Optional[str]
description: Optional[str]
price: Optional[float]
```

---

## ProductResponse

Resposta retornada pela API.

```id="ht6ksn"
id: int
name: str
description: str
price: float
```

---

# Executando com Docker

Build da imagem:

```bash id="1h4p2q"
docker build -t product_service .
```

Executar container:

```bash id="x1sh0k"
docker run -p 8000:8000 product_service
```

---

# Boas Práticas Utilizadas

* arquitetura em camadas
* separação entre routers, services e models
* validação com Pydantic
* documentação automática do FastAPI
* injeção de dependência com `Depends`

---

# Melhorias Futuras

* autenticação com JWT
* cache de produtos com Redis
* integração com `order_service`
* testes automatizados com Pytest
* pipeline de CI/CD


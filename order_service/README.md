# Order Service

Microserviço responsável pelo **gerenciamento de pedidos de compra** dentro da arquitetura de microserviços do sistema de e-commerce.

Este serviço orquestra o fluxo principal de compras, registrando pedidos realizados pelos usuários e os itens associados a cada pedido.

---

# Responsabilidade

O **order_service** gerencia:

* criação de pedidos
* listagem de pedidos
* consulta de pedidos por ID
* registro de itens de cada pedido

Cada pedido pode conter **vários itens**, representando os produtos comprados.

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

O serviço faz parte de uma arquitetura baseada em **microservices**.

Exemplo de arquitetura:

```text
Client
   │
   ▼
API Gateway
   │
   ├── user_service
   ├── product_service
   └── order_service
```

O **order_service** recebe pedidos e registra os itens associados.

---

# Estrutura do Projeto

```
app
│
├── main.py
├── database.py
│
├── routers
│   └── order_router.py
│
├── services
│   └── order_service.py
│
├── models
│   ├── order_model.py
│   └── order_item_model.py
│
├──schemas
    └── order_schema.py


```

---

# Banco de Dados

O serviço utiliza duas tabelas principais.

## Tabela: `orders`

| Campo       | Tipo     | Descrição                           |
| ----------- | -------- | ----------------------------------- |
| id          | integer  | Identificador do pedido             |
| user_id     | integer  | ID do usuário que realizou o pedido |
| status      | string   | Status do pedido                    |
| total_price | float    | Valor total do pedido               |
| created_at  | datetime | Data de criação                     |

---

## Tabela: `order_items`

| Campo      | Tipo    | Descrição                             |
| ---------- | ------- | ------------------------------------- |
| id         | integer | Identificador do item                 |
| order_id   | integer | ID do pedido                          |
| product_id | integer | ID do produto                         |
| quantity   | integer | Quantidade comprada                   |
| price      | float   | Preço do produto no momento da compra |

---

# Relação entre as tabelas

```
orders (1) ────────── (N) order_items
```

Um **pedido pode ter vários itens**.

---

# Executando o Serviço

Instalar dependências:

```bash
pip install -r requirements.txt
```

Executar o servidor:

```bash
uvicorn app.main:app --reload
```

A API ficará disponível em:

```
http://localhost:8000
```

---

# Documentação da API

FastAPI gera documentação automaticamente.

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

Base URL:

```
/orders
```

---

# Health Check

Verifica se o serviço está funcionando.

```
GET /orders/health
```

Response:

```json
{
  "status": "ok",
  "service": "order_service"
}
```

---

# Criar Pedido

Cria um novo pedido com seus itens.

```
POST /orders
```

### Request

```json
{
  "user_id": 1,
  "items": [
    {
      "product_id": 1,
      "quantity": 2,
      "price": 50.0
    },
    {
      "product_id": 3,
      "quantity": 1,
      "price": 120.0
    }
  ]
}
```

### Response

```json
{
  "id": 1,
  "user_id": 1,
  "status": "created",
  "total_price": 220.0,
  "created_at": "2026-03-11T12:00:00",
  "items": [
    {
      "id": 1,
      "product_id": 1,
      "quantity": 2,
      "price": 50.0
    },
    {
      "id": 2,
      "product_id": 3,
      "quantity": 1,
      "price": 120.0
    }
  ]
}
```

---

# Listar Pedidos

Retorna todos os pedidos cadastrados.

```
GET /orders
```

Response:

```json
[
  {
    "id": 1,
    "user_id": 1,
    "status": "created",
    "total_price": 220.0,
    "created_at": "2026-03-11T12:00:00",
    "items": []
  }
]
```

---

# Buscar Pedido por ID

Retorna um pedido específico.

```
GET /orders/{order_id}
```

Exemplo:

```
GET /orders/1
```

---

# Modelos de Dados

## OrderCreate

Utilizado para criar pedidos.

```
user_id: int
items: list[OrderItemCreate]
```

---

## OrderItemCreate

Representa um item dentro do pedido.

```
product_id: int
quantity: int
price: float
```

---

## OrderResponse

Resposta retornada pela API.

```
id: int
user_id: int
status: str
total_price: float
created_at: datetime
items: list[OrderItemResponse]
```

---

# Executando com Docker

Build da imagem:

```bash
docker build -t order_service .
```

Executar container:

```bash
docker run -p 8000:8000 order_service
```

---

# Boas Práticas Utilizadas

* arquitetura em camadas
* separação entre router, service e model
* validação com Pydantic
* documentação automática com FastAPI
* uso de relacionamentos com SQLAlchemy

---

# Melhorias Futuras

* autenticação com JWT
* comunicação entre microservices
* integração com product_service
* testes automatizados
* mensageria com RabbitMQ ou Kafka
* CI/CD pipeline


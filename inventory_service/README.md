# Inventory Service

Microserviço responsável pelo gerenciamento de inventário.  
Ele permite criar, consultar, atualizar e remover registros de inventário através de uma API REST.


## Objetivo do Serviço

Este microserviço faz parte de uma arquitetura baseada em microserviços, sendo responsável exclusivamente pelo gerenciamento de inventário de produtos.

Suas responsabilidades incluem:

controle de estoque

consulta de disponibilidade

atualização de quantidades

manutenção de registros de inventário

## Tecnologias

- Python
- FastAPI
- SQLAlchemy
- Pydantic

## Base URL


/inventory


## Endpoints

### Health Check

Verifica se o serviço está ativo.

**GET** `/health`

#### Response
```json
{
  "status": "ok",
  "service": "inventory_service"
}

```
## Listar Inventários

Retorna todos os registros de inventário.

GET /

Response
[
  {
    "id": 1,
    "product_id": 10,
    "quantity": 50
  }
]

## Buscar Inventário por ID

Retorna um inventário específico.

GET /{inventory_id}

Parâmetros
Parâmetro	Tipo	Descrição
inventory_id	integer	ID do inventário
Response
{
  "id": 1,
  "product_id": 10,
  "quantity": 50
}

## Criar Inventário

Cria um novo registro de inventário.

POST /

Body
{
  "product_id": 10,
  "quantity": 50
}
Response
{
  "id": 1,
  "product_id": 10,
  "quantity": 50
}
## Atualizar Inventário

Atualiza um inventário existente.

PUT /{inventory_id}

Parâmetros
Parâmetro	Tipo	Descrição
inventory_id	integer	ID do inventário
Body
{
  "product_id": 10,
  "quantity": 100
}
Response
{
  "id": 1,
  "product_id": 10,
  "quantity": 100
}
## Deletar Inventário

Remove um registro de inventário.

DELETE /{inventory_id}

Parâmetros
Parâmetro	Tipo	Descrição
inventory_id	integer	ID do inventário
Response
{
  "message": "Inventory deleted"
}

## Estrutura Esperada dos Schemas

InventoryCreate
{
  "product_id": "integer",
  "quantity": "integer"
}
InventoryUpdate
{
  "product_id": "integer",
  "quantity": "integer"
}
InventoryResponse
{
  "id": "integer",
  "product_id": "integer",
  "quantity": "integer"
}

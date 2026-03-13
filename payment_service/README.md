## 💳 Payment Service

Microserviço responsável por gerenciar pagamentos em uma arquitetura de microserviços para e-commerce.

O serviço permite:

Criar pagamentos

Consultar pagamentos

Buscar pagamento por ID

Remover pagamentos

Verificar status do serviço (health check)

## A API é construída utilizando FastAPI, com persistência de dados via SQLAlchemy.

📚 Sumário

Arquitetura

Tecnologias

Estrutura do Projeto

Instalação

Executando o Serviço

Documentação da API

Endpoints

Modelo de Dados

Integração com Microserviços

Melhorias Futuras


## 🏗 Arquitetura

O projeto segue uma arquitetura em camadas, separando responsabilidades para facilitar manutenção e escalabilidade.

Router → Service → Repository → Database

## Fluxo de requisição:

Client Request
      │
      ▼
Router (FastAPI)
      │
      ▼
Service Layer (Regras de negócio)
      │
      ▼
Repository Layer (Acesso ao banco)
      │
      ▼
Database
## 🧰 Tecnologias

Principais tecnologias utilizadas no projeto:

FastAPI — Framework moderno para APIs

SQLAlchemy — ORM para banco de dados

Pydantic — Validação de dados

Uvicorn — Servidor ASGI

Python 3.10+

## 📁 Estrutura do Projeto
payment_service
│
├── app
│   │
│   ├── main.py
│   ├── database.py
│   │
│   ├── models
│   │   └── payment_model.py
│   │
│   ├── schemas
│   │   └── payment_schema.py
│   │
│   ├── repositories
│   │   └── payment_repository.py
│   │
│   ├── services
│   │   └── payment_service.py
│   │
│   └── routers
│       └── payment_router.py
│
└── requirements.txt


## ▶️ Executando o Serviço

Execute o servidor com:

uvicorn app.main:app --reload

O serviço ficará disponível em:

http://localhost:8000

## 📖 Documentação da API

A documentação interativa é gerada automaticamente pelo FastAPI.

Swagger UI
http://localhost:8000/docs
ReDoc
http://localhost:8000/redoc
🔌 Endpoints
Health Check

## Verifica se o serviço está ativo.

GET /payments/health

Response:

{
  "status": "ok",
  "service": "Payment_service"
}

## Criar pagamento
POST /payments/

Request:

{
  "order_id": 1,
  "amount": 150.0,
  "provider": "stripe"
}

Response:

{
  "id": 1,
  "order_id": 1,
  "amount": 150.0,
  "provider": "stripe",
  "status": "SUCCESS",
  "created_at": "2026-03-13T20:10:00"
}

## Listar pagamentos
GET /payments/

Response:

[
  {
    "id": 1,
    "order_id": 1,
    "amount": 150.0,
    "provider": "stripe",
    "status": "SUCCESS",
    "created_at": "2026-03-13T20:10:00"
  }
]

## Buscar pagamento por ID
GET /payments/{payment_id}
Remover pagamento

## DELETE /payments/{payment_id}

Response:

{
  "message": "Payment deleted"
}




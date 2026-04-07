🧩 E-commerce Microservices Architecture (Professional README)

Este repositório apresenta uma arquitetura de microserviços para um sistema de e-commerce, projetada com foco em escalabilidade, manutenibilidade e baixo acoplamento, utilizando FastAPI e princípios de Clean Architecture.

Cada microserviço possui responsabilidade única e expõe APIs REST bem definidas para comunicação entre serviços.

📚 Sumário
Arquitetura
Tecnologias
Estrutura do Projeto
Instalação
Execução
Microserviços
Product Service
Order Service
Payment Service
User Service
Notification Service
Inventory Service
Integração
Melhorias Futuras

🏗️ Arquitetura
Arquitetura baseada em microserviços
Banco de dados por serviço
Comunicação via REST (evolução para eventos)
Clean Architecture:
Domain → regras de negócio
Application → casos de uso
Infrastructure → integrações externas
Interfaces → API

⚙️ Tecnologias
Python 3.10+
FastAPI
SQLAlchemy
PostgreSQL
Pydantic
Uvicorn
Docker

📁 Estrutura Base
```
app/
├── application/
├── domain/
├── infrastructure/
├── interfaces/
├── database/
└── main.py
```

🚀 Instalação
git clone <repo-url>
cd project

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt

▶️ Execução
uvicorn app.main:app --reload

🧩 Microserviços
📦 Product Service
📖 Descrição

Gerencia produtos disponíveis no sistema.

🎯 Responsabilidades
CRUD de produtos

🔌 Exemplo de Request

POST /products
```
{
  "name": "Notebook Dell",
  "description": "Notebook i7 16GB RAM",
  "price": 4500.00
}
```

📥 Exemplo de Response
```
{
  "id": 1,
  "name": "Notebook Dell",
  "description": "Notebook i7 16GB RAM",
  "price": 4500.00,
  "created_at": "2026-04-06T12:00:00"
}
```

🛒 Order Service
📖 Descrição

Gerencia pedidos e orquestra o fluxo de compra.

🎯 Responsabilidades
Criar pedidos
Gerenciar itens do pedido

🔌 Exemplo de Request

POST /orders
```
{
  "user_id": 10,
  "items": [
    {
      "product_id": 1,
      "quantity": 2
    }
  ]
}
```

📥 Exemplo de Response
```
{
  "id": 100,
  "user_id": 10,
  "status": "CREATED",
  "total": 9000.00,
  "items": [
    {
      "product_id": 1,
      "quantity": 2,
      "price": 4500.00
    }
  ]
}
```

💳 Payment Service
📖 Descrição

Gerencia pagamentos dos pedidos.

🎯 Funcionalidades
Criar pagamento
Consultar pagamento

🔌 Exemplo de Request

POST /payments
```
{
  "order_id": 100,
  "amount": 9000.00,
  "method": "CREDIT_CARD"
}
```

📥 Exemplo de Response
```
{
  "id": 500,
  "order_id": 100,
  "status": "APPROVED",
  "amount": 9000.00,
  "processed_at": "2026-04-06T12:05:00"
}
```
👤 User Service
📖 Descrição

Gerencia usuários do sistema.

🔌 Exemplo de Request

POST /users
```
{
  "name": "Antonio Castro",
  "email": "antonio@email.com"
}
```

📥 Exemplo de Response
```
{
  "id": 10,
  "name": "Antonio Castro",
  "email": "antonio@email.com",
  "created_at": "2026-04-06T11:50:00"
}
```

🔔 Notification Service
📖 Descrição

Gerencia notificações do sistema.

🔌 Exemplo de Request

POST /notifications
```
{
  "user_id": 10,
  "message": "Seu pedido foi aprovado"
}
```

📥 Exemplo de Response
```
{
  "id": 900,
  "user_id": 10,
  "message": "Seu pedido foi aprovado",
  "status": "SENT"
}
```

📦 Inventory Service
📖 Descrição

Gerencia estoque de produtos.

🎯 Responsabilidades
Controle de estoque
Reserva de produtos

🔌 Exemplo de Request

POST /inventory
```
{
  "product_id": 1,
  "available_quantity": 100,
  "reserved_quantity": 0
}
```

📥 Exemplo de Response
```
{
  "product_id": 1,
  "available_quantity": 100,
  "reserved_quantity": 0,
  "updated_at": "2026-04-06T12:10:00"
}
```
🔗 Integração entre Serviços

Fluxo típico:

User cria pedido → Order Service
Order consulta produtos → Product Service
Order valida estoque → Inventory Service
Order envia pagamento → Payment Service
Payment confirma → Notification Service

🚧 Melhorias Futuras
JWT + OAuth2
API Gateway
Kafka (event-driven)
Retry + DLQ
Observabilidade (Prometheus + Grafana)
Cache com Redis
Testcontainers

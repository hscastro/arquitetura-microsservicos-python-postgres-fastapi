## 🔔 Notification Service

Microserviço responsável por gerenciar notificações dentro de uma arquitetura de microserviços para e-commerce.

O serviço permite:

Criar notificações
Listar notificações
Buscar notificação por ID
Atualizar notificações
Remover notificações
Verificar saúde do serviço (health check)

## 📚 Sumário

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

O serviço segue uma arquitetura em camadas para melhor organização e escalabilidade.

## Fluxo de requisição:

Client
  │
  ▼
Router (FastAPI)
  │
  ▼
Service Layer
  │
  ▼
Repository Layer
  │
  ▼
Database

Essa abordagem separa:

Rotas → entrada da API

Services → regras de negócio

Repositories → acesso ao banco

Models/Schemas → estrutura de dados

## 🧰 Tecnologias

Principais tecnologias utilizadas:

FastAPI — Framework moderno para APIs REST

SQLAlchemy — ORM para persistência de dados

Pydantic — Validação de dados

Uvicorn — Servidor ASGI

## 📁 Estrutura do Projeto

notification_service
│
├── app
│   │
│   ├── main.py
│   ├── database.py
│   │
│   ├── models
│   │   └── notification_model.py
│   │
│   ├── schemas
│   │   └── notification_schema.py
│   │
│   ├── repositories
│   │   └── notification_repository.py
│   │
│   ├── services
│   │   └── notification_service.py
│   │
│   └── routers
│       └── notification_router.py
│
└── requirements.txt

## 3️⃣ Instalar dependências

pip install -r requirements.txt

## ▶️ Executando o Serviço

Inicie o servidor:

uvicorn app.main:app --reload

O serviço estará disponível em:

http://localhost:8000


## 📖 Documentação da API

A documentação interativa é gerada automaticamente.

Swagger UI:

http://localhost:8000/docs

ReDoc:

http://localhost:8000/redoc

## 🔌 Endpoints
Health Check

## Verifica se o serviço está funcionando.

GET /notifications/health

Response:

{
  "status": "ok",
  "service": "Notification_service"
}

## Listar notificações
GET /notifications/

Response:

[
  {
    "id": 1,
    "message": "Order created",
    "type": "email",
    "status": "sent"
  }
]

## Buscar notificação por ID
GET /notifications/{notification_id}

Exemplo:

GET /notifications/1

Response:

{
  "id": 1,
  "message": "Order created",
  "type": "email",
  "status": "sent"
}

## Criar notificação
POST /notifications/

Request:

{
  "message": "Payment successful",
  "type": "email"
}

Response:

{
  "id": 2,
  "message": "Payment successful",
  "type": "email",
  "status": "pending"
}

## Atualizar notificação
PUT /notifications/{notification_id}

Request:

{
  "status": "sent"
}

Response:

{
  "id": 2,
  "message": "Payment successful",
  "type": "email",
  "status": "sent"
}

## Deletar notificação
DELETE /notifications/{notification_id}

Response:

{
  "message": "Notification deleted"
}

## 🗄 Modelo de Dados

Exemplo de estrutura de notificação:

Campo	Tipo	Descrição
id	Integer	Identificador da notificação
message	String	Conteúdo da notificação
type	String	Tipo da notificação (email, sms, push)
status	String	Status da notificação
created_at	DateTime	Data de criação

## 🔗 Integração com Microserviços

Este serviço pode receber eventos de outros serviços da plataforma:

Serviço	Evento
Order Service	Pedido criado
Payment Service	Pagamento confirmado
Inventory Service	Estoque atualizado

## Fluxo comum:

Order Created
     │
     ▼
Notification Service
     │
     ▼
Send Email / SMS / Push

## 🚀 Melhorias Futuras

Integração com serviços de email (SendGrid / SES)

Envio de SMS (Twilio)
Push notifications
Processamento assíncrono com filas
Integração com RabbitMQ ou Kafka
Logs estruturados
Dockerização do serviço
Testes automatizados


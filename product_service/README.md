Product Service

Microserviço responsável pelo gerenciamento de produtos dentro do ecossistema da aplicação.
Ele disponibiliza uma API REST para operações de CRUD de produtos, permitindo que outros serviços consultem, criem, atualizem ou removam produtos.

Este serviço foi desenvolvido utilizando arquitetura em camadas, promovendo separação de responsabilidades, facilidade de manutenção e testabilidade.


Responsabilidades do Serviço

O Product Service é responsável por:

Cadastro de produtos

Consulta de produtos

Atualização de informações de produtos

Exclusão de produtos

Persistência de dados no banco

Este serviço não contém regras de negócio de outros domínios, mantendo o princípio de single responsibility para microserviços.

Arquitetura do Microserviço

O serviço segue uma arquitetura em camadas:

Controller (API)
     │
     ▼
Service Layer
     │
     ▼
Repository / ORM
     │
     ▼
Database

Camadas

Controller (Router)
Responsável por expor os endpoints HTTP.

Service Layer
Contém as regras de negócio do domínio de produtos.

Repository / ORM
Responsável pela comunicação com o banco via SQLAlchemy.

Database
Persistência dos dados.

Diagrama de Arquitetura

                ┌─────────────────────┐
                │     Client / API    │
                │ (Frontend / Other MS)│
                └───────────┬─────────┘
                            │
                            ▼
                  ┌──────────────────┐
                  │     FastAPI      │
                  │  Product Router  │
                  └──────────┬───────┘
                             │
                             ▼
                  ┌──────────────────┐
                  │  Product Service │
                  │ Business Logic   │
                  └──────────┬───────┘
                             │
                             ▼
                  ┌──────────────────┐
                  │   SQLAlchemy ORM │
                  │     Repository   │
                  └──────────┬───────┘
                             │
                             ▼
                  ┌──────────────────┐
                  │     Database     │
                  │  (PostgreSQL /   │
                  │    MySQL etc)    │
                  └──────────────────┘

Listar Produtos

Retorna todos os produtos cadastrados.

Response

[
  {
    "id": 1,
    "name": "Product A",
    "price": 100.0,
    "description": "Example product"
  }
]

Buscar Produto por ID

Retorna um produto específico.

GET /products/{product_id}

Response

{
  "id": 1,
  "name": "Product A",
  "price": 100.0,
  "description": "Example product"
}

Criar Produto

Cria um novo produto.

POST /products/

Request Body

{
  "name": "Product A",
  "price": 100.0,
  "description": "Example product"
}

Response

{
  "id": 1,
  "name": "Product A",
  "price": 100.0,
  "description": "Example product"
}

Estrutura do Projeto

Exemplo de organização recomendada:

app
│
├── main.py
│
├── database
│   └── database.py
│
├── models
│   └── product_model.py
│
├── schemas
│   └── product_schema.py
│
├── routers
│   └── product_router.py
│
├── services
│   └── product_service.py
│
└── repositories
    └── product_repository.py

Execução do Projeto
Instalar dependências

pip install -r requirements.txt

Rodar aplicação

uvicorn app.main:app --reload

Servidor disponível em:

http://localhost:8000

Documentação Automática

O FastAPI gera documentação automaticamente:

Swagger

http://localhost:8000/docs

Redoc

http://localhost:8000/redoc


Boas Práticas Aplicadas

Separação de camadas

Dependency Injection

Validação de dados com Pydantic

Padrão REST

Código desacoplado
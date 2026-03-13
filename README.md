# Microservices E-commerce Architecture

Arquitetura baseada em **microserviços** para uma plataforma de e-commerce escalável, utilizando **FastAPI**, mensageria com **Kafka**, cache com **Redis** e observabilidade com **Prometheus + Grafana**.

## Visão Geral da Arquitetura

Client (Web/Mobile)
│
▼
API Gateway (Traefik)
│
┌───────────────┬───────────────┬───────────────┬───────────────┐
▼ ▼ ▼ ▼
Auth Service User Service Order Service Product Service
│ │ │ │
▼ ▼ ▼ ▼
PostgreSQL PostgreSQL PostgreSQL PostgreSQL

  │
  ▼

Kafka (Event Streaming)
┌───────────────┬───────────────┬───────────────┐
▼ ▼ ▼
Payment Service Notification Inventory Service
│
▼
Redis

  │
  ▼

Observability (Prometheus + Grafana)


## Componentes

### API Gateway
- **Traefik**
- Responsável por roteamento das requisições, balanceamento de carga e entrada única da aplicação.

### Core Services
Serviços principais responsáveis pela lógica central da aplicação.

- **Auth Service** → autenticação e autorização
- **User Service** → gerenciamento de usuários
- **Product Service** → catálogo de produtos
- **Order Service** → processamento de pedidos

Cada serviço possui **banco PostgreSQL isolado**, seguindo o princípio de **database per service**.

### Event Streaming

- **Kafka**
- Comunicação assíncrona entre microserviços
- Permite desacoplamento e escalabilidade do sistema.

### Async Services

Serviços que reagem a eventos do sistema:

- **Payment Service** → processamento de pagamentos
- **Inventory Service** → controle de estoque
- **Notification Service** → envio de notificações

### Cache e Sessões

- **Redis**
- Utilizado para cache, sessões e otimização de performance.

### Observabilidade

- **Prometheus** → coleta de métricas
- **Grafana** → visualização e monitoramento

## Características da Arquitetura

- Arquitetura baseada em **microserviços**
- **API Gateway** centralizado
- Comunicação **síncrona (REST)** e **assíncrona (Kafka)**
- **Banco de dados isolado por serviço**
- **Escalabilidade horizontal**
- **Observabilidade integrada**

## Tecnologias

- **FastAPI**
- **PostgreSQL**
- **Kafka**
- **Redis**
- **Traefik**
- **Prometheus**
- **Grafana**
- **Docker / Docker Compose**



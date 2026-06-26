# E-Commerce Analytics Platform

A data engineering and analytics platform built with Python, PostgreSQL, FastAPI, Streamlit, and Docker.

The project demonstrates a complete data pipeline from raw e-commerce data to interactive analytics dashboards and REST API endpoints.

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- FastAPI
- Streamlit
- Docker
- Docker Compose
- Git
- GitHub Actions
- Pytest

## Features

- ETL pipeline for e-commerce data
- PostgreSQL database
- REST API with FastAPI
- Interactive Streamlit dashboard
- Dockerized application
- Automated API tests
- GitHub Actions CI

## Architecture

```text
Raw CSV
   │
   ▼
ETL Pipeline
   │
   ▼
PostgreSQL
   │
   ▼
FastAPI
   │
   ▼
Streamlit Dashboard
```

## Project Structure

```text
ecommerce-analytics-platform/
│
├── api/
├── dashboard/
├── database/
├── data/
├── etl/
├── tests/
├── Dockerfile
├── Dockerfile.dashboard
├── docker-compose.yml
└── README.md
```

## Installation

```bash
git clone <repository>

cd ecommerce-analytics-platform

docker compose up --build
```


# 8. API

| Endpoint | Beschreibung |
|----------|--------------|
| `/summary` | KPI summary |
| `/top-categories` | Top product categories |
| `/monthly-revenue` | Monthly revenue |
| `/orders-by-state` | Orders grouped by state |

# 9. Dashboard

# 10. Tests

```md
## Running Tests
```

```bash
python -m pytest tests
```

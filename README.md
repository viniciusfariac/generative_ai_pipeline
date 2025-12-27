# generative_ai_pipeline

Este projeto replica o desafio prático do **BootCamp santander-2025-ciencia-de-dados-com-python da dio**, aplicando conceitos de **Ciência de Dados**, **Python** e **ETL (Extract, Transform, Load)**.

Devido à indisponibilidade da API original utilizada no desafio, o fluxo foi adaptado para trabalhar com **arquivos CSV**, mantendo a mesma lógica de processamento apresentada no projeto oficial.

---

## 📌 Objetivo

Demonstrar a construção de um pipeline ETL completo que:

- Extrai dados de usuários a partir de um arquivo CSV
- Gera mensagens personalizadas de marketing utilizando IA generativa
- Atualiza os dados processados simulando a persistência que seria feita via API

---

## 🔄 Fluxo ETL

### 1️⃣ Extração (Extract)
- Leitura do arquivo `users.csv`
- Cada linha representa um cliente do banco

### 2️⃣ Transformação (Transform)
- Para cada cliente, uma mensagem personalizada é gerada
- A IA simula o papel de um agente de marketing do Santander
- A mensagem gerada é associada ao respectivo cliente

### 3️⃣ Carregamento (Load)
- Os dados são atualizados diretamente no DataFrame
- O arquivo CSV é sobrescrito, simulando a atualização que seria feita pela API

---

## 📂 Estrutura do Projeto

```text
generative_ai_pipeline/
│
├── data/
│   └── users.csv
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
├── .gitignore
├── requirements.txt
└── README.md

# 🚀 Blogging Platform API (Flask)

Uma API RESTful simples para gerenciamento de posts de blog, desenvolvida em Python com Flask. Este projeto implementa operações completas de CRUD e segue boas práticas de APIs REST.

---

## 📌 Sobre o Projeto

Esta API permite que usuários:

* Criem novos posts
* Visualizem todos os posts
* Busquem posts por ID
* Atualizem posts existentes
* Deletem posts
* Filtrarem posts por termos de busca

---

## 🧠 Conceitos aplicados

* REST API
* CRUD (Create, Read, Update, Delete)
* Métodos HTTP (GET, POST, PUT, DELETE)
* Manipulação de JSON
* Status Codes (200, 201, 400, 404, 204)
* Estrutura de backend com Flask

---

## 🛠️ Tecnologias utilizadas

* Python 3
* Flask

---

## 📁 Estrutura do Projeto

```
blog-api/
│
├── app.py
```

---

## ⚙️ Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/blog-api.git
cd blog-api
```

---

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

Ative o ambiente:

* Windows:

```bash
venv\Scripts\activate
```

---

### 3. Instale as dependências

```bash
pip install flask
```

---

### 4. Execute a aplicação

```bash
python app.py
```

A API estará disponível em:

```
http://127.0.0.1:5000
```

---

## 🧪 Endpoints da API

### 🔹 Criar post

```
POST /posts
```

Body:

```json
{
  "title": "Meu post",
  "content": "Conteúdo aqui",
  "category": "Tech",
  "tags": ["python", "api"]
}
```

---

### 🔹 Listar todos os posts

```
GET /posts
```

---

### 🔹 Buscar post por ID

```
GET /posts/{id}
```

---

### 🔹 Atualizar post

```
PUT /posts/{id}
```

---

### 🔹 Deletar post

```
DELETE /posts/{id}
```

---

### 🔹 Filtrar posts

```
GET /posts?term=tech
```

---

## 📌 Exemplos de resposta

### ✅ Sucesso (201 Created)

```json
{
  "id": 1,
  "title": "Meu post",
  "content": "Conteúdo aqui",
  "category": "Tech",
  "tags": ["python", "api"],
  "createdAt": "2026-01-01T12:00:00",
  "updatedAt": "2026-01-01T12:00:00"
}
```

---

### ❌ Erro (400 Bad Request)

```json
{
  "error": "Dados inválidos"
}
```

---

## 🚀 Melhorias futuras

* Integração com banco de dados (SQLite / PostgreSQL)
* Autenticação de usuários (JWT)
* Paginação de resultados
* Deploy em nuvem (Render, Railway, etc.)

---

## 👨‍💻 Autor

Desenvolvido por **Luis Rodrigues**
https://roadmap.sh/projects/blogging-platform-api

---

## 📄 Licença

Este projeto está sob a licença MIT.

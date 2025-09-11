# 📚 API de Gerenciamento de Livros

Este projeto é uma **API RESTful desenvolvida em Python com Flask**, que gerencia um banco de dados fictício de livros.
A API permite **listar, buscar, adicionar, atualizar (PUT/PATCH) e remover livros**.

---

## 📂 Estrutura do Projeto

```
📁 projeto_api_livros
│-- app.py          # Arquivo principal da API Flask
│-- bd_livros.py    # Banco de dados fictício (lista de livros)
│-- README.md       # Documentação do projeto
```

---

## ⚙️ Tecnologias Utilizadas

* **Python 3.12+**
* **Flask** (microframework para construção da API)

---

## ▶️ Como Executar o Projeto

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/projeto_api_livros.git
   cd projeto_api_livros
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install flask
   ```

4. Execute o servidor Flask:

   ```bash
   python app.py
   ```

5. Acesse no navegador ou no **Postman/Insomnia**:

   ```
   http://127.0.0.1:5000
   ```

---

## 📌 Endpoints da API

### 🔹 Listar todos os livros

```
GET /livros
```

### 🔹 Buscar livro por ID

```
GET /livros/<id>
```

### 🔹 Adicionar novo livro

```
POST /livros
```

📥 Exemplo de JSON enviado:

```json
{
  "id": 6,
  "titulo": "A Menina que Roubava Livros",
  "autor": "Markus Zusak",
  "ano": 2005
}
```

### 🔹 Atualizar livro (substituir todos os dados)

```
PUT /livros/<id>
```

### 🔹 Atualizar parcialmente livro

```
PATCH /livros/<id>
```

📥 Exemplo de JSON enviado:

```json
{
  "ano": 2020
}
```

### 🔹 Remover livro

```
DELETE /livros/<id>
```

---

## 🎯 Objetivo Didático

Este projeto foi criado para fins **educacionais**, auxiliando no aprendizado de:

* Criação de APIs com Flask
* Estruturação de rotas e métodos HTTP
* Manipulação de dados em listas/dicionários
* Integração com ferramentas como **Postman/Insomnia**

---

## 👩‍💻 Autor

Feito por **Alexsandra Campos** ✨
Instrutora de Python & Desenvolvimento de Sistemas.

---

👉 Quer que eu gere os dois **README.md** em arquivos prontos (`.md`) para você já adicionar direto no GitHub?

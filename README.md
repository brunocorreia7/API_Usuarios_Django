📌 API de Usuários — Django + Django REST Framework

Esta API foi desenvolvida com Django e Django REST Framework, permitindo realizar operações CRUD completas (Create, Read, Update e Delete) para gerenciamento de usuários.
O projeto segue boas práticas, utilizando ViewSets, Serializers e rotas organizadas.

🚀 Tecnologias utilizadas

Python 3

Django 5.2.8

Django REST Framework 3.16.1

SQLite (banco padrão do Django)

📂 Estrutura principal do projeto
/API_Usuarios_Django
    ├── api_usuarios/
    │   ├── settings.py
    │   ├── urls.py
    ├── usuarios/
    │   ├── models.py
    │   ├── serializers.py
    │   ├── views.py
    ├── manage.py

🧩 Endpoints da API
Base URL
http://127.0.0.1:8000/api/usuarios/

➕ Criar usuário (POST)
POST /api/usuarios/


Body:

{
  "nome": "Usuario",
  "email": "Usuario@email.com"
}

📄 Listar usuários (GET)
GET /api/usuarios/

🔍 Buscar usuário por ID (GET)
GET /api/usuarios/<id>/

✏️ Atualizar usuário (PUT/PATCH)
PUT /api/usuarios/<id>/
PATCH /api/usuarios/<id>/

❌ Deletar usuário (DELETE)
DELETE /api/usuarios/<id>/

🛠️ Instalação e execução do projeto
1️⃣ Clone o repositório
git clone https://github.com/brunocorreia7/API_Usuarios_Django.git
cd API_Usuarios_Django

2️⃣ Crie um ambiente virtual
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Instale as dependências
pip install -r requirements.txt

4️⃣ Aplique as migrações
python manage.py migrate

5️⃣ Inicie o servidor
python manage.py runserver


Acesse:
👉 http://127.0.0.1:8000/api/usuarios/

🗃️ Banco de Dados
Modelo utilizado:
class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

📜 Arquivos ignorados no .gitignore

Para manter o repositório limpo e seguro, os seguintes arquivos e diretórios foram ignorados:

.env
*.sqlite3
__pycache__/
*.pyc
*.pyo
*.log
staticfiles/
media/
venv/
.env/
.venv/
.vscode/


Isso impede que arquivos sensíveis, ambientes virtuais, cache ou banco local sejam enviados ao GitHub.

💡 Melhorias futuras

Adicionar paginação nativa do DRF

Implementar autenticação (JWT ou TokenAuth)

Documentação automática com Swagger / Redoc

Testes automatizados com Pytest

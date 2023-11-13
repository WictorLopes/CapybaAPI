**CapybaAPI**

Este é um projeto Django que contém funcionalidades de acordo com o que foi pedido no link https://drive.google.com/drive/folders/1SjslUwT6F1GI1erBYdVCvMd0DBSVDUbQ

Instalação
Clone o repositório:

git clone https://github.com/seu-usuario/seu-projeto.git
Instale as dependências:
Certifique-se de ter o Python e o pip instalados. Em seguida, navegue até o diretório do projeto e execute:

pip install -r requirements.txt
Configure o banco de dados:

python manage.py makemigrations
python manage.py migrate
Execute o servidor de desenvolvimento:

python manage.py runserver
O servidor será iniciado em http://127.0.0.1:8000/.



Endpoint de Registro de Usuário:
POST /api/register/
Use este endpoint para registrar um novo usuário.


Endpoint de Login:
POST /api/login/
Faça login para obter um token de autenticação.


Endpoint de Logout:
POST /api/logout/
Realize o logout do usuário.


Endpoint de Lista de Itens Públicos:
GET /api/public-items/
Retorna uma lista de itens públicos. Suporta paginação, pesquisa e filtros.


Endpoint de Lista de Itens Restritos:
GET /api/restricted-items/
Retorna uma lista de itens restritos. Requer e-mail verificado para acessar. Suporta paginação, pesquisa e filtros.


Endpoint de Edição de Perfil de Usuário:
GET /api/edit-profile/
PUT /api/edit-profile/
Use este endpoint para visualizar e atualizar o perfil do usuário.


Endpoint de Envio de Token de Confirmação por E-mail:
POST /api/send-email-confirmation-token/
Envia um token de confirmação para o e-mail do usuário.


Endpoint de Validação do Token de Confirmação por E-mail:
POST /api/validate-email-confirmation-token/
Valida o token de confirmação recebido por e-mail.


Observações
Login para o admin: 
usuário: admin
senha: 123

Contribuição
Contribuições são bem-vindas! 
Sinta-se a vontade para enviar pull requests para melhorias, correções de bugs ou adição de funcionalidades.

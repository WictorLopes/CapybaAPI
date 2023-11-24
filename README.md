Para melhorar a formatação do seu README no Git, você pode seguir algumas práticas para tornar as instruções mais legíveis e organizadas. Aqui está um exemplo de como você pode organizar e formatar as informações do README:

### CapybaAPI

Este é um projeto Django que contém funcionalidades de acordo com o que foi pedido [neste link](https://drive.google.com/drive/folders/1SjslUwT6F1GI1erBYdVCvMd0DBSVDUbQ).

#### Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/seu-projeto.git
    ```

2. Instale as dependências: Certifique-se de ter o Python e o pip instalados. Em seguida, navegue até o diretório do projeto e execute:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure o banco de dados:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Execute o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

O servidor será iniciado em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

#### Endpoints

- **Registro de Usuário**: `POST /api/register/` - Use este endpoint para registrar um novo usuário.
- **Login**: `POST /api/login/` - Faça login para obter um token de autenticação.
- **Logout**: `POST /api/logout/` - Realize o logout do usuário.
- **Lista de Itens Públicos**: `GET /api/public-items/` - Retorna uma lista de itens públicos. Suporta paginação, pesquisa e filtros.
- **Lista de Itens Restritos**: `GET /api/restricted-items/` - Retorna uma lista de itens restritos. Requer e-mail verificado para acessar. Suporta paginação, pesquisa e filtros.
- **Edição de Perfil de Usuário**:
  - `GET /api/edit-profile/`
  - `PUT /api/edit-profile/` - Use este endpoint para visualizar e atualizar o perfil do usuário.
- **Envio de Token de Confirmação por E-mail**: `POST /api/send-email-confirmation-token/` - Envia um token de confirmação para o e-mail do usuário.
- **Validação do Token de Confirmação por E-mail**: `POST /api/validate-email-confirmation-token/` - Valida o token de confirmação recebido por e-mail.

#### Observações

- Login para o admin: 
  - Usuário: `admin`
  - Senha: `123`

#### Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests para melhorias, correções de bugs ou adição de funcionalidades.

Atualize seu arquivo README no Git com essa estrutura organizada e revisada para facilitar a compreensão e uso por parte dos usuários do seu projeto.
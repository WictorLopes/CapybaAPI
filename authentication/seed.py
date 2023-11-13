import requests
API_URL = 'http://127.0.0.1:8000/api/'
# Seed para login
def seed_login(email, password):
    login_url = f'{API_URL}login/'  
    login_data = {'email': email, 'password': password}
    response = requests.post(login_url, data=login_data)
    if response.status_code == 200:
        token = response.json().get('token', '')
        return token
    return None

# Seed para edição de perfil
def seed_edit_profile(token, new_data):
    profile_url = f'{API_URL}edit-profile/' 
    auth_headers = {'Authorization': f'Token {token}'}
    response = requests.put(profile_url, headers=auth_headers, data=new_data)
    if response.status_code == 200:
        return True
    return False

# Seed para listagem de itens
def seed_item_list(token, search='', is_draft=None):
    item_list_url = f'{API_URL}items/'  
    auth_headers = {'Authorization': f'Token {token}'}
    query_params = {'search': search, 'is_draft': is_draft} 
    response = requests.get(item_list_url, headers=auth_headers, params=query_params)
    if response.status_code == 200:
        items = response.json()  
        return items
    return None

# Seed para logout
def seed_logout(token):
    logout_url = f'{API_URL}logout/'  
    auth_headers = {'Authorization': f'Token {token}'}
    response = requests.post(logout_url, headers=auth_headers)
    if response.status_code == 200:
        return True
    return False

user_email = 'example@example.com'  
user_password = 'your_password'  
auth_token = seed_login(user_email, user_password)

if auth_token:
    new_profile_data = {'new_field': 'new_value'}  
    edited = seed_edit_profile(auth_token, new_profile_data)
    if edited:
        items_list = seed_item_list(auth_token, search='termo', is_draft=True)  
        logged_out = seed_logout(auth_token)

# Seed para Registro
def seed_register_user(email, password):
    register_url = f'{API_URL}register_user/'
    data = {'email': email, 'password': password, 'first_name': 'John Doe', 'profile_image': 'example.jpg'}
    response = requests.post(register_url, data=data)
    return response

response = seed_register_user('example@example.com', 'password123')
if response.status_code == 201:
    print("Usuário registrado com sucesso!")
else:
    print("Erro ao registrar o usuário:", response.text)
    
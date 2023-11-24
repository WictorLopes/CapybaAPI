import requests
import os

def upload_file(username, api_token, local_file_path, remote_path):
    with open(local_file_path, 'rb') as file:
        response = requests.post(
            f"https://www.pythonanywhere.com/api/v0/user/{username}/files/path{remote_path}",
            files={'file': file},
            headers={'Authorization': f'Token {api_token}'}
        )
    return response

def main():
    USERNAME = os.environ['USERNAME']
    API_TOKEN = os.environ['PYTHONANYWHERE_API_TOKEN']
    # Define your local directory and remote directory here
    LOCAL_DIR = 'C:\Users\wicto\OneDrive\Documents\CapybaAPI'
    REMOTE_DIR = '/home/wictorlopes/'

    for root, dirs, files in os.walk(LOCAL_DIR):
        for file in files:
            local_file_path = os.path.join(root, file)
            remote_file_path = os.path.join(REMOTE_DIR, file)
            response = upload_file(USERNAME, API_TOKEN, local_file_path, remote_file_path)
            if response.status_code == 200:
                print(f"Uploaded {file} successfully.")
            else:
                print(f"Failed to upload {file}. Status Code: {response.status_code}")

if _name_ == "_main_":
    main()

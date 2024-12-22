from dotenv import load_dotenv
import os 

load_dotenv("../.envs/.env.local")

api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")

# print(f"api key  : {api_key}")
# print(f"secret key : {secret_key}")
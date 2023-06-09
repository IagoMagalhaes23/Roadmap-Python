"""
    obter_dados_api.py
    Autor: Iago Magalhães
    Descrição:
        - Mostrar exemplo de como consumir uma api em Python
"""

import requests
import json

def buscar_dados():
    request = requests.get("http://localhost:3002/api/todo")
    todos = json.loads(request.content)
    print(todos)
    print(todos[0]['titulo'])

if __name__ == '__main__':
    buscar_dados()
import requests

def get_greeting(name):
    response = requests.get(f'http://localhost:5000/say_hello/{name}')

    print(response.text)
nombre = input("What's your name? ")
get_greeting(nombre)
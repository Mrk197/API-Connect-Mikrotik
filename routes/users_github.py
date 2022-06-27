from flask import Blueprint, request
from requests import get
from function_jwt import valida_token
from flask import jsonify

users_github = Blueprint("users_github", __name__)

response = " "

@users_github.before_request  #antes de la petición
def verify_token_middleware():
    token = request.headers['Authorization'].split(" ")[1] #obtiene token
    global response #para indicar que se va a utilizar la vaariable global
    response = valida_token(token, output=False) #valida token
    print(response)


@users_github.route("/github/users", methods=["POST"])
def github():
    global response
    if response == 0: #si no devuelve error
        data = request.get_json()
        country = data['country']
        return get(f'https://api.github.com/search/users?q=location:"{country}"&page=1').json()
    return response  #si el token no es valido


from flask import Blueprint, request
from flask import jsonify
from function_jwt import write_token, valida_token

routes_auth = Blueprint("routes_auth", __name__) #módulo routes_auth


@routes_auth.route("/login", methods=["POST"]) #ruta login, crea token si estas registrado
def login():
    data = request.get_json() #se guarda en variable data el json de la petición
    if data['username'] == "Mirka Alamilla": #si el usuario esta registrado  #SE VA MODIFICAR A ACCESO A BD
        return write_token(data=request.get_json()) #crea token
    else:
        response = jsonify({"message": "User not found"}) #si no se encuentra el usuario
        response.status_code = 404
        return response #regresa respuesta de error


@routes_auth.route("/verify/token") #ruta para validar token
def verify():
    token = request.headers['Authorization'].split(" ")[1] #obtiene campo 'Authotization' de la cabecera y hace un spit para optener la poscición 1 (dónde esta token)
    return valida_token(token, output=True) #retorna salida

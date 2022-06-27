from flask import Blueprint, request
from conexion import searchinfo
from function_jwt import valida_token
from routes.sendPing import send_ping
import subprocess

get_data = Blueprint("get_data", __name__)  # módulo get_data

response = " "


@get_data.before_request
def verify_token():
    token = request.headers['Authorization'].split(" ")[1]
    global response  # para indicar que se va a utilizar la vaariable global
    response = valida_token(token, output=False)  # valida token
    print(response)


@get_data.route("/search", methods=["POST"])
def ingresar():
    global response
    if response == 0:  # si no devuelve error en la conexión
        request_data = request.get_json()
        return searchinfo(request_data['Comando'])
    return response  # si el token no es valido


#PING
@get_data.route("/verify-conexion", methods=["POST"])
def sendping():
    global response
    if response == 0:
        reques_data = request.get_json()
        res = subprocess.run(sendping(reques_data["IP"]))
        return res
    return response


#Obtener tráfico
@get_data.route("/trafic")
def viewtrafic():
    global response
    if response == 0:
        trafict = searchinfo('ip accounting snapshot print terse')
        return trafict
    return response


from flask import Blueprint, request
from function_jwt import valida_token
from conexion2 import conectar

reparar_router = Blueprint("reparar_router", __name__)  # módulo reparar

response = " "


@reparar_router.before_request
def verify_token():
    token = request.headers['Authorization'].split(" ")[1]
    global response  # para indicar que se va a utilizar la vaariable global
    response = valida_token(token, output=False)  # valida token
    print(response)


@reparar_router.route("/validaraddress", methods=["POST"])
def validaraddres():
    request_data = request.get_json()
    respuesta = conectar(request_data['IP'], request_data['user'], request_data['password'], request_data['mode']
                         , "ip firewall address-list print terse")
    print(respuesta)
    list = respuesta.split("\n")
    listL = len(list)
    print(listL)
    respuesta2 = conectar(request_data['IP'], request_data['user'], request_data['password'], request_data['mode'],
                          "ip proxy access print terse")
    list2 = respuesta2.split("\n")
    list2L = len(list2)
    print(list2L)

    if listL == list2L:
        return "Todo OK"
    else:
        if listL > list2L:
            #MOROSOS
            return "Más morosos"
        else:
            #PROXY

            return respuesta2

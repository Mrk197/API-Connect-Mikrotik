from jwt import encode, decode
from jwt import exceptions
from os import getenv
from datetime import datetime, timedelta
from flask import jsonify


def expire_date(days: int) : #funcion para det. días que va a durar el token
    now = datetime.now() #fecha actual
    new_date = now + timedelta(days) #total de días
    return new_date


def write_token(data: dict): #función que recibe datos para encriptación
    token = encode(payload={**data, "exp": expire_date(2)}, key=getenv("SECRET"), algorithm="HS256")
    #payload->info. a encriptar, key->valor para encriptar, algorithm->algoritmo para encriptar
    return token.encode("UTF-8")


def valida_token(token, output=False): #Función para validar token, sin mostrar salida
    try:
        if output:
            return decode(token, key=getenv("SECRET"), algorithms=["HS256"])
    except exceptions.DecodeError:
        response = jsonify(message='Invalid Token')
        response.status_code = 401
        return response
    except exceptions.ExpiredSignatureError:
        response = jsonify(message='Token Expired')
        response.status_code = 401
        return response


from jwt import encode, decode
from jwt import exceptions
from os import getenv
from datetime import datetime, timedelta
from flask import jsonify


def expire_date(days: int): #funcion para det. días que va a durar el token
    now = datetime.now() #fecha actual
    new_date = now + timedelta(days) #total de días
    return new_date


def write_token(data: dict): #función que recibe datos para encriptación
    token = encode(payload={**data, "exp": expire_date(2)}, key=getenv("SECRET"), algorithm="HS256")
    #payload->info. a encriptar, key->valor para encriptar, algorithm->algoritmo para encriptar
    return token.encode("UTF-8")


def valida_token(token, output=False): #Función para validar token, sin mostrar salida
    try: #se van a usar excepciones
        if output: #si salida es true
            return decode(token, key=getenv("SECRET"), algorithms=["HS256"]) #retorna salida decodificada
        decode(token, key=getenv("SECRET"), algorithms=["HS256"]) #no retorna salida
        return 0
    except exceptions.DecodeError: #excepción si pasa un valor no valido
        response = jsonify(message='Invalid Token', status=401) #retona json  #otra sintaxis: jsonify({"message":"Invalid Token"})
        response.status_code = 401
        return response
    except exceptions.ExpiredSignatureError: #excepción cuando token a expirado
        response = jsonify(message='Token Expired', status=401)
        response.status_code = 401
        return response


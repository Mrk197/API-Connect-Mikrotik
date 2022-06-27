from flask import Blueprint, request
from conexion import setconfig, searchinfo
from function_jwt import valida_token


set_config = Blueprint("set_config", __name__)  # módulo get_data

response = " "


@set_config.before_request
def verify_token():
    token = request.headers['Authorization'].split(" ")[1]
    global response  # para indicar que se va a utilizar la vaariable global
    response = valida_token(token, output=False)  # valida token
    print(response)


@set_config.route("/config", methods=["POST"])
def ingresar():
    global response
    if response == 0:  # si no devuelve error
        request_data = request.get_json()
        return setconfig(request_data['Comando'])
    return response  # si el token no es valido


# Agregar PPP
@set_config.route("/config/setPPP", methods=["POST"])
def setppp():
    global response
    if response == 0:
        request_data = request.get_json()
        return setconfig('ppp secret add comment=\"'
                         + request_data['Comment'] +
                         '\" name=' + request_data['Name'] + ' password=' + request_data['Password']
                         + ' remote-address=' + request_data['Remote IP']
                         + ' service=' + request_data['Service'])
    return response


# Agregar QUEUE
@set_config.route("/config/setQUEUE", methods=["POST"])
def setqueue():
    global response
    if response == 0:
        request_data = request.get_json()
        return setconfig('queue simple add comment=\"'
                         + request_data['comment'] +
                         '\" limit-at=' + request_data['limit-at'] + ' max-limit='
                         + request_data['max-limit']
                         + ' name=' + request_data['name']
                         + ' target=' + request_data['target']
                         + '  priority=' + request_data['priority'])  # madar vacio para dejar default
    return response


# Agregar IP
@set_config.route("/config/addIP", methods=["POST"])
def addip():
    global response
    if response == 0:
        request_data = request.get_json()
        return setconfig('ip address add address=' + request_data['address']
                         + ' interface=' + request_data['ether']
                         + ' network=' + request_data['network'])
    return response


#Modificar Plan
@set_config.route("/config/setLimit", methods=["GET"])
def setlimit():
    global response
    if response == 0:
        request_data = request.get_json()
        return setconfig('queue simple set ' + request_data['name-queue'] +
                         ' max-limit=' + request_data['max-limit'] +
                         ' limit-at=' + request_data['limit-at'])
    return response


#Agregar regla de morosos/aviso
@set_config.route("/config/addmorosos", methods=["PUT"])
def addmorosos():
    global response
    if response == 0:
        request_data = request.get_json()
        return setconfig("ip firewall address-list add" +
                         " address=" + request_data['address'] +
                         " comment=" + request_data['comment'] +

                         " list=" + request_data['list'])
    return response


#Quitar regla de morosos/aviso
@set_config.route("/config/deletemorosos", methods=["DELETE"])
def deletemorosos():
    global response
    if response == 0:
        request_data = request.get_json()
        return setconfig("/ip firewall address-list remove [/ip firewall address-list find address="
                         + request_data['IP'] + "]")
    return response


#Agregar regla de proxy
@set_config.route("/config/addproxy", methods=["PUT"])
def addmproxy():
    global response
    if response == 0:
        request_data = request.get_json()
        return setconfig("ip proxy access add" +
                         " action=" + request_data['action'] +
                         " comment=" + request_data['comment'] +
                         " src-address=" + request_data['src-address'] +
                         " dst-host=" + request_data['dst-host'])
    return response

#Borrar regla de proxy
@set_config.route("/config/deleteproxy", methods=["DELETE"])
def deleteproxy():
    global response
    if response == 0:
        request_data = request.get_json()
        return setconfig("/ip proxy access remove [/ip proxy access find src-address=\"" + request_data['IP']
                         + "\"]")
    return response

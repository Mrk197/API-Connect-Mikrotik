from flask import Blueprint, request
from conexion import conectar

get_data = Blueprint("gat_data", __name__)


@get_data.route("/ingresar", methods=["POST"])
def ingresar():

    request_data = request.get_json()
    return conectar(request_data['Accion'], request_data['Comando'])

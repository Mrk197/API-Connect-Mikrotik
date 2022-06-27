import time
from flask import Blueprint, request
from function_jwt import valida_token
import ping3
import os
import platform


send_ping = Blueprint("send_ping", __name__)  # módulo send_ping

response = " "
rping = " "

@send_ping.before_request
def verify_token():
    token = request.headers['Authorization'].split(" ")[1]
    global response  # para indicar que se va a utilizar la vaariable global
    response = valida_token(token, output=False)  # valida token
    print(response)


@send_ping.route("/ping", methods=["POST"])
def ping():
    global response
    global rping
    if response == 0:
        request_data = request.get_json()
        host = request_data["ip"]
        ping3.EXCEPTIONS = True
        try:
            print(ping3.ping(host))
        except ping3.errors.HostUnknown:
            print("Host unknown error")
            return "Host unknown error"
        except ping3.errors.DestinationHostUnreachable:
            print("Destination Host Unreachable")
            rping = "Destination Host Unreachable"
            return "Destination Host Unreachable"
        except ping3.errors.TimeExceeded:
            print("Time Exceeded")
            rping = "Time Exceeded"
            return "Time Exceeded"
        except ping3.errors.PingError:
            print("A ping error raised.")
            rping = "A ping error raised."
            return "A ping error raised."
        else:
            return "True"
        #print(senping(host))
    else:
        return response


#def senping(host):


#print(sendping("192.168.3.170"))

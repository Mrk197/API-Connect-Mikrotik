from netmiko import ConnectHandler
from flask import jsonify
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException


def conectar(hostip, user, password, mode, comando):

    MT1 = {  # datos para conexión a MK
        'device_type': 'mikrotik_routeros',
        'host': hostip,
        'username': user,
        'password': password,
    }

    if mode == "1":
        try:
            net_connect = ConnectHandler(**MT1)
            print("CONEXIÓN EXITOSA")
            # Para hacer comandos de consulta
            output = net_connect.send_command(comando, delay_factor=5)
            return output
        except NetMikoTimeoutException:
            return "Handled timeout exception"
        except AuthenticationException:
            return "AuthenticationException"
        except SSHException:
            return "SSHException"
    elif mode == "2":
        net_connect = ConnectHandler(**MT1)
        print("CONEXIÓN EXITOSA")
        # Para hacer comandos de configuración
        net_connect.enable()
        output = net_connect.send_config_set(comando)
        salida = output.split("\n")  # Se divide respuesta obtenido desde MK
        net_connect.save_config()
        net_connect.exit_enable_mode()
        if salida[2]:  # Si devuelve alguna respuesta de error
            return jsonify(error=salida[2])  # retorna error
        return jsonify(message='PETICION EXITOSA')  # Si no, retorna restorna respusta
    else:
        return "CONEXIÓN EXITOSA"





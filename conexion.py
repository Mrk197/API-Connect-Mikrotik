from netmiko import ConnectHandler
from decouple import config

MT1 = {
    'device_type': 'mikrotik_routeros',
    'host':   config('HOSTIP'),
    'username': config('USER'),
    'password': config('PASSWORD'),
}


def conectar(accion, comando):
    net_connect = ConnectHandler(**MT1)
    print("CONEXIÓN EXITOSA")
    if accion == "0":
        output = net_connect.send_command(comando)
        return output
    else:
        net_connect.enable()
        #commands = ['']
        output = net_connect.send_config_set(comando)
        print(output)
        net_connect.save_config()
        net_connect.exit_enable_mode()
        return output


#res = conectar(0, 'export')
#print(res)

from pythonping import ping
import os


response = ping('192.168.3.170', verbose=False, count=5)  #verbose=False -> no muestra resultado

print(response)


def ping(host):
        parameter = '-n' if platform.system().lower() == 'windows' else '-c'
        rping = os.system("ping " + parameter + " 3 " + host)
        print(rping)
        if rping == 0:
            return "True"
        else:
            return "False"
        #print(senping(host))

import ping3

ping3.EXCEPTIONS = True

try:
    print(ping3.ping('192.168.3.173'))
except ping3.errors.HostUnknown:
    print("Host unknown error")
except ping3.errors.DestinationHostUnreachable:
    print("Destination Host Unreachable")
except ping3.errors.TimeExceeded:
    print("Time Exceeded")
except ping3.errors.PingError:
    print("A ping error raised.")
else:
    print("Se tiene conexion")



import socket

def establish_connection(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Conexión establecida con el servidor.")

    while True:
        # Aquí puedes agregar la lógica para recibir y procesar los comandos del servidor

        command = client_socket.recv(1024).decode()
        if not command:
            break

        print("Comando recibido:", command)

    client_socket.close()

# Mensaje personalizado
print("╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╮╱╭┳━━━╮")
print("┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╰╮┃┃╭━╮┃")
print("┃╰━━┳╮╭┳━━┳━┳━━┳╮╭┳━━┫╭╮╰╯┃╰━╯┃")
print("╰━━╮┃┃┃┃╭╮┃╭┫┃━┫╰╯┃╭╮┃┃╰╮┃┣━━╮┃")
print("┃╰━╯┃╰╯┃╰╯┃┃┃┃━┫┃┃┃╰╯┃┃╱┃┃┣━━╯┃")
print("╰━━━┻━━┫╭━┻╯╰━━┻┻┻┻━━┻╯╱╰━┻━━━╯")
print("╱╱╱╱╱╱╱┃┃")
print("╱╱╱╱╱╱╱╰╯")
print("SupremoN9 - Bienvenido a Destroyer v2.4")
print("Created BY N9")
print("Sígueme en Instagram: supremon9\n")

host = input("Ingresa la dirección IP del servidor: ")
port = int(input("Ingresa el puerto del servidor: "))

establish_connection(host, port)

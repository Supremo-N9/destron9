import socket
import os
from PIL import Image
from pydub import AudioSegment
import PyPDF2

# Función para imprimir en color
def print_color(message, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
    }
    end_color = '\033[0m'
    print(colors[color] + message + end_color)

def send_file(host, port, file_path):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    file_name = file_path.split("/")[-1]
    client_socket.send(file_name.encode())

    file_extension = os.path.splitext(file_path)[1]

    if file_extension.lower() == ".jpg" or file_extension.lower() == ".png":
        # Transferir imágenes
        image = Image.open(file_path)
        image.save(client_socket, "JPEG" if file_extension.lower() == ".jpg" else "PNG")
    elif file_extension.lower() == ".mp3" or file_extension.lower() == ".wav":
        # Transferir archivos de música
        audio = AudioSegment.from_file(file_path, format=file_extension[1:])
        audio.export(client_socket, format=file_extension[1:])
    elif file_extension.lower() == ".pdf":
        # Transferir archivos PDF
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                client_socket.sendall(page.extract_text().encode())

    print_color("Transferencia de archivo completada.", "green")

    client_socket.close()

# Mensaje personalizado
print_color("╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╮╱╭┳━━━╮", "cyan")
print_color("┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╰╮┃┃╭━╮┃", "cyan")
print_color("┃╰━━┳╮╭┳━━┳━┳━━┳╮╭┳━━┫╭╮╰╯┃╰━╯┃", "cyan")
print_color("╰━━╮┃┃┃┃╭╮┃╭┫┃━┫╰╯┃╭╮┃┃╰╮┃┣━━╮┃", "cyan")
print_color("┃╰━╯┃╰╯┃╰╯┃┃┃┃━┫┃┃┃╰╯┃┃╱┃┃┣━━╯┃", "cyan")
print_color("╰━━━┻━━┫╭━┻╯╰━━┻┻┻┻━━┻╯╱╰━┻━━━╯", "cyan")
print_color("╱╱╱╱╱╱╱┃┃", "cyan")
print_color("╱╱╱╱╱╱╱╰╯", "cyan")
print_color("SupremoN9 - Bienvenido a Destroyer v2.4", "yellow")
print_color("Created BY N9", "yellow")
print_color("Sígueme en Instagram: supremon9\n", "yellow")

host = input("ip/host: ")
port = int(input("port: "))
file_path = input("Ingrese la ruta del archivo a enviar: ")

send_file(host, port, file_path)

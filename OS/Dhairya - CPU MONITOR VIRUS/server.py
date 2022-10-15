import socket
import tqdm
import os


ServerHost = "0.0.0.0"
ServerPort = 8000
BufferSize = 4096
separator = "<SEPARATOR>"


s = socket.socket()
s.bind((ServerHost,ServerPort))
s.listen(10)
print(f"[*] Listening as {ServerHost}:{ServerPort}")
client_socket, address = s.accept()
print(f"[+]{address} is connected")
received = client_socket.recv(BufferSize).decode()
filename, filesize = received.split(separator)
filename = os.path.basename(filename)
filesize = int(filesize)
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "wb") as f:
    while True:
        bytes_read = client_socket.recv(BufferSize)
        if not bytes_read:

            break

        f.write(bytes_read)
        progress.update(len(bytes_read))


client_socket.close()
s.close()

f = open("File.txt", "r")
print(f)
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(), end='')
# mysock.close()

received_data = b""
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    received_data += data
    if b"\r\n\r\n" in received_data:  # Check if the end of the header is reached
        header, _, _ = received_data.partition(b"\r\n\r\n")  # Partition the data into header and body
        print(header.decode())
        break  # Exit the loop after printing the header

mysock.close()
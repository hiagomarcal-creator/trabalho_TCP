from socket import *

serverName = '127.0.0.1'
serverPort = 1217
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Digite uma frase em minúsculas: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('Do servidor:', modifiedSentence.decode())
clientSocket.close()
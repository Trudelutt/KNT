__author__ = 'trude'
from socket import *

# Message to send
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Our mail server is smtp.stud.ntnu.no
mailserver = 'smtp.stud.ntnu.no'

# Create socket called clientSocket and establish a TCP connection
# (use the appropriate port) with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))
#Fill in end

recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
	print '220 reply not received from server.'

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'

# Send MAIL FROM command and print server response.
# Fill in start
mailCommand=  'MAIL FROM: <trudejos@stud.ntnu.no>\r\n'
clientSocket.send(mailCommand)
recv2 = clientSocket.recv(1024)
print(recv2)
if recv2[:3] != '250':
	print '250 reply not received from server'

# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
RCPT = 'RCPT TO: <trude.jostad@gmail.com>\r\n'
print(RCPT)
clientSocket.send(RCPT)
recv3 = clientSocket.recv(1024)
print(recv3)
if recv3[:3] != '250':
	print '250 reply not received from server'
# Fill in end

# Send DATA command and print server response.
# Fill in start
DATA = 'DATA\r\n'
clientSocket.send(DATA)
recv4 = clientSocket.recv(1024)
if recv4[:3] != '354':
	print '250 reply not received from server'
# Fill in end

# Send message data.
clientSocket.send(msg)
# Fill in start



# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send('\r\n.\r\n')
recv6 = clientSocket.recv(1024)
print(recv)
if recv6[:3] != '250':
	print '250 reply not received from server'
# Fill in end

# Send QUIT command and get server response.
# Fill in start
clientSocket.send('QUIT\r\n')
recv7 = clientSocket.recv(1024)
print(recv7)
if recv7[:3] != '221':
	print '250 reply not received from server'
clientSocket.close()
# Fill in end
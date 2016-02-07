__author__ = 'trude'
import time
from socket import *

# Get the server hostname and port as command line arguments
host = '' # FILL IN START		# FILL IN END
port = 12000 # FILL IN START		# FILL IN END
timeout = 1 # in seconds
RTT= []

# Create UDP client socket
# FILL IN START
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Note the second parameter is NOT SOCK_STREAM
# but the corresponding to UDP

# Set socket timeout as 1 second
clientSocket.settimeout(1)

# FILL IN END

# Sequence number of the ping message
ptime = 0
packetloss = 0
# Ping for 10 times
while ptime < 10:
	ptime += 1
	# Format the message to be sent as in the Lab description
	data =  "Ping" + str(ptime)+ " " + str(time.asctime())# FILL IN START		# FILL IN END

	try:
		# FILL IN START

		# Record the "sent time"
		send = time.time()
		# Send the UDP packet with the ping message
		clientSocket.sendto(data, (host, port))
		# Receive the server response
		modifiedData, serverAddress = clientSocket.recvfrom(1024)
		# Record the "received time"
		# Display the server response as an output
		print(modifiedData)
		# Round trip time is the difference between sent and received time
		receive = time.time()
		print(str(receive - send) +" "+ "sec")
		RTT.append(receive-send)

		# FILL IN END
	except:
	# Server does not response
	# Assume the packet is lost
		packetloss+=1
		print "Request timed out."
		continue

# Close the client socket
clientSocket.close()
print("min RTT" + str(min(RTT)))
print("max RTT" + str(max(RTT)))
print("Average"+ str(sum(RTT)/len(RTT)))
print("packetloss rate" + " " + str(packetloss * 100/ 10))


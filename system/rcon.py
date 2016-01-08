#Based on a modified version of SourceRcon
#https://github.com/frostschutz/SourceLib
import select, socket, struct

class RconSteam:

    def connect(host, portnumber, password):
        sockrcon = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sockrcon.connect((host, portnumber))
        sockrcon.send(sock.send("0xFF0xFF0xFF0xFFrcon 5SweeT23")


    connect(('142.4.210.104', '3222', '5SweeT23'))

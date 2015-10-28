"""DashServ v0.1.0 (alpha-unstable)
Usage:
    dashserv.py init <server_file_name>
    dashserv.py authorize PROVIDER
    dashserv.py start <hostname>
    dashserv.py stop <hostname>
    dashserv.py destroy <hostname>
    dashserv.py snapshot <hostname>
    dashserv.py ssh <hostname>

Arguments:
    HOSTNAME    Hostname of initialized server.
    PROVIDER    digitalocean
    
Options:
    --version   Display current version of DashServ
    --help  Display this help message.
    
Examples:
    dashserv server init example_droplet.yaml
    
"""

from docopt import docopt
from providers.digitalocean import *

if __name__ == '__main__':
    arguments = docopt(__doc__, version='DashServ 0.1.0')
    print(arguments) #Debug line - prints docopt arguments

#Init will parse the server script and change values to the best available vals
if arguments['init'] == True:
    print ("INFO: Initializing Server...")




#Verify authorization, if not authed, will ask servers to provide auth key
if arguments['authorize'] == True:

    #Check if authenticated with digitalocean


    auth_status_code = Auth.is_authenticated()
    #auth_status_code = 404
    
    if (auth_status_code == True):
        print("Successfully authenticated with" + arguments['PROVIDER'])
    else:
        print ("Error: Not authenticated! Need digitalocean api key!")
        api_key = input("DigitalOcean API key: ")
        Auth.setAuthToken(api_key)

    
    
    
    
        
        
        
        
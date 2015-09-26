"""DashServ (Alpha Testing)
Usage:
    dashserv.py init FILE
    dashserv.py authorize PROVIDER
    dashserv.py start HOSTNAME
    dashserv.py stop HOSTNAME
    dashserv.py destroy HOSTNAME
    dashserv.py snapshot HOSTNAME
    dashserv.py ssh HOSTNAME

Arguments:
    FILE    Server config file formatted in yaml
    HOSTNAME    Hostname of initialized server.
    PROVIDER    digitalocean
    
Options:
    --version   Display current version of DashServ
    --help  Display this help message.
    
Examples:
    dashserv server init example_droplet.yaml
    
"""

from docopt import docopt
from lib.base import Auth

if __name__ == '__main__':
    arguments = docopt(__doc__, version='DashServ 0.1.0')
    print(arguments) #Debug line - prints docopt arguments

#Init will parse the server script and change values to the best available vals
if arguments['init'] == True:
    with open(arguments['FILE'], 'r') as stream:
        print (yaml.load(stream))

#Verify authorization, if not authed, will ask user to provide auth key
if arguments['authorize'] == True:
    auth_status_code = Auth.is_authenticated()
    #auth_status_code = 404
    
    if (auth_status_code == 200):
        print("Successfully authenticated with digitalocean!")
    else:
        print ("Error: Not authenticated! Need digitalocean api key!")
        api_key = input("DigitalOcean API key: ")
        Auth.setAuthToken(api_key)
        
        
        
        
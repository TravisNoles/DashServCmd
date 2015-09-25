"""DashServ (Alpha Testing)
Usage:
    dashserv.py init FILE
    dashserv.py authorize PROVIDER
    dashserv.py start <hostname>
    dashserv.py stop <hostname>
    dashserv.py destroy <hostname>
    dashserv.py snapshot <hostname>
    dashserv.py ssh <hostname>

Arguments:
    FILE    Server config file formatted in yaml
    
    
Options:
    --version   Display current version of DashServ
    --help  Display this help message.
    
Examples:
    dashserv server init example_droplet.yaml
    
"""

from docopt import docopt
import yaml
import providers.digitalocean

if __name__ == '__main__':
    arguments = docopt(__doc__, version='DashServ 0.1.0')
    print(arguments)

if arguments['init'] == True:
    with open(arguments['FILE'], 'r') as stream:
        print (yaml.load(stream))
    
if arguments['authorize'] == True and arguments['digitalocean'] == True:
    
    print ('Not implemented')
    #Read auth file.
    
    
    
    
    
    
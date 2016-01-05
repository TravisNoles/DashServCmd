"""DashServCMD v0.1.0-alpha
Usage:
    dashserv.py web-gui start
    dashserv.py <app_name config
    dashserv.py <app_name> start
    dashserv.py <app_name> stop
    dashserv.py <app_name> remove

Arguments:


Options:
    --version   Display current version of DashServ
    --help  Display this help message.

Examples:


"""

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='dashservcmd 0.1.0')
    print(arguments) #Debug line - prints docopt arguments

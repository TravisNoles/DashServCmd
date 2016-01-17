"""DashServCMD v0.1.0-alpha
Usage: dashservcmd <command> [options]

Commands:

    install <app_name>
    list <app_name>
    configure <app_name
    uninstall <app_name>
    start <app_name>
    stop <app_name>


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

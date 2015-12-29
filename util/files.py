import glob, os, yaml
from os.path import expanduser #Get servers dir


class Files(object):
    "Handles files and management of files."
    
    #Set authfile path to the home directory.
    authfile = expanduser('~') + '/' + 'base.yaml'

    def get_server_init_file():
        "Get server init file."

        init_file = glob.glob('.yaml')

        return init_file
    
    def read_yaml_file(filename):
        "Open file and return content of file."
        
        with open(filename, 'r') as stream:
            file_content = yaml.safe_load(stream)
    
        return file_content
        
    
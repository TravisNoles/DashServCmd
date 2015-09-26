import requests, yaml, json
from os.path import expanduser #Get user dir

class Auth:
    def __init__(self, apikey):
        return
    
    #Return api key stored in auth file (root home dir)
    def _getAuthToken():
        #Read auth file.
        _authpath = expanduser('~') + '/' + '.dashserv_auth.yaml'
    
        #Open file with read-access('r')
        with open(_authpath, 'r') as stream:
            _authfile = yaml.safe_load(stream)
        
        _authtoken = _authfile['apikeys']['digitalocean']
        
        
        return _authtoken
        
    #Check if auth token is valid
    #TODO: Return true or false, not status code.
    def is_authenticated():
        auth_token = "Bearer " + Auth._getAuthToken()
        
        headers = {'Content-Type': 'application/json', 'Authorization': auth_token}
        data = requests.get("https://api.digitalocean.com/v2/account", headers=headers)
        status_code = data.status_code
        return status_code

    def setAuthToken(apikey):
        auth_token = apikey
        authpath = expanduser('~') + '/' + '.dashserv_auth.yaml'
        authdata = {'apikeys': {'digitalocean': auth_token}}
        
        #Open auth file with write access.
        with open(authpath, 'w') as stream:
            yaml.dump(authdata, stream, default_flow_style=False)

            
            
            
class Server:
    
    def __init__(self, hostname):
        return;


class Droplet():

    def __init__(self, name):
        return
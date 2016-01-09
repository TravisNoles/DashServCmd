import requests, yaml, json
import util.files

class Auth:
    def __init__(self, apikey):
        return

    def setAuthToken(apikey):
        """Prompt user for api key."""

        #TODO: Get/set path.
        #TODO: Parse config file for api key.
        #TODO: Open file (as stream)



        authpath = expanduser('~') + '/' + 'base.yaml'
        authdata = {'apikeys': {'digitalocean': auth_token}}

        #Open auth file with write access.
        with open(authpath, 'w') as stream:
            yaml.dump(authdata, stream, default_flow_style=False)


        #TODO: Catch exceptions / data validations
        #TODO: Return if successful or not


        return


    #Return api key stored in auth file (root home dir)
    def getAuthToken():
        """Return authentication token."""

        #Read auth file.
        _authpath = expanduser('~') + '/' + 'base.yaml'

        read_yaml_file(Files.authfile)


        #Open file with read-access('r')
        with open(_authpath, 'r') as stream:
            _authfile = yaml.safe_load(stream)

        _authtoken = _authfile['apikeys']['digitalocean']


        return _authtoken

    #Check if auth token is valid
    def is_authenticated():
        auth_token = "Bearer " + Auth._getAuthToken()

        headers = {'Content-Type': 'application/json', 'Authorization': auth_token}
        data = requests.get("https://api.digitalocean.com/v2/account", headers=headers)
        status_code = data.status_code

        if status_code == 200:
            authenticated = True
        else:
            authenticated = False

        return authenticated


class BaseAPI():


    self.api_regions = region #Stores all of the regions
    self.baseurl = 'https://api.digitalocean.com/v2/'


    #Initialization of baseapi.
    def init(self):
        "Initiates BaseAPI class."

        r = requests.get()
        self.region = region




    def getRegions():
        "Returns a list of regions."

        return regions



    def postData(self, url):



    def getData(self, url):





    def getHeaders(self, url):
        #Get auth token.
        auth_token = Auth.getAuthToken()
        headers = {'Content-Type': 'application/json', 'Authorization': auth_token}
        return headers







class Droplet(BaseAPI):
    "Creates and maintains digitalocean droplet servers."

    available_apps = ['tshock']


    def __init__(self, name, region, size, image, ssh_keys, backups, ipv6, private_networking, user_data):
        #User Provided Values
        self.name = name
        self.region = region
        self.size = size
        self.image = image
        self.ssh_keys = ssh_keys
        self.backups = backups


        #Default droplet values.
        self.disk = '20gb'
        self.memory = '512mb'
        self.vcpus = 1


        self.ipv6 = ipv6
        self.private_networking = private_networking
        self.user_data = user_data



    #Create a new droplet
    def new(self, name, region, size, image, ssh_keys, backups, ipv6, private_networking, user_data)
        "Creates a new droplet."
        return droplet



    #Get functions of droplet class.
    def get_name(self):
        return self.name

    def get_disk(self):
        return self.disk

    def get_memory(self):
        return self.memory




    #Append SSH key
    def add_sshkey(self, ssh_key):
        self.ssh_keys.append(ssh_key)
        return

    #Set Droplet Name
    def set_name(self, name):
        self.name = name
        return

    def set_region(self, region):
        self.region = region
        return

    def set_image(self, image):
        self.image = image
        return

    def set_backups(self, backups=False):
        self.backups = backups
        return

    def set_ipv6(self, ipv6=False):
        self.ipv6 = ipv6
        return

    def set_privatenetwork(self, value=False):
        self.private_networking = value
        return

    def set_userdata(self, user_data=""):
        self.user_data = user_data
        return

    def get_droplet(self):
        "Get all values of a droplet."
        droplet = []

        # Get servers provided values.
        droplet.append(self.name)
        droplet.append(self.region)
        droplet.append(self.size)
        droplet.append(self.image)
        droplet.append(self.ssh_keys)
        droplet.append(self.backups)
        droplet.append(self.ipv6)
        droplet.append(self.private_networking)
        droplet.append(self.user_data)

        #Get Digitalocean values.



        return droplet




    # Create Droplet, creates the droplet and relays data to api, creating the droplet.
    def create(self):
        headers = getHeaders()
        droplet_properties = {'name': name, "region": region, "size": size, "image": image, "ssh_keys": ssh_keys, "backups": backups, "ipv6": ipv6, "user_data": user_data, 'private_networking': private_networking}
        req = requests.post('https://api.digitalocean.com/v2/droplets', json=droplet_properties, headers=headers)



        if req.status_code == 200:
            creation_successful = True
        else:
            creation_successful = False


        return creation_successful

    #Read and parse the init file
    def parse_server_file(self):

        init_file = glob.glob('*.yaml')


    return init_file

#Manages all applications.
import json
import yaml
import docker

class applications:
    """Manages applications, starts/stops/pauses apps,
    returns results in json format. """

    def __init__(self, name, description, files):
        self.name = name
        self.description = description
        self.files = files

    #Define getter/setters here.




    #Install the application, based on __init_parameters (declare new instance.)
    def install(self):
        """ Attempts to run the application with provided docker file,
        sets/gets settings from configuration file, runs commands inside
        container, prepares application container for first use. Runs app's
        setup.py file inside the docker folder, runs the app for the first time
        while setting any required settings that is provided in the config
        file. If there is any errors while running this command it will display
        to the user depending on the error.

        Arguments: name - App name
        """

        #Read (parse) application config file.
        with open('name', 'r') as f:
            app_config = yaml.load(f)


        # Load Settings
        app_config['']

        # Run Dockerfile

            return result



    def check_update(self, name):
        """Checks for application updates."""

        # Read app url from package file.


        return self.result





    def start(app_name):
        """Starts the application. Application must be already setup(installed.)
        """

        #Check to see if the app has been setup, if so continue to run.



        return result

    def stop(self, app_name):
        """Stops the app safely via Docker."""


        return result

    def uninstall(self, name):
        """Removes an application."""

        return result

    def sendcmd(self, name):


        return result



applications.install("test", "test2")

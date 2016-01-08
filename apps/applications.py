#Manages all applications.
import json

class application:
    """Manages applications, starts/stops/pauses apps,
    returns results in json format. """

    def __init__(self, name):
        self.name = name
        self.running = False
        self.enabled = False
        self.result =
        {
            "result_code": 0
            "message": "Unknown Error",
            "details": "default_error",
        }


    def update(self, name):
        """Updates application."""



        return results

    def install(self, name):
        """ Attempts to run the application with provided docker file,
        sets/gets settings from configuration file, runs commands inside
        container, prepares application container for first use. Runs app's
        setup.py file inside the docker folder, runs the app for the first time
        while setting any required settings that is provided in the config
        file. If there is any errors while running this command it will display
        to the user depending on the error.

        Arguments: name = app_name
        """


        #Read (parse) application config file.


        # Set settings and run docker file.


        return result



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

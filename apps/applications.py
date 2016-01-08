#Manages all applications.
import json

class applications():
    """Manages applications, starts/stops/pauses apps,
    returns results in json format. """

    def listall():
        """Returns in json format all currently installed applications that are in the /apps subprocess
        directory. """


    def install(app_name):
        """Attempts to install and setup an application. Returns results in json. """

        result =
        {
            "message": "Unknown Error",
            "details": "default_error"
        }

        #Read application config file.

        



        return result



    def start(app_name):
        """Start the app."""

        result =
        {

        }

        return result

    def stop(app_name)



        return result

    def uninstall(app_name):
        """Removes an application."""
        result = 0



        return result

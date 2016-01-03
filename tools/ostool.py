#Is a tool that can detect what OS the user is running, what linux distro, etc.
import platform




class osTool():

    def detect_os():
        """Detect what the application is running on, and return OS w/ distro"""
        runningOS = platform.system() #Returns OS (looking for "Linux")

        if platform.system == "Linux":
            print ("hai")

        print (platform.linux_distribution()




    def detectRAM():
        """Detect the amount of RAM that is being used and max available."""
        return memory



    detect_os()

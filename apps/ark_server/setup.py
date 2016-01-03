import os

#ark_server setup file.
#Required dashservcmd apps: steamcmd
#Required OS: Debian 8 (only for now.)
#Required system apps: lib32gcc1
#Hardware Requirements (2 Players): >4GB RAM, 64bit processor,



#Check requirements.
    def check_requirements():
        




#Install and Setup ArkServer
    def download():



#Set file limits (linux)
    #Add fs.file-max=100000 to: /etc/sysctl.conf && apply change: sysctl -p /etc/sysctl.conf

    #Add following lines to: /etc/security/limits.conf
    # *               soft    nofile          1000000
    # *               hard    nofile          1000000

    # Add: session required pam_limits.so TO /etc/pam.d/common-session


    #Run steamcmd: ./steamcmd.sh +login anonymous +force_install_dir <install_dir> +app_update "376030 validate" +quit
    # Force install directory to ark_server/files



    #Reboot to apply all changes correctly.

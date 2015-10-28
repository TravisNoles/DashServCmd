# DashServCmd

DashServCmd v0.1.0-dev
----------------------

DashServ is an all in one console application that aims to be easy to use with
a beautiful syntax along with being pythonic in usage. The purpose of dashserv
is to solve the complexities of managing your server. Instead of going to
multiple cloud management web applications on their respective websites,
why not handle all of the daily maintence of your cloud servers with one
application right where you do all your daily work anyways. Inside your console.

Disclaimer: Unstable development version, not for production use. Always make
backups. Use at your own risk.

Upcoming Features
--------

* Terraria Server Management
* Ark Server Management
* Minecraft Server Management
* DigitalOcean System Management


Installation
------------

Note: App will have a setup.py file later on in development.

1) Copy .dashserv_auth.yaml to the root of your home directory.
2) Copy the root of dashserv into the root of your home directory.


Usage
-------

1) Create a server file anywhere, home directory recommended with the extension,
.yaml. Name the file with what you wish to call your server so the file can
be easily identifiable.
2) Initialize your server: dashserv.py init example_droplet.yaml
3) Example server file with values will be provided in the /doc folder.
4) Now you can manage your server that you just created via the command line.


If you have any questions regarding usage, please see the wiki or you can
optionally contact me. Please submit any bug reports via github.


ChangeLog
----------

v0.1.0-dev

* DigitalOcean droplet support -- Can create, delete, shutdown, and backup servers.
* Initialize digitalocean droplet from a yaml file
* 



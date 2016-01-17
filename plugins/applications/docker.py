import json, requests

class docker:
    """Interacts with docker containers, connects dashapps to docker."""

    def __init__(self):
        self.dockerfile
        self.arguments

    def build(self, path):
        return results


    def rename_container(self container_name):
        return results

    def rm_img():
        return results

    def login(self, username, password, email, registry_url="", reauth=False):
        docker.login()

        return results

    def attach(self, name):
        return results

    def list_containers(self):
        """Similar to docker ps command."""


        return results


    def list_images(self):

        return results

    def create_network(self):

        return results

    def execute(self, command):

        return results

    def restart(self, container_name):
        return results


    def start(self, container_name):
        return results

    def stop(self, container_name):
        return results


    def top(self, container_name):
        return results



    def list_volumes(self, container_name):
        return results

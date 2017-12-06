import json
from pprint import pprint
import os
import json
import socket
import subprocess
import requests
import sys




class ClientAPI:


    def __init__(self, url):
        self.url = url


    def Change_Directory (self, path_to_directory):

        """this method read the data from json flie.

                Args:
                    path_to_directory = path to directory

                """

        self.directory_working= path_to_directory
        os.chdir(self.directory_working)
        print os.getcwd()




    def Read_Json(self,name_of_json):

        """this method read the data from json flie.

        Args:
            name_of_json = name of json file


        """


        with open(name_of_json) as data_file_json:
            data = json.load(data_file_json)
        pprint(data)




    def Verify_Connection_To_Json_Server(self, command):

        self.command=command
        self.process=subprocess.Popen(self.command, universal_newlines=True, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        self.data_cmd=self.process.stdout.read()
        self.retcode=self.process.wait()
        print self.data_cmd
        #add verify methos to the confirm the return data







    def Edit_Data_Client(self, header, data_to_send, url_header):

        """this method edit data Client.

        Args:
            name = name of client
            id_document = id document of client
            address = address of client
             user = user of client
             password = password of client



        """

        self.req=requests.patch(url=url_header, params=json.dumps(data_to_send), headers=header)













if __name__ == '__main__':

    def my_exception_hook(exctype, value, traceback):
        # Print the error and traceback
        print(exctype, value, traceback)
        # Call the normal Exception hook after
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)


    # Set the exception hook to our wrapping function



    #def Edit_Data_Client(self,name, id_document, address, user, password,id):
    # self.data_to_send= {"name": "client one", "document_id": "21324365", "address": "Mustafar 1", "user": "userone", "password": "12354"}

    client=ClientAPI("http://localhost:3000/clients")
    client.Change_Directory("/Users/brunasantos/Desktop/fake-api/fake_api")
    #client.Read_Json('endpoints.json')
    client.Verify_Connection_To_Json_Server("json-server --watch endpoints.json")
    client.Edit_Data_Client()
    url_id1="http://localhost:3000/clients/1"
    headers = {"Content-Type: application/json"}
    data = {"address": "Mustafar NEW", "user": "PoliwrathNEW XXXXX", "password": "start1234EW"}
    client.Edit_Data_Client(headers,data,url_id1)























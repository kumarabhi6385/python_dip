import sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.append(str(HERE / '..'))
from blobmanager.blobconfig import AzureBlobConfig

from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

import os
import uuid
import logging

class AzureBlobHandler():

    def __init__(self, config: AzureBlobConfig):
        self.config = config

    # def get_blob_service_client_sas(self):
    #     account_url = self.config.account_url
    #     credential = self.config.token
    #     # Create the BlobServiceClient object
    #     blob_service_client = BlobServiceClient(account_url, credential=credential)
    #     return blob_service_client
    def get_blob_service_client(self):
        blob_service_client = BlobServiceClient.from_connection_string(self.config.connectionString)
        return blob_service_client
    
    def get_list_containers(self):
        blob_service_client = self.get_blob_service_client()
        containers = blob_service_client.list_containers(include_metadata=True)
        result = []
        for container in containers:
             result.append(container['name'])
        return result
    
    def get_list_blob(self, containerName: str):
        blob_service_client = self.get_blob_service_client()
        container_client = blob_service_client.get_container_client(containerName)
        names = []
        blob_list = container_client.list_blobs()
        for blob in blob_list:
            names.append(blob.name)
        return names
     
    
    def uploadFile(self, filePath: str):
        logging.debug("Upload file method inside blob manager is called")
        blob_service_client = self.get_blob_service_client()
        container_client = blob_service_client.get_container_client(container=self.config.containername)
        with open(filePath, mode="rb") as data:
            blobname = str(uuid.uuid4())
            extension = os.path.splitext(filePath)[1]
            name = blobname + extension
            blob_client = container_client.upload_blob(name=name, data=data, overwrite=True)
        logging.debug("Upload file completed")


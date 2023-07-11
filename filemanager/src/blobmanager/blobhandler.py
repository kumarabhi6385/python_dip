import sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.append(str(HERE / '..'))
from blobmanager.blobconfig import AzureBlobConfig

from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

import logging

logging.basicConfig(level=logging.DEBUG, filename="output.log")

class AzureBlobHandler():

    def __init__(self, config: AzureBlobConfig):
        self.config = config

    def get_blob_service_client_sas(self):
        account_url = self.config.account_url
        credential = self.config.token
        # Create the BlobServiceClient object
        blob_service_client = BlobServiceClient(account_url, credential=credential)
        return blob_service_client
    
    def list_containers(self):
        i=0
        blob_service_client = self.get_blob_service_client_sas()
        containers = blob_service_client.list_containers(include_metadata=True)
        return containers
    
    def uploadFile(self, filePath: str):
        logging.debug("Upload file method inside blob manager is called")

import sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.append(str(HERE / '..'))
from blobmanager.blobhandler import AzureBlobConfig, AzureBlobHandler

import json
import logging

logging.basicConfig(level=logging.DEBUG, filename="output.log")

def getAzureStorageAccountConfiguration():
    with open("config.json") as file:
        config = json.load(file)
        blob_credential = config["azure_storage_account"]
    blobConfig = AzureBlobConfig(blob_credential["maxfilesize"], blob_credential["account_url"], blob_credential["token"])
    return blobConfig

def uploadfile(filePath: str):
    logging.debug("Upload file method is called")
    blobConfig = getAzureStorageAccountConfiguration()
    blobmanager = AzureBlobHandler(blobConfig)
    blobmanager.uploadFile(filePath)
    
uploadfile("config.json")

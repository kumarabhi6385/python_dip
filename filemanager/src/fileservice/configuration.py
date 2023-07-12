import sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.append(str(HERE / '..'))
from blobmanager.blobconfig import AzureBlobConfig

import logging
import json

class Configuration():
    def __init__(self):
        self.loadConfiguration()
        
    def loadConfiguration(self):
        try:
            with open("config.json") as file:
                config = json.load(file)
                blob_credential = config["azure_storage_account"]
                self.maxfilesize = blob_credential["maxfilesize"]
                self.account_url = blob_credential["account_url"]
                self.token = blob_credential["token"]
        except Exception as err:
            logging.exception(f"Exception details  - {err}")
            raise Exception(err)    
    
    def getAzureStorageAccountConfiguration(self):
        try:
            return AzureBlobConfig(self.maxfilesize, self.account_url, self.token)
        except Exception as err:
            logging.exception(f"Exception details  - {err}")
            raise Exception(err)
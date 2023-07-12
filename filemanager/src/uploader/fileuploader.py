import sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.append(str(HERE / '..'))
from blobmanager.blobhandler import AzureBlobConfig, AzureBlobHandler

import json
import logging

#logging.basicConfig(level=logging.DEBUG, filename="output.log")
logging.basicConfig(level=logging.DEBUG)

# def getAzureStorageAccountConfiguration():
#     try:
#         with open("config.json") as file:
#             config = json.load(file)
#             blob_credential = config["azure_storage_account"]
#         blobConfig = AzureBlobConfig(blob_credential["maxfilesize"], blob_credential["account_url"], blob_credential["token"], blob_credential["container_name"])
#         return blobConfig
#     except Exception as err:
#         logging.error(f"Exception Type  - {type(err)}")
#         logging.error(f"Exception arguments  - {err.args}")
#         logging.error(f"Exception details  - {err}")
#         raise Exception(err)

def getAzureStorageAccountConfiguration():
    try:
        with open("config.json") as file:
            config = json.load(file)
            blob_credential = config["azure_storage_account"]
        blobConfig = AzureBlobConfig(blob_credential["account_name"], blob_credential["account_key"], blob_credential["connectionstring"], blob_credential["container_name"])
        return blobConfig
    except Exception as err:
        logging.error(f"Exception Type  - {type(err)}")
        logging.error(f"Exception arguments  - {err.args}")
        logging.error(f"Exception details  - {err}")
        raise Exception(err)


def uploadfile(filePath: str):
    try:
        logging.debug("Upload file method is called")
        blobConfig = getAzureStorageAccountConfiguration()
        blobmanager = AzureBlobHandler(blobConfig)
        blobmanager.uploadFile(filePath)
    except Exception as err:
        logging.error(f"Exception Type  - {type(err)}")
        logging.error(f"Exception arguments  - {err.args}")
        logging.error(f"Exception details  - {err}")
        raise Exception(err)
    
def getContianerDetails():
    try:
        logging.debug("getContianerDetails method is called")
        blobConfig = getAzureStorageAccountConfiguration()
        blobmanager = AzureBlobHandler(blobConfig)
        data = blobmanager.list_containers()
        logging.debug(f"Container list {data}")
    except Exception as err:
        logging.error(f"Exception Type  - {type(err)}")
        logging.error(f"Exception arguments  - {err.args}")
        logging.error(f"Exception details  - {err}")
        raise Exception(err)
    
def getListOfBlobs():
    try:
        logging.debug("getListOfBlobs method is called")
        blobConfig = getAzureStorageAccountConfiguration()
        blobmanager = AzureBlobHandler(blobConfig)
        data = blobmanager.get_list_blob(blobConfig.containername)
        logging.debug(f"blob list {data}")
    except Exception as err:
        logging.error(f"Exception Type  - {type(err)}")
        logging.error(f"Exception arguments  - {err.args}")
        logging.error(f"Exception details  - {err}")
        raise Exception(err)
    
#getContianerDetails()
uploadfile(r"C:\Users\Abhishek.Srivastava\Desktop\src\GoF_Book.pdf")
getListOfBlobs()

import sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.append(str(HERE / '..'))
from blobmanager.blobhandler import AzureBlobConfig, AzureBlobHandler

import json
import logging
import asyncio

#logging.basicConfig(level=logging.DEBUG, filename="output.log")
logging.basicConfig(level=logging.DEBUG)

def getAzureStorageAccountConfiguration():
    try:
        with open("config.json") as file:
            config = json.load(file)
            blob_credential = config["azure_storage_account"]
        blobConfig = AzureBlobConfig(blob_credential["maxfilesize"], blob_credential["account_url"], blob_credential["token"])
        return blobConfig
    except Exception as err:
        logging.exception(f"Exception details  - {err}")
        raise Exception(err)

async def uploadfile(filePath: str):
    try:
        logging.debug("Upload file method is called")
        blobConfig = getAzureStorageAccountConfiguration()
        blobmanager = AzureBlobHandler(blobConfig)
        await blobmanager.uploadFile_async(filePath)
    except Exception as err:
        logging.exception(f"Exception details  - {err}")
        raise Exception(err)
    
async def getListOfBlobsAsync():
    try:
        logging.debug("Inside getListOfBlobs method")
        blobConfig = getAzureStorageAccountConfiguration()
        blobmanager = AzureBlobHandler(blobConfig)
        data = await blobmanager.get_list_blob_async()
    except Exception as err:
        logging.exception(f"Exception details  - {err}")
        raise Exception(err)
    finally:
        logging.debug("Outside getListOfBlobs method")
        return data
    
async def deleteBlobAsync(blobname:str):
    try:
        logging.debug("Inside deleteBlobAsync method")
        blobConfig = getAzureStorageAccountConfiguration()
        blobmanager = AzureBlobHandler(blobConfig)
        data = await blobmanager.delete_blob_async(blobname)
    except Exception as err:
        logging.exception(f"Exception details  - {err}")
        raise Exception(err)
    finally:
        logging.debug("Outside deleteBlobAsync method")
        return data
    
async def deleteBlobsAsync(blobs:list):
    try:
        logging.debug("Inside deleteBlobsAsync method")
        blobConfig = getAzureStorageAccountConfiguration()
        blobmanager = AzureBlobHandler(blobConfig)
        data = await blobmanager.delete_blobs_async(blobs)
    except Exception as err:
        logging.exception(f"Exception details  - {err}")
        raise Exception(err)
    finally:
        logging.debug("Outside deleteBlobsAsync method")
        return data
    
async def deleteAllBlobsAsync():
    try:
        logging.debug("Inside deleteAllBlobsAsync method")
        blobConfig = getAzureStorageAccountConfiguration()
        blobmanager = AzureBlobHandler(blobConfig)
        data = await blobmanager.delete_all_blobs_async()
    except Exception as err:
        logging.exception(f"Exception details  - {err}")
        raise Exception(err)
    finally:
        logging.debug("Outside deleteAllBlobsAsync method")
        return data
    
async def main():
    await uploadfile(r"C:\Users\Abhishek.Srivastava\Desktop\src\GoF_Book.pdf")
    #await deleteBlobAsync(r"60e83468-c652-4e71-be94-fd9a5da5f4ee..pdf")
    #await deleteBlobsAsync(['02b3c876-c0c3-4aa2-a43c-7bdd25d42299.pdf', 'd504aa28-ef62-41e9-a3d5-975601020b2a.pdf'])
    #await deleteAllBlobsAsync()
    data = await getListOfBlobsAsync()
    logging.info(data)

if __name__ == '__main__':
    asyncio.run(main())

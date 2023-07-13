import sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.append(str(HERE / '..'))

from blobmanager.blobconfig import AzureBlobConfig

from azure.identity import DefaultAzureCredential
from azure.storage.blob.aio import BlobServiceClient, BlobClient, ContainerClient

import os
import uuid
import logging

class AzureBlobHandler():

    # config should have account_url and sas token for specific container
    def __init__(self, config: AzureBlobConfig):
        self.config = config
    
    # Below function will be be used to upload file using azure
    # when absolute path of the file is given
    async def uploadFile_async(self, filePath: str):
        try:
            container = ContainerClient.from_container_url(
                container_url=self.config.account_url,
                credential=self.config.token,
            )
            with open(filePath, mode="rb") as data:
                blobname = str(uuid.uuid4())
                extension = os.path.splitext(filePath)[1]
                name = blobname + extension
                await container.upload_blob(name=name, data=data, overwrite=True)
        except Exception as err:
            logging.exception(f"Exception details  - {err}")
            raise Exception(err)
        finally:
            await container.close()

    # Below function will be be used to upload file using file object
    async def uploadFileData_async(self, file):
        try:
            container = ContainerClient.from_container_url(
                container_url=self.config.account_url,
                credential=self.config.token,
            )
            blobname = str(uuid.uuid4())
            extension = ".pdf"
            name = blobname + extension
            await container.upload_blob(name=name, data=file, overwrite=True)
        except Exception as err:
            logging.exception(f"Exception details  - {err}")
            raise Exception(err)
        finally:
            await container.close()

    # Below function will be be used to list of blobs
    async def get_list_blob_async(self):
        blob_list = []
        try:
            container = ContainerClient.from_container_url(
                container_url=self.config.account_url,
                credential=self.config.token,
            )
            # async for blob in container.list_blob_names():
            #     blob_list.append(blob)
            #blobs = container.list_blob_names().by_page()
            blob_list = [b async for b in container.list_blob_names()]
        except Exception as err:
            logging.exception(f"Exception details  - {err}")
            raise Exception(err)
        finally:
            await container.close()
            logging.debug(f"Received blobs {blob_list}")
            return blob_list
        
    # Below function will be be used to delete the blob
    async def delete_blob_async(self, blobname:str):
        try:
            container = ContainerClient.from_container_url(
                container_url=self.config.account_url,
                credential=self.config.token,
            )
            blobs = [blobname]
            await container.delete_blobs(*blobs)
        except Exception as err:
            logging.exception(f"Exception details  - {err}")
            raise Exception(err)
        finally:
            await container.close()

    # Below function will be be used to delete list of blobs
    async def delete_blobs_async(self, blobs:list):
        try:
            container = ContainerClient.from_container_url(
                container_url=self.config.account_url,
                credential=self.config.token,
            )
            await container.delete_blobs(*blobs)
        except Exception as err:
            logging.exception(f"Exception details  - {err}")
            raise Exception(err)
        finally:
            await container.close()
    
    # Below function will be be used to delete list of blobs
    async def delete_all_blobs_async(self):
        try:
            container = ContainerClient.from_container_url(
                container_url=self.config.account_url,
                credential=self.config.token,
            )
            blob_list = [b async for b in container.list_blob_names()]
            logging.debug(blob_list)
            await container.delete_blobs(*blob_list)
        except Exception as err:
            logging.exception(f"Exception details  - {err}")
            raise Exception(err)
        finally:
            await container.close()
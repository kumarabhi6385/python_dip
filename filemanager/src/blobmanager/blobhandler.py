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

    def __init__(self, config: AzureBlobConfig):
        self.config = config

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

    async def get_list_blob_async(self):
        blobs_list = []
        try:
            container = ContainerClient.from_container_url(
                container_url=self.config.account_url,
                credential=self.config.token,
            )
            async for blob in container.list_blob_names():
                blobs_list.append(blob)
        except Exception as err:
            logging.exception(f"Exception details  - {err}")
            raise Exception(err)
        finally:
            await container.close()
            logging.debug(f"Received blobs {blobs_list}")
            return blobs_list
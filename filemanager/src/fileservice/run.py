import sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.append(str(HERE / '..'))
from fastapi import FastAPI
from blobmanager.blobhandler import AzureBlobConfig, AzureBlobHandler
from configuration import Configuration


import json
import logging

#logging.basicConfig(level=logging.DEBUG, filename="output.log")
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()
config = Configuration()

@app.get("/")
async def get_root():
    try:
        blobConfig = config.getAzureStorageAccountConfiguration()
        blobmanager = AzureBlobHandler(blobConfig)
        data = await blobmanager.get_list_blob_async()
    except Exception as err:
        logging.exception(f"Exception details  - {err}")
    finally:
        return json.dumps(data)
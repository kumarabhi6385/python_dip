import sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.append(str(HERE / '..'))
from fastapi import FastAPI,HTTPException,File,UploadFile
from blobmanager.blobhandler import AzureBlobConfig, AzureBlobHandler
from configuration import Configuration

from pydantic import BaseModel

import json
import logging

#logging.basicConfig(level=logging.DEBUG, filename="output.log")
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()
config = Configuration()

class Blobs(BaseModel):
    blobs: list

@app.get("/")
async def get_root():
    return "Welcome to File service built on Fast API"
    
@app.get("/blobs")
async def blob_list():
    try:
        blobConfig = config.getAzureStorageAccountConfiguration()
        blobmanager = AzureBlobHandler(blobConfig)
        data = await blobmanager.get_list_blob_async()
    except Exception as err:
        logging.exception(f"Exception details  - {err}")
    finally:
        return json.dumps(data)
    
@app.post("/uploadfile")
async def upload_file(file: UploadFile = File(...)):
    logging.debug("Inside create_upload_file")
    try:
        blobConfig = config.getAzureStorageAccountConfiguration()
        blobmanager = AzureBlobHandler(blobConfig)
        await blobmanager.uploadFileData_async(file) 
        return {"filename": file.filename, "message": "File is uploaded"}
    except Exception as err:
        logging.exception(f"Exception details  - {err}")
        raise HTTPException(status_code=500, detail="can not delete")
    
@app.delete("/blobs/{blob_name}")
async def delete_blob(blob_name: str):
    try:
        blobConfig = config.getAzureStorageAccountConfiguration()
        blobmanager = AzureBlobHandler(blobConfig)
        await blobmanager.delete_blob_async(blob_name)
        return {"message": "Blob is deleted"}
    except Exception as err:
        logging.exception(f"Exception details  - {err}")
        raise HTTPException(status_code=500, detail="can not delete")

@app.delete("/blobs/")
async def delete_blobs(item: Blobs):
    try:
        logging.debug(f"delete_blobs is called")
        blobConfig = config.getAzureStorageAccountConfiguration()
        blobmanager = AzureBlobHandler(blobConfig)
        await blobmanager.delete_blobs_async(item.blobs)
        return {"message": "Blobs are deleted"}
    except Exception as err:
        logging.exception(f"Exception details  - {err}")
        raise HTTPException(status_code=500, detail="can not delete")
    
@app.delete("/blobs/all/")
async def delete_blobs_all():
    try:
        logging.debug(f"delete_blobs is called")
        blobConfig = config.getAzureStorageAccountConfiguration()
        blobmanager = AzureBlobHandler(blobConfig)
        await blobmanager.delete_all_blobs_async()
        return {"message": "Blobs are deleted"}
    except Exception as err:
        logging.exception(f"Exception details  - {err}")
        raise HTTPException(status_code=500, detail="can not delete")

import sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.append(str(HERE / '..'))
from fastapi import FastAPI
from blobmanager.blobhandler import AzureBlobConfig, AzureBlobHandler

app = FastAPI()
@app.get("/")
def get_root():
    blobconfig = AzureBlobConfig("test", "test1", "test2")
    blobClient = AzureBlobHandler(blobconfig)
    data = blobClient.uploadFile()
    return data
    #return "Welcome to API written in python"
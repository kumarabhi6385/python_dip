import sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.append(str(HERE / '..'))

from blobmanager.blobconfig import AzureBlobConfig

class AzureBlobHandler():
    def __init__(self, config: AzureBlobConfig):
        self.config = config
    def uploadFile(self):
        return "Upload method is called"

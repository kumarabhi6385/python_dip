class AzureBlobConfig():
    def __init__(self, maxfilesize, account_url, token, containername = ""):
        self.maxfilesize = maxfilesize
        self.account_url = account_url
        self.token = token
        self.containername = containername

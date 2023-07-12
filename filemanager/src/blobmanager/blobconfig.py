class AzureBlobConfig():
    def __init__(self, maxfilesize, account_url, token):
        self.maxfilesize = maxfilesize
        self.account_url = account_url
        self.token = token
class AzureBlobConfig():
    # def __init__(self, maxfilesize, account_url, token, containername = ""):
    #     self.maxfilesize = maxfilesize
    #     self.account_url = account_url
    #     self.token = token
    #     self.containername = containername
    def __init__(self, account_name:str, account_key:str, 
                 connectionString:str, containername:str):
        self.account_name = account_name
        self.account_key = account_key
        self.connectionString = connectionString
        self.containername = containername
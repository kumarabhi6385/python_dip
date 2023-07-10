# python_dip

This Project will used to demonstrate large files to be uploaded on blobs for further processing using DIP.

# Process

1. On Client Side - One python package is created to upload files by splitting into smaller chunks and upload into azure blobs

2. On server side - A web app used to display details of uploaded blob which is store in database (it could be cosmos db, mongo db etc)

3. On server side - Another python package which will be triggered when new blob is added to azure. This package will be used to process file using DIP or text analysis.

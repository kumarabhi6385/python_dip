# python_dip

This Project will used to demonstrate large files to be uploaded on blobs for further processing using DIP.

# Process

1. On Client Side - One python package is created to upload files by splitting into smaller chunks and upload into azure blobs

2. On server side - A web app used to display details of uploaded blob which is store in database (it could be cosmos db, mongo db etc)

3. On server side - Another python package which will be triggered when new blob is added to azure. This package will be used to process file using DIP or text analysis.

# Steps:

1. Create a new directory.
   mkdir python_dip
2. python -m venv filemanager
   run source bin/activate on mac
   filemanager/Scripts/activate on windows to activate virtual environment.
3. create src folder to contain python files
4. pip3 install pipreqs
5. Create projects and install dependency
6. import packages in files
7. run pipreqs

# to install dependency run

pip install -r requirement.txt

# set up azure blob conenction with python

pip install azure-storage-blob azure-identity

from zipfile import ZipFile

with ZipFile("digit-recognizer.zip", 'r') as unzip:

    unzip.printdir() # <<-- Check inside zip file

    unzip.extract('train.csv') # <<-- Extract a single file

    #unzip.extractall() # <<-- Extract all files at once
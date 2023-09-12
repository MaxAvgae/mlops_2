import wget, zipfile

url_dataset = "https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip"
zip_name = "kagglecatsanddogs_5340.zip"
directory_to_extract = "cats_and_dogs"

wget.download(url_dataset)
with zipfile.ZipFile(zip_name, "r") as myzip:
    myzip.extractall(directory_to_extract)

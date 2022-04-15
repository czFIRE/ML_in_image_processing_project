import wget
import os

import shutil

basic_url: str = "https://data.vision.ee.ethz.ch/cvl/DIV2K/"
index_file_path: str = "datasets.txt"

print("\nDownloading and extracting dataset to this directory.\n")

with open(index_file_path, "r") as file:
    for line in file.readlines():
        # if you don't have wget module then uncomment the next line and comment the wget command
        # os.system("wget " + basic_url + line[:-1] + ".zip")
        wget.download(basic_url + line[:-1] + ".zip")

        shutil.unpack_archive("./" + line[:-1] + ".zip")

print("\nAll done!")

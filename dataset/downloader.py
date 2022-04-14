import os
import shutil

basic_url: str = "https://data.vision.ee.ethz.ch/cvl/DIV2K/"
index_file_path: str = "datasets.txt"

file = open(index_file_path, "r")

print("Downloading and extracting dataset to this directory.")

for line in file.readlines():
    os.system("wget " + basic_url + line[:-1] + ".zip")
    shutil.unpack_archive("./" + line[:-1] + ".zip")

print("All done!")
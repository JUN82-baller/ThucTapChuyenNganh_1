import os 
from zipfile import ZipFile

os.system("kaggle datasets download -d ahmeduzaki/global-earthquake-tsunami-risk-assessment-dataset")

with ZipFile("global-earthquake.zip", 'r') as zip_ref:
    zip_ref.extractall("data/")

print("Data downloaded and extracted to 'data/' directory.")
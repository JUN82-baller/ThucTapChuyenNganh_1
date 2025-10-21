import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

 #1 xac thuc voi Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("d:/earthquake_project/src/earthquake-data-uploader-f94703799f78.json", scope)
client = gspread.authorize(creds)

#2 mo Google Sheet
spreadsheet = client.open("Earthquake_data")
worksheet = spreadsheet.sheet1

#3 ghi du lieu vao sheet
df=pd.read_csv('data/earthquake_data_tsunami.csv')
worksheet.update([df.columns.values.tolist()] + df.values.tolist())

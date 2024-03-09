import gspread
from oauth2client.service_account import ServiceAccountCredentials
from howlongtobeatpy import HowLongToBeat

def get_game_id(game_name):
    hltb = HowLongToBeat()
    results = hltb.search(game_name)
    if results:
        return results[0].game_id
    else:
        return "Not found"

def process_google_sheet(sheet):
    print("Processing Google Sheet...")
    game_names = sheet.col_values(2)
    for i, game_name in enumerate(game_names[2:], start=3):
        print(f"Processing row {i}...")
        game_id = get_game_id(game_name)
        sheet.update_cell(i, 9, game_id) # chose what column do you want to add or you could retrive the data in the cmd only or whatever you want
    print("Processing complete.")

creds_file = "" #JSON file here with the path 
sheet_url = ""
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
client = gspread.authorize(creds)
sheet = client.open_by_url(sheet_url).sheet1

process_google_sheet(sheet)
#to run the code use the cmd 

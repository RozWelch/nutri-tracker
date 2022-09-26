# terminal is 80 characters wide and 24 rows high

# code for accessing google spreadsheet taken from Love Sandwiches walk-through project
import gspread
from google.oauth2.service_account import Credentials
from rich.text import Text

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('habit_tracker')

measurments = SHEET.worksheet('measurments')

person_data = measurments.get_all_values()

print(person_data)

# print home screen page
print(""" 
......            ___  __       ___  __        __        ___  __   ......
......  |\ | |  |  |  |__) |     |  |__)  /\  /  ` |__/ |__  |__)  ......
......  | \| \__/  |  |  \ |     |  |  \ /~~\ \__, |  \ |___ |  \  ......
 ......................................................................
 .   o   \ o /  _ o        __|    \ /     |__         o _  \ o /   o   .
 .  /|\    |     /\   __\o   \o    |    o/     o/__   /\     |    /|\  .
 .  / \   / \   | \  /) |    ( \  /o\  / )    |   (\  / |   / \   / \  .
 .......................................................................
                                                          """)

returning = input('Hello, have you used Nutri Tracker before? Yes/No ')
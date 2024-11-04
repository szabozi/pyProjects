import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = "1dJ6hbtjncWYa_7qKYu70CGbY2VWqZ36UX2NkKEgdaxA"


def main():
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())

    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()

        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="Book-List!A1:N5046").execute()
        sheet_data = result.get("values", [])

        # Set to store unique values from Column A where Column H is "yes"
        unique_values_column_a = set()

        # printing only column A
        for record in sheet_data:
            # Ensure both Column A and Column H exist in the row
            if len(record) >= 8 and record[0] and record[7].lower() == "yes":
                unique_values_column_a.add(record[0])  # Add only Column A value if Column H is "yes"

        # Convert the set to a list and sort it alphabetically
        sorted_values_column_a = sorted(list(unique_values_column_a))

        # Print out all unique values from Column A
        for value in sorted_values_column_a:
            print(value)

    except HttpError as error:
        print(error)


if __name__ == "__main__":
    main()

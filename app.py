from flask import Flask, request, render_template
import gspread
import os
import json
from oauth2client.service_account import ServiceAccountCredentials
app = Flask(__name__) #by writing __name__ inside telling flask where to find the templates

# Read credentials from environment variable
cred_json = os.getenv("GOOGLE_SHEET_CREDENTIALS")
cred_dict = json.loads(cred_json)

# Setup Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(cred_dict, scope)
client = gspread.authorize(creds)

# Open your Google Sheet by name
sheet = client.open("UserResponses").sheet1

@app.route('/', methods = ['GET', 'POST'])
def user_form():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        email = request.form.get('email')
        birthday = request.form.get('birthday')
        phone_number = request.form.get('phone')
        instagram = request.form.get('instagram')
        gender = request.form.get('gender')


        sheet.append_row([name, age, email, gender, birthday, phone_number, instagram])
        return f"<h2>Thanks, {name}!</h2><p>Your data has been saved to Google Sheets.</p>"

    return render_template('form.html')

@app.route('/users_list', methods = ['GET'])
def users_list():
    return f"users list page"

if __name__ == '__main__':
    app.run(debug=True)

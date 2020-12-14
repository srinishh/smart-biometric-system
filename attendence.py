import gspread
import datetime

gc = gspread.service_account(filename='attendence_cred.json')
sh = gc.open_by_key('1qo9lPJ1xRu1tcnywkNwdogBYJ7yCBnEFimZ9cV-wxXM')
worksheet = sh.sheet1



def markAttendence(name):
    x = datetime.datetime.now()
    date = x.strftime("%x")
    time = x.strftime("%X")
    li = [date,name,time]
    worksheet.append_row(li)



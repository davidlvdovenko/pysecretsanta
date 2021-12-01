# Imports (External)
import json
from prettytable import prettytable
from prettytable import from_csv
import csv
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Import Config File and Initialize variables and preferneces
with open("config.json", "r") as jsonfile:
    configfile = json.load(jsonfile)

tabletitle = configfile["title"]
emailbody = configfile["body"]
emailbody2 = configfile["body2"]
emailbody3 = configfile["body3"]
emailsignature = configfile["signature"]
listname = configfile["listname"]
smtprelay = configfile["smtprelay"]
smtpport = configfile["smtpport"]
smtpuser = configfile["user"]
smtppassword = configfile["password"]

# Create Table
SantasMasterRecord = prettytable.PrettyTable()
SantasMasterRecord.field_names = ["Secret Santa", "Recipient"]

# Create SMTP Connection
smtpserver = server = smtplib.SMTP(smtprelay,smtpport)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.login(smtpuser,smtppassword)

# Open CSV File
csvfile = open(listname, newline='')
csvdata = csv.reader(csvfile, delimiter=',', quotechar='|')

# Initialize Array for Secret Santa Array and Recipient Array
secretsantaarray = []
recipientarray = []
secretsantaemailarray = []

for line in csvdata:
    secretsantaarray.append(line[0])
    recipientarray.append(line[0])
    secretsantaemailarray.append(line[1])

# For every person in Secret Santa Array - assign a random person in the Recieving Array, that is not equal to itself.
Person = 0

for secretsanta in secretsantaarray:
    while True:
        recipient = random.choice(recipientarray)
        if recipient is not secretsanta:
            break
        else:
            continue
    
    # Add Entry to Table
    SantasMasterRecord.add_row([secretsanta,recipient])

    # Remove person from Recieving Array
    recipientarray.remove(recipient)

    # Send Email to Secret Santa
    print(secretsantaemailarray[Person])
    sentto = secretsantaemailarray[Person]

    message = MIMEMultipart("alternative")
    message["Subject"] = "Winter Camp Secret Santa"
    message["From"] = smtpuser
    message["To"] = sentto

    text = """\
    Hello """+secretsanta+""",

    """+emailbody+recipient+"""
    """+emailbody2+"""
    """+emailbody3+"""
    
    """+"Merry Christmas,"+"""
    """+emailsignature+"""
    """

    part1 = MIMEText(text, "plain")
    message.attach(part1)

    try:
        smtpserver.sendmail(smtpuser, sentto, message.as_string())
    except:
        continue

    # Step Next
    Person = Person+1

# Generate Table
masterlist = SantasMasterRecord.get_string()
with open('masterlist.txt', 'w') as f:
    f.write(masterlist)

# Clean Up
csvfile.close()
smtpserver.close()

# End
exit
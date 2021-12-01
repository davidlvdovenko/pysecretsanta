# Textline GUI
print("""
Welcome to Secret Santa Python Script
Please make sure you have everything setup correctly before proceeding
Visit: https://github.com/davidlvdovenko/pysecretsanta for instructions""")
input("---Press Enter to continue---")
print("")

# Textline GUI
print("Importing Libraries...")

## Imports (External)
try:
    import json
    from os import execlp
    from prettytable import prettytable
    from prettytable import from_csv
    import csv
    import random
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
except:
    print("Fatal Error: Failed to import libraries.")
    input("---Please click ENTER to exit script---")
    exit

# Textline GUI
print("Importing Configuration File...")

## Import Config File and Initialize variables and preferneces
try:
    with open("config.json", "r") as jsonfile:
        configfile = json.load(jsonfile)
except:
    print("Fatal Error: Failed to import config.json.")
    input("---Please click ENTER to exit script---")
    exit

# Textline GUI
print("Assigning Configuration Variables...")

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

# Textline GUI
print("Creating Table...")

## Create Table
try:
    SantasMasterRecord = prettytable.PrettyTable()
    SantasMasterRecord.field_names = ["Secret Santa", "Recipient"]
except:
    print("Fatal Error: Failed to create table.")
    input("---Please click ENTER to exit script---")
    exit

# Textline GUI
print("Establishing Email Connection...")

## Create SMTP Connection
try:
    smtpserver = server = smtplib.SMTP(smtprelay,smtpport)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.login(smtpuser,smtppassword)
except:
    print("Fatal Error: Failed to connect to Email Service.")
    input("---Please click ENTER to exit script---")
    exit

# Textline GUI
print("Opening Santa's List...")

## Open CSV File
try:
    csvfile = open(listname, newline='')
    csvdata = csv.reader(csvfile, delimiter=',', quotechar='|')
except:
    print("Fatal Error: Failed to open Santa's List.")
    input("---Please click ENTER to exit script---")
    exit

# Textline GUI
print("Creating Arrays...")

## Initialize Array for Secret Santa Array and Recipient Array
try:
    secretsantaarray = []
    recipientarray = []
    secretsantaemailarray = []

    for line in csvdata:
        secretsantaarray.append(line[0])
        recipientarray.append(line[0])
        secretsantaemailarray.append(line[1])
except:
    print("Fatal Error: Failed to parse Santa's List")
    input("---Please click ENTER to exit script---")
    exit

# Textline GUI
print("Drawing Names...")

## For every person in Secret Santa Array - assign a random person in the Recieving Array, that is not equal to itself.
Person = 0

try:
    for secretsanta in secretsantaarray:
        while True:
            recipient = random.choice(recipientarray)
            if recipient is not secretsanta:
                break
            else:
                continue

        ## Add Entry to Table
        SantasMasterRecord.add_row([secretsanta,recipient])

        ## Remove person from Recieving Array
        recipientarray.remove(recipient)

        ## Send Email to Secret Santa
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

        # Textline GUI
        print("Sending email to "+sentto+"...")

        try:
            smtpserver.sendmail(smtpuser, sentto, message.as_string())
        except:
            print("Error: Cannot send email to the following address:"+sentto)
            continue

        ## Step Next
        Person = Person+1
except:
    print("Fatal Error: Failed in selection loop. Please contact script creator.")
    input("---Please click ENTER to exit script---")
    exit

# Textline GUI
print("")
print("Generating Masterlist...")

## Generate Table
try:
    masterlist = SantasMasterRecord.get_string()
    with open('masterlist.txt', 'w') as f:
        f.write(masterlist)
except:
    print("Fatal Error: Failed to generate master list.")
    input("---Please click ENTER to exit script---")
    exit

# Textline GUI
print("Finishing Up...")

## Clean Up
csvfile.close()
smtpserver.close()

# Textline GUI
print("")
print("""
Congrats! The script ran successfully. 
The masterlist file has been generated and contains the list of Santas and Recipients.
Make sure to keep this file secret :)""")
input("---Please click ENTER to exit---")

## End
exit
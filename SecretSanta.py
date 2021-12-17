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
location = configfile["location"]
date = configfile["date"]
description = configfile["description"]
emailsignature = configfile["signature"]
image = configfile["image"]
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
        message["Subject"] = tabletitle
        message["From"] = smtpuser
        message["To"] = sentto

        text = """\
        Hello """+secretsanta+""",

        Location: """+location+"""
        Date: """+date+"""
        Description"""+description+"""
        Your Recipient: """+recipient+"""
        
        """+"Merry Christmas,"+"""
        """+emailsignature+"""
        """

        html = """\
            <html lang="en" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml">
            <head>
            <title></title>
            <meta charset="utf-8"/>
            <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
            <!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]-->
            <!--[if !mso]><!-->
            <link href="https://fonts.googleapis.com/css?family=Alegreya" rel="stylesheet" type="text/css"/>
            <link href="https://fonts.googleapis.com/css?family=Bitter" rel="stylesheet" type="text/css"/>
            <link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet" type="text/css"/>
            <link href="https://fonts.googleapis.com/css2?family=Satisfy&display=swap" rel="stylesheet" type="text/css"/>
            <!--<![endif]-->
            <style>
                    * {
                        box-sizing: border-box;
                    }

                    body {
                        margin: 0;
                        padding: 0;
                    }

                    a[x-apple-data-detectors] {
                        color: inherit !important;
                        text-decoration: inherit !important;
                    }

                    #MessageViewBody a {
                        color: inherit;
                        text-decoration: none;
                    }

                    p {
                        line-height: inherit
                    }

                    @media (max-width:660px) {
                        .icons-inner {
                            text-align: center;
                        }

                        .icons-inner td {
                            margin: 0 auto;
                        }

                        .row-content {
                            width: 100% !important;
                        }

                        .stack .column {
                            width: 100%;
                            display: block;
                        }
                    }
                </style>
            </head>
            <body style="background-color: #000; margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
            <table border="0" cellpadding="0" cellspacing="0" class="nl-container" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #000;" width="100%">
            <tbody>
            <tr>
            <td>
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
            <tbody>
            <tr>
            <td>
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #000000; color: #000000; width: 640px;" width="640">
            <tbody>
            <tr>
            <td class="column" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
            <table border="0" cellpadding="0" cellspacing="0" class="heading_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
            <tr>
            <td style="width:100%;text-align:center;padding-top:50px;">
            <h1 style="margin: 0; color: #ffffff; font-size: 36px; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; line-height: 120%; text-align: center; direction: ltr; font-weight: normal; letter-spacing: normal; margin-top: 0; margin-bottom: 0;"><strong>"""+tabletitle+"""</strong></h1>
            </td>
            </tr>
            </table>
            <table border="0" cellpadding="0" cellspacing="0" class="text_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
            <tr>
            <td style="padding-left:10px;padding-right:10px;padding-top:50px;">
            <div style="font-family: 'Trebuchet MS', Tahoma, sans-serif">
            <div style="font-size: 12px; font-family: 'Montserrat', 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif; mso-line-height-alt: 14.399999999999999px; color: #ffffff; line-height: 1.2;">
            <p style="margin: 0; font-size: 14px; text-align: center;"><strong><span style="font-size:18px;">Hello """+secretsanta+"""</span></strong></p>
            </div>
            </div>
            </td>
            </tr>
            </table>
            <table border="0" cellpadding="0" cellspacing="0" class="text_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
            <tr>
            <td style="padding-left:10px;padding-right:10px;padding-top:10px;">
            <div style="font-family: 'Trebuchet MS', Tahoma, sans-serif">
            <div style="font-size: 12px; font-family: 'Montserrat', 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif; mso-line-height-alt: 14.399999999999999px; color: #c1272d; line-height: 1.2;">
            <p style="margin: 0; font-size: 34px; text-align: center;">Your Recipient: """+recipient+"""</p>
            </div>
            </div>
            </td>
            </tr>
            </table>
            <table border="0" cellpadding="0" cellspacing="0" class="image_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
            <tr>
            <td style="width:100%;padding-right:0px;padding-left:0px;padding-bottom:70px;">
            <div align="center" style="line-height:10px"><img alt="Christmas image" src='"""+image+"""' style="display: block; height: auto; border: 0; width: 448px; max-width: 100%;" title="Christmas image" width="448"/></div>
            </td>
            </tr>
            </table>
            </td>
            </tr>
            </tbody>
            </table>
            </td>
            </tr>
            </tbody>
            </table>
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
            <tbody>
            <tr>
            <td>
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #000000; color: #000000; width: 640px;" width="640">
            <tbody>
            <tr>
            <td class="column" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
            <table border="0" cellpadding="0" cellspacing="0" class="text_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
            <tr>
            <td style="padding-left:10px;padding-right:10px;">
            <div style="font-family: 'Trebuchet MS', Tahoma, sans-serif">
            <div style="font-size: 12px; font-family: 'Montserrat', 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif; mso-line-height-alt: 14.399999999999999px; color: #c1272d; line-height: 1.2;">
            <p style="margin: 0; font-size: 34px; text-align: center;"><span style="font-size:34px;">Merry Christmas</span></p>
            </div>
            </div>
            </td>
            </tr>
            </table>
            <table border="0" cellpadding="0" cellspacing="0" class="text_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
            <tr>
            <td style="padding-left:10px;padding-right:10px;padding-top:20px;">
            <div style="font-family: 'Trebuchet MS', Tahoma, sans-serif">
            <div style="font-size: 12px; font-family: 'Montserrat', 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif; mso-line-height-alt: 14.399999999999999px; color: #ffffff; line-height: 1.2;">
            <p style="margin: 0; font-size: 14px; text-align: center;"><strong><span style="font-size:18px;">"""+emailsignature+"""</span></strong></p>
            </div>
            </div>
            </td>
            </tr>
            </table>
            <table border="0" cellpadding="0" cellspacing="0" class="text_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
            <tr>
            <td style="padding-bottom:60px;padding-left:45px;padding-right:45px;padding-top:30px;">
            <div style="font-family: 'Trebuchet MS', Tahoma, sans-serif">
            <div style="font-size: 12px; font-family: 'Montserrat', 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif; mso-line-height-alt: 14.399999999999999px; color: #ffffff; line-height: 1.2;">
            <p style="margin: 0; font-size: 14px; text-align: center;">"""+description+"""</p>
            </div>
            </div>
            </td>
            </tr>
            </table>
            </td>
            </tr>
            </tbody>
            </table>
            </td>
            </tr>
            </tbody>
            </table>
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-3" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
            <tbody>
            <tr>
            <td>
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #000000; color: #000000; width: 640px;" width="640">
            <tbody>
            <tr>
            <td class="column" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
            <table border="0" cellpadding="0" cellspacing="0" class="divider_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
            <tr>
            <td style="padding-left:10px;padding-right:10px;padding-top:50px;">
            <div align="center">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="80%">
            <tr>
            <td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 2px solid #C1272D;"><span> </span></td>
            </tr>
            </table>
            </div>
            </td>
            </tr>
            </table>
            </td>
            </tr>
            </tbody>
            </table>
            </td>
            </tr>
            </tbody>
            </table>
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-4" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
            <tbody>
            <tr>
            <td>
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #000000; color: #000000; width: 640px;" width="640">
            <tbody>
            <tr>
            <td class="column" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
            <div class="spacer_block" style="height:50px;line-height:50px;font-size:1px;"> </div>
            </td>
            </tr>
            </tbody>
            </table>
            </td>
            </tr>
            </tbody>
            </table>
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-5" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
            <tbody>
            <tr>
            <td>
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #000000; color: #000000; width: 640px;" width="640">
            <tbody>
            <tr>
            <td class="column" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
            <div class="spacer_block" style="height:40px;line-height:20px;font-size:1px;"> </div>
            </td>
            </tr>
            </tbody>
            </table>
            </td>
            </tr>
            </tbody>
            </table>
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-6" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
            <tbody>
            <tr>
            <td>
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 640px;" width="640">
            <tbody>
            <tr>
            <td class="column" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
            <table border="0" cellpadding="0" cellspacing="0" class="icons_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
            <tr>
            <td style="padding-bottom:5px;padding-top:5px;color:#9d9d9d;font-family:inherit;font-size:15px;text-align:center;">
            <table cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
            <tr>
            <td style="text-align:center;">
            <!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
            <!--[if !vml]><!-->
            <table cellpadding="0" cellspacing="0" class="icons-inner" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block; margin-right: -4px; padding-left: 0px; padding-right: 0px;">
            <!--<![endif]-->
            <tr>
            </tr>
            </table>
            </td>
            </tr>
            </table>
            </td>
            </tr>
            </table>
            </td>
            </tr>
            </tbody>
            </table>
            </td>
            </tr>
            </tbody>
            </table>
            </td>
            </tr>
            </tbody>
            </table><!-- End -->
            </body>
            </html>
            """

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, 'html')
        message.attach(part1)
        message.attach(part2)

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
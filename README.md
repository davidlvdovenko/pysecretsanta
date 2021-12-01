# Secret Santa Python Script
A script to automatically create a Secret Santa game from a list of names and emails.
Please visit the following link for more information: https://davidlvdovenko.com/secret-santa-script/

## Introduction
The holiday season is upon us and that means lots of happy days, good food, and giving. One of the best ways to experience the “giving” part of the holiday season is by playing Secret Santa. For those that don’t know – Secret Santa is a game played in a group of people where each person, gets the name of another person (anonymously). The person you draw becomes your recipient. You now have to get that person a gift. Someone will also draw your name, however, you don’t know who it is or what they will get you – adding intrigue and a bit of mystery to the whole game… At the end of the game, you exchange gifts and try to guess who got you your gift. Your secret Santa may or may not reveal themselves to you – it’s part of the fun 🙂

However, there is one big problem with playing this game… Traditionally, the person setting up the game must draw the names for everyone and they will know all the secrets and they won’t get to play since they’d know who their Secret Santa is… What if there was a way to have a third party do this for us and keep it a mystery for everyone so that everyone could play?

Well, I have a solution. Introducing – the Secret Santa Python Script! This script will take a list of names and email addresses randomize/simulate a draw and send everyone an email notifying you who is your recipient. A modern twist on a holiday classic!

## Basic Setup
There is no GUI (Graphical User Interface) for this script, so there will be a bit of manual setup that will be required. If you know how to use a computer, I will guide you through all the steps so that you can set it up yourself.

NOTE: If you are interested in creating a GUI for this script, please reach out to me and we can work on making it a reality.

Please visit the following link to download all files needed.

https://github.com/davidlvdovenko/pysecretsanta

Once you have downloaded the zip file, extract it to find the files inside. This repository contains the following files:

- SecretSanta.exe – This is the main executable. You will run this when you have completed the setup.
- SecretSanta.py – This is the same thing as the executable – only here you can change the code to your liking. You might have to install additional packages to get this to work.
- list.csv – This is an example of a list for the program to use. I will guide you through how to make your own list in a bit.
- config.json – This is your configuration file. I will explain everything you need to do to set this up.

## List Setup
The list is simply as CSV file (Comma Seperated Value) that can be created using almost any spreadsheet editor. I will show you how to do it inside of Microsoft Excel. Open up Excel and in the first column write down the list of all the names of people participated and in the second column the associated email addresses.

Click File > Save As and make sure you name the file “list.csv” (This can be changed if you so wish, but it must also then be changed in the config.json file) and make sure it is saved as a .CSV file. This is important! Then go ahead and delete the old list.csv file and put the new one you created along side all the other files like SecretSanta.exe…

## Email Setup
For this step you can use your own SMTP server if you have that setup. If you don’t I will show you how to use Gmail to accomplish the same thing. Please follow the steps carefully.

For the sake of security, create a new email you will use just for this Secret Santa project. Once you have created the Gmail account you will want to go to: https://myaccount.google.com/lesssecureapps and enable “less secure apps”. This will allow you to use the email for raw SMTP message sending. And there we go… That is it for this section.

## Config File
Our last step is to finish editing the config file. Go ahead and open up config.json.

Please edit all the following fields:

title: This will be the title to the masterlist.txt file and subject of the email.
body: This is the first line of the email. After this line, the recipient will be listed.
body2: This is for the second line, use this for whatever you want.
body3: This is for the third line, use this for whatever you want.
signature: This is the name the email gets signed with.
listname: This specifies the name of the list file ending in .csv.
smtprelay: This specifies the email server (Use smtp.gmail.com if you are using google)
smtpport: This specifies the smtp port of the email server (Use 587 if you are using google)
user: This specifies the username of the email server (This is your email if you are using google)
password: This specifies the password for the user (Email Password)

## All Done
All configuration is complete and ready to go. Make sure all the files including the .exe file are in the same folder/directory and go ahead and launch SecretSanta.exe.

Click enter to continue. If everything goes right – you should be greated with a congratulations page at the end of the script. In the same directory you will also find the masterlist.txt file. This file contains list of all Santas and Recipients. Only open this file if absolutly needed or if someone thought they could get away with not getting someone a gift LOL.

You are free to use this script however you like. Please share with your friends and if you use any part of this code, a mention in the form of a comment would be greatly appreciated. Merry Christmas Everyone and enjoy!

## Troubleshooting
This section is for any errors that come up during the setup process or running the scripts. If you have an issue, please contact me and I will respond with a solution to the problem. Thanks!

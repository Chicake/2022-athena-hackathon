# -*- coding: utf-8 -*-
"""banktree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KDRexmicSDmrbyjWXn8J816_I5UQDxNf
"""

# Bank side: Simple demo of round-up pot

print("*Your bank app*")
roundupPot = 0
purchase = float(input("Money you spent (only in numbers): "))
roundupPot = roundupPot + (math.ceil(purchase) - purchase)
keepPurchase = input("Do you want to keep buying? yes or no: ")

import math
while keepPurchase == "yes":
  purchase = float(input("Money you spent (only in numbers): "))
  roundupPot = roundupPot + (math.ceil(purchase) - purchase)
  keepPurchase = input("Do you want to keep buying? yes or no: ")
else:
  print("Purchase finished")

# Stock info (e.g., buying environmental impact related company's stock)
environmentStockPrice = 10
sustainabilityStockPrice = 20
zeroCarbonStockPrice = 15
environmentStockName = "Company A "
sustainabilityStockName = "Company B "
zeroCarbonStockName = "Company C "

# Banktree side
print("*Opened Banktree*")

# Sign-in and Log-in
print("Sign-in page")
emailV = input("What is your email? ")
passwordV = input("What do you want for your password? ")

print("Log-in page")
email = input("Type in your email: ")
password = input("Type in your password: ")

while emailV != email and passwordV != password:
  print("Incorrect username/password")
  email = input("Type in your email: ")
  password = input("Type in your password: ")
else:
  print("Successful log-in!")

# Choices
passion = input("What are you passionate about? Type environment, sustainability or zero carbon: ")
investType = input("What investment type are you interested in? Type stock, bond, ESG index funds, micro lending and buket bryant: ") #This algorithm assumes stock
commitLength = input("How long would you like to hold the stock for? Type in 2 months, 6-12 months or 2 years: ")
if passion=="environment":
  print("You will be investing " + environmentStockName + investType + " that is worth " + str(environmentStockPrice) + " each, which is focused on " + passion + " which you are planning to hold for " + commitLength)
elif passion=="sustainability":
  print("You will be investing " + sustainabilityStockName + investType + " that is worth " + str(sustainabilityStockPrice) + " each, which is focused on " + passion + " which you are planning to hold for " + commitLength)
elif passion=="zero carbon":
  print("You will be investing " + zeroCarbonStockName + investType + " that is worth " + str(zeroCarbonStockPrice) + " each, which is focused on " + passion + " which you are planning to hold for " + commitLength)

bank = input("Choose your bank by typing in monzo, monese, revolut or starling: ")

print("*Withdrawl from " + bank + " round-up pot*")

transfer = float(input("Money you want to invest: "))

while transfer > roundupPot:
  print("Amount you entered is too large. Try again.")
  transfer = float(input("Money you want to transfer to Banktree: "))
else:
  print("Processing...")

if passion=="environment":
  print("You have successfully bought " + str(transfer/environmentStockPrice) + " " + investType + " of " + environmentStockName)
elif passion=="sustainability":
  print("You have successfully bought " + str(transfer/sustainabilityStockPrice) + " " + investType + " of " + sustainabilityStockName)
elif passion=="zero carbon":
  print("You have successfully bought " + str(transfer/zeroCarbonStockPrice) + " " + investType + " of " + zeroCarbonStockName)

print("*Legal documents appear*")
agreement = input("Do you agree to all these legal documents? yes or no: ")
if agreement=="yes":
  print("Investment completed!")
else:
  print("Investment is cancelled. Returning to home page.")
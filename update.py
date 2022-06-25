import os
import json
import randint from random

user = os.getenv("user")
action = os.getenv("action")

stats = {}
data = {}
with open('players.json') as players:
    data = json.load(players)
    players.close()

def act():
  if action == "feed":
    stats["totalfed"] += 1
    stats["currentfed"] += 1
    if user not in data["angels"]:
      data["angels"][user] = 1
    else:
      data["angels"][user] += 1
  elif action == "kill":
    stats["deathtoll"] += 1
    data["murderers"].append(user)
    generateNew()

firstNames = []
lastNames = []
def generateNew():
  stats["currentfed"] = 0
  stats["name"] = firstNames[randint(0,len(firstNames))] + lastNames[randint(0,len(lastNames))]
  
# if not a murderer then act
if user not in data["murderers"]:
  act()

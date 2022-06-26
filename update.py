import sys
import json
from random import randint

user = sys.argv[1]
action = sys.argv[2]

print(user)
print(action)

stats = {}
data = {}
with open("players.json") as players:
    data = json.load(players)
    players.close()
with open("stats.json") as sdata:
    stats = json.load(sdata)
    sdata.close()

def act():
    if action == "feed":
        stats["totalfed"] += 1
        stats["currentfed"] += 1
            
        if stats["currentfed"] > stats["highstreak"]:
            stats["highstreak"] = stats["currentfed"]
        if user not in data["angels"]:
            data["angels"][user] = 1
        else:
            data["angels"][user] += 1
    elif action == "kill":
        stats["deathtoll"] += 1
        if user in data["angels"]:
            del data["angels"][user]
        data["murderers"].append(user)
        generateNew()
    

firstNames = ["Abraham", "Muhammad ibn", "Alan", "Albert", "Albertus", "Alexander", "Alfred North", "Andrew", "Archimedes", "Aristotle", "Arthur", "Augustin-Louis", "Augustus", "Benjamin", "Bernhard", "Bertrand", "Blaise", "Brook", "Carl Friedrich", "Charles", "David", "Diophantus"]
lastNames = ["De Moivre", "Khwarizmi", "Turing", "Einstein", "Magnus", "Grothendieck", "Whitehead", "Wiles", "Cayley", "Cauchy", "De Morgan", "Banneker", "Riemann", "Russel", "Pascal", "Taylor", "Gauss", "Babbage", "Bernoulli", "Hilbert"]
def generateNew():
    stats["currentfed"] = 0
    stats["name"] = firstNames[randint(0,len(firstNames))] + " " + lastNames[randint(0,len(lastNames))]

def updateReadme():
    state = ""
    if stats["currentfed"] == 0:
        state = "emaciated"
    elif stats["currentfed"] < 6:
        state = "starving"
    elif stats["currentfed"] < 11:
        state = "recovering"
    elif stats["currentfed"] < 25:
        state = "average"
    elif stats["currentfed"] < 50:
        state = "chubby"
    elif stats["currentfed"] < 100:
        state = "obese"
    else:
        state = "sandworm"
        
    with open("README.md", "w") as f:
        f.write('''<h2 align="center">Hi, I'm Rob.</h2>

<br>
<br>

<h1 align="center">
Dilemma
</h1>

<p align="center">
This is a proof of concept, multiplayer game via github actions that can be played by submitting issues with different titles.
</p>

<p align="center">
<a href=https://github.com/foogolplex/foogolplex/issues/new?title=feed&body=just+click+submit+and+feed+they+will>feed</a>
</p>
<p align="center">
<a href=https://github.com/foogolplex/foogolplex/issues/new?title=kill&body=just+click+submit+and+they+will+die+but+be+warned+that+you+will+be+revoked+from+your+privileges>kill</a>
</p>

<p align="center">
<img src="https://github.com/foogolplex/foogolplex/blob/main/{}.gif" width="200" height="200">
</img>
</p>

<p align="center">
Name: {}
</p>

<p align="center">
Current state: {}
</p>

<p align="center">
Streak (currently fed): {}
</p>

<p align="center">
Highest streak: {}
</p>

<p align="center">
Total times fed: {}
</p>

<p align="center">
Deathtoll: {}
</p>

'''.format(state, stats["name"], state, stats["currentfed"], stats["highstreak"], stats["totalfed"], stats["deathtoll"]))
        f.write('\n| Top Feeders | Score |')
        f.write('\n| :-: | :-: |')
        for angel in data["angels"].keys():
            f.write('\n| [@'+angel+ '](https://github.com/'+ angel + '/) | ' + str(data["angels"][angel]) + ' |')
        f.write('\n\n| Murderers |')
        f.write('\n| :-: |')
        for m in data["murderers"]:
            f.write('\n| [@'+m+'](https://github.com/'+ m + '/) |')
        f.close()
# if not a murderer then act
if user not in data["murderers"]:
    act()
    updateReadme()

    # save changes
    with open("players.json", "w") as p:
        json.dump(data, p)
        p.close()
    with open("stats.json", "w") as s:
        json.dump(stats, s)
        s.close()

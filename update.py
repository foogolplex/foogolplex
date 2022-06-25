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
        if user not in data["angels"]:
            data["angels"][user] = 1
        else:
            data["angels"][user] += 1
    elif action == "kill":
        stats["deathtoll"] += 1
        data["murderers"].append(user)
        generateNew()

firstNames = ["Abraham", "Muhumammad ibn", "Alan", "Albert", "Albertus", "Alexander", "Alfred North", "Andrew", "Archimedes", "Aristotle", "Arthur", "Augustin-Louis", "Augustus", "Benjamin", "Bernhard", "Bertrand", "Blaise", "Brook", "Carl Friedrich", "Charles", "David", "Diophantus"]
lastNames = ["De Moivre", "Khwarizmi", "Turing", "Einstein", "Magnus", "Grothendieck", "Whitehead", "Wiles", "Cayley", "Cauchy", "De Morgan", "Banneker", "Riemann", "Russel", "Pascal", "Taylor", "Gauss", "Babbage", "Bernoulli", "Hilbert"]
def generateNew():
    stats["currentfed"] = 0
    stats["name"] = firstNames[randint(0,len(firstNames))] + lastNames[randint(0,len(lastNames))]

def updateReadme():
    with open("README.md", "w") as f:
        f.write("""[feed](https://github.com/foogolplex/foogolplex/issues/new?title=feed&body=just+click+submit+and+feed+they+will)\n
[kill](https://github.com/foogolplex/foogolplex/issues/new?title=kill&body=just+click+submit+and+they+will+die+but+be+warned+that+you+will+be+revoked+from+your+privileges)
""")
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

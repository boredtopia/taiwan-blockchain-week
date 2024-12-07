import json
 
START_ID = 1
TOTAL_SUPPLY = 10_000

NAME = "Boredtopia Taiwan Blockchain Week Souvenir"
DESC = "Celebrate your journey into the world of Web3 with the exclusive “Boredtopia Taiwan Blockchain Week Souvenir” NFT! Minted on the Kaia Chain, this digital collectible is a special keepsake for attendees of the Taiwan Blockchain Week 2024."
IMG = "https://boredtopia.github.io/taiwan-blockchain-week/asset.png"
ATTRS = [
    #{
    #  "trait_type": "Edition",
    #  "value": "Special"
    #},
]
#ENGINE = "Bored Town Launchpad"

tpl = {
  "name": "<FILL-IN-LOOP>",
  "description": DESC,
  "image": IMG,
  "attributes": ATTRS,
  #"compiler": ENGINE,
}

for index in range(0, TOTAL_SUPPLY):
    id = START_ID + index
    tpl["name"] = "{} #{}".format(NAME, id)
    with open("../docs/json/{}.json".format(id), "w") as f:
        json.dump(tpl, f)

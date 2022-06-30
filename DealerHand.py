import random
# deck setup
deck = range(2, 11)
playerHand = []
dealerHand = []
playerIn = True
dealerIn = True
bustCheck = 2
faces = ['J', 'Q', 'K', 'A']
newdeck = []
for i in range(2, 11):
    for j in range(4):
        newdeck.append(i)
for i in faces:
    for j in range(4):
        newdeck.append(i)
print(list(newdeck))

# deal card
def dealCard(personHand):
    card = random.choice(newdeck)
    personHand.append(card)
    newdeck.remove(card)

def calcHand(personHand):
    handValue = 0
    faceCards = ['J', 'Q', 'K']
    length = len(personHand)
    i=0
    while i <length:
        card = personHand[i]
        if card in deck:
            handValue = handValue + card
        elif card in faceCards:
            handValue = handValue + 10
        else:
            if handValue < 11:
                handValue = handValue + 11
            else:
                handValue = handValue + 1
        i=i+1
    return handValue

# checking if winner
def checkBustPlayer():
    if calcHand(playerHand) > 21:
        return 0
    else:
        return 1

def checkBustDealer():
    if calcHand(dealerHand) > 21:
        return 0
    else:
        return 1

def cardFormat(personHand):
    length = len(personHand)
    i = 0
    while i<length:
        valueStr = str(personHand[i])
        print("*****")
        print("*",valueStr, "*")
        print("*****")
        print("--------")
        i=i+1
    strValue = str(calcHand(personHand))
    print("current hand value:", strValue)

def play():
    for i in range(2):
        dealCard(playerHand)
    dealCard(dealerHand)
    print("PLAYER HAND: ")
    cardFormat(playerHand)
    print("DEALER HAND: ")
    cardFormat(dealerHand)

    hitStay = input("1. Hit\n2. Stay\n Would you like to hit or stay: ")
    while hitStay!=2 or playerBust==0:
        dealCard(playerHand)
        print("PLAYER HAND: ")
        cardFormat(playerHand)
        print("DEALER HAND: ")
        cardFormat(dealerHand)
        playerBust = checkBustPlayer()
        if playerBust == 0:
            playerHandValue = str(calcHand(playerHand))
            print("PLAYER HAS BUSTED:", playerHandValue, "DEALER WINS :(")
            break
        hitStay = input("1. Hit\n2. Stay\n Would you like to hit or stay: ")

    if playerBust==1:
        playerValue = calcHand(playerHand)
        dealerValue = calcHand(dealerHand)
        while dealerValue<playerValue:
            dealCard(dealerHand)
            dealerValue = calcHand(dealerHand)
        if checkBustDealer()==0:
            dealerHandValue = str(calcHand(dealerHand))
            print("DEALER HAS BUSTED:", dealerHandValue, "PLAYER WINS!!!!")

play()
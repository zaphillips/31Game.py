# Zachary Phillips
# 31Test.py

from graphics import *
from buttonFunction import *
from deck import Deck
import time

def main():

    controlDeck = Deck()
    controlDeck.shuffle()

    width = 1200
    height = 800
    win = GraphWin('Scat Prototype', width, height)

    controlComputerDeck(width, height, win)

    deck = Image(Point(width/2 + 80, height/2), 'red_back_2.png')
    deck.draw(win)

    discardCard = [controlDeck.draw()]
    discardSuit, discardName, discardValue = discardCard[0].split()
    discard = Image(Point(width/2 - 80, height/2 ), discardName + discardSuit + ".png")
    discard.draw(win)

    decisionDeck = []
    playerDeck = []
    playerDeckImages = []

    for n in range(1, 4):
        card = controlDeck.draw()
        playerDeck.append(card)
        playerSuit, playerName, playerValue = card.split()
        playerCard = drawCard(width, height, playerSuit, playerName, 'player', n)
        playerDeckImages.append(playerCard)
        playerDeckImages[n-1].draw(win)
        print("You drew a " + playerName + " of " + playerSuit + "s with a value of " + playerValue)

    print(playerDeck)

    computerDeck = []

    for n in range(1, 4):
        card = controlDeck.draw()
        computerDeck.append(card)
        computerSuit, computerName, computerValue = card.split()
        print("The computer drew a " + computerName + " of " + computerSuit + "s with a value of " + computerValue)

    print(computerDeck)

    playerDeckText = Text(Point(playerDeckImages[0].getAnchor().getX(), 62.5), 'Player Deck')
    playerDeckText.setStyle('bold')
    playerDeckText.setSize(16)

    playerDeckText.draw(win)

    knockButton = Rectangle(Point(playerDeckImages[0].getAnchor().getX() - 62.5, height - 90), Point(playerDeckImages[0].getAnchor().getX() + 62.5, height - 65))
    knockButton.setFill('gray')

    knockButtonText = Text(knockButton.getCenter(), 'Knock')
    knockButtonText.setStyle('bold')

    play = True

    while play:

        knockButton.draw(win)
        knockButtonText.draw(win)

        playerClick = win.getMouse()

        if buttonClicked(playerClick, knockButton):
            quit()
        else:
            knockButtonText.undraw()
            knockButton.undraw()


        if imageClicked(playerClick, discard):
            discard.undraw()
            outline = createOutline(discard)
            outline.draw(win)
            discard.draw(win)
            playerClick = win.getMouse()
            while (imageClicked(playerClick, playerDeckImages[0])) == False and (imageClicked(playerClick, playerDeckImages[1])) == False and (imageClicked(playerClick, playerDeckImages[2])) == False:
                playerClick = win.checkMouse()
            if imageClicked(playerClick, playerDeckImages[0]):
                decisionDeck.append(discardCard[-1])
                discardCard[-1] = playerDeck[0]
                discardSuit, discardName, discardValue = discardCard[-1].split()
                discard = Image(Point(width / 2 - 80, height / 2), discardName + discardSuit + ".png")
                discard.draw(win)
                playerDeck[0] = decisionDeck[0]
                card = playerDeck[0]
                playerSuit, playerName, playerValue = card.split()
                playerCard = drawCard(width, height, playerSuit, playerName, 'player', 1)
                playerDeckImages[0] = playerCard
                playerDeckImages[0].draw(win)
                decisionDeck = []
            if imageClicked(playerClick, playerDeckImages[1]):
                decisionDeck.append(discardCard[-1])
                discardCard[-1] = playerDeck[1]
                discardSuit, discardName, discardValue = discardCard[-1].split()
                discard = Image(Point(width / 2 - 80, height / 2), discardName + discardSuit + ".png")
                discard.draw(win)
                playerDeck[1] = decisionDeck[0]
                card = playerDeck[1]
                playerSuit, playerName, playerValue = card.split()
                playerCard = drawCard(width, height, playerSuit, playerName, 'player', 2)
                playerDeckImages[1] = playerCard
                playerDeckImages[1].draw(win)
                decisionDeck = []
            if imageClicked(playerClick, playerDeckImages[2]):
                decisionDeck.append(discardCard[-1])
                discardCard[-1] = playerDeck[2]
                discardSuit, discardName, discardValue = discardCard[-1].split()
                discard = Image(Point(width / 2 - 80, height / 2), discardName + discardSuit + ".png")
                discard.draw(win)
                playerDeck[2] = decisionDeck[0]
                card = playerDeck[2]
                playerSuit, playerName, playerValue = card.split()
                playerCard = drawCard(width, height, playerSuit, playerName, 'player', 3)
                playerDeckImages[2] = playerCard
                playerDeckImages[2].draw(win)
                decisionDeck = []
            outline.undraw()
        if imageClicked(playerClick, deck):
            deck.undraw()
            outline = createOutline(deck)
            outline.draw(win)
            deck.draw(win)
            playerClick = win.getMouse()
            while (imageClicked(playerClick, playerDeckImages[0])) == False and (imageClicked(playerClick, playerDeckImages[1])) == False and (imageClicked(playerClick, playerDeckImages[2])) == False and imageClicked(playerClick, discard) == False:
                playerClick = win.checkMouse()
            if imageClicked(playerClick, playerDeckImages[0]):
                decisionDeck.append(controlDeck.draw())
                print(decisionDeck)
                discardCard.append(playerDeck[0])
                discardSuit, discardName, discardValue = discardCard[-1].split()
                discard = Image(Point(width / 2 - 80, height / 2), discardName + discardSuit + ".png")
                discard.draw(win)
                playerDeck[0] = decisionDeck[0]
                card = playerDeck[0]
                playerSuit, playerName, playerValue = card.split()
                playerCard = drawCard(width, height, playerSuit, playerName, 'player', 1)
                playerDeckImages[0] = playerCard
                playerDeckImages[0].draw(win)
                decisionDeck = []
            if imageClicked(playerClick, playerDeckImages[1]):
                decisionDeck.append(controlDeck.draw())
                print(decisionDeck)
                discardCard.append(playerDeck[1])
                discardSuit, discardName, discardValue = discardCard[-1].split()
                discard = Image(Point(width / 2 - 80, height / 2), discardName + discardSuit + ".png")
                discard.draw(win)
                playerDeck[1] = decisionDeck[0]
                card = playerDeck[1]
                playerSuit, playerName, playerValue = card.split()
                playerCard = drawCard(width, height, playerSuit, playerName, 'player', 2)
                playerDeckImages[1] = playerCard
                playerDeckImages[1].draw(win)
                decisionDeck = []
            if imageClicked(playerClick, playerDeckImages[2]):
                decisionDeck.append(controlDeck.draw())
                print(decisionDeck)
                discardCard.append(playerDeck[2])
                discardSuit, discardName, discardValue = discardCard[-1].split()
                discard = Image(Point(width / 2 - 80, height / 2), discardName + discardSuit + ".png")
                discard.draw(win)
                playerDeck[2] = decisionDeck[0]
                card = playerDeck[2]
                playerSuit, playerName, playerValue = card.split()
                playerCard = drawCard(width, height, playerSuit, playerName, 'player', 3)
                playerDeckImages[2] = playerCard
                playerDeckImages[2].draw(win)
                decisionDeck = []
            if imageClicked(playerClick, discard):
                decisionDeck.append(controlDeck.draw())
                print(decisionDeck)
                discardCard.append(decisionDeck[0])
                discardSuit, discardName, discardValue = discardCard[-1].split()
                discard = Image(Point(width / 2 - 80, height / 2), discardName + discardSuit + ".png")
                discard.draw(win)
                decisionDeck = []

            outline.undraw()

    win.getMouse()

    win.close()

def drawCard(width: int, height: int, suit: str, name: str, player: str, cardNumber: int):
    if player == 'player':
        if cardNumber == 1:
            return Image(Point(100, height/4), name + suit + ".png")
        elif cardNumber == 2:
            return Image(Point(100, (height / 2)), name + suit + ".png")
        elif cardNumber == 3:
            return Image(Point(100, (height / 4) * 3), name + suit + ".png")

def controlComputerDeck(width: int, height: int, win: GraphWin):
    computerCard1 = Image(Point(width - 100, height / 4), 'red_back_2.png')
    computerCard2 = Image(Point(width - 100, (height / 2)), 'red_back_2.png')
    computerCard3 = Image(Point(width - 100, (height / 4) * 3), 'red_back_2.png')
    computerDeck = Text(Point(computerCard1.getAnchor().getX(), 62.5), 'Computer Deck')
    computerDeck.setStyle('bold')
    computerDeck.setSize(16)
    computerCard1.draw(win)
    computerCard2.draw(win)
    computerCard3.draw(win)
    computerDeck.draw(win)

def createOutline(image: Image)-> Rectangle:
    P1x = image.getAnchor().getX() - 63.5
    P1y = image.getAnchor().getY() - 96.5
    P2x = image.getAnchor().getX() + 63.5
    P2y = image.getAnchor().getY() + 96.5
    Outline = Rectangle(Point(P1x, P1y), Point(P2x, P2y))
    Outline.setOutline('blue')
    return Outline

def getHandValue(hand: list)-> int:
    Suit1, Name1, Value1 = hand[0].split()
    Suit2, Name2, Value2 = hand[1].split()
    Suit3, Name3, Value3 = hand[2].split()
    if Suit1 == Suit2 and Suit1 == Suit3:
        return int(Value1) + int(Value2) + int(Value3)
    elif Suit1 != Suit2 and Suit1 != Suit3 and Suit2 != Suit3:
        if int(Value1) > int(Value2) and int(Value1) > int(Value3):
            return int(Value1)
        if int(Value2) > int(Value1) and int(Value2) > int(Value3):
            return int(Value2)
        if int(Value3) > int(Value1) and int(Value3) > int(Value2):
            return int(Value3)
    elif Suit1 == Suit2:
        if (int(Value1) + int(Value2)) > int(Value3):
            return int(Value1) + int(Value2)
        else:
            return int(Value3)
    elif Suit1 == Suit3:
        if (int(Value1) + int(Value3)) > int(Value2):
            return int(Value1) + int(Value3)
        else:
            return int(Value2)
    elif Suit2 == Suit3:
        if (int(Value2) + int(Value3)) > int(Value1):
            return int(Value2) + int(Value3)
        else:
            return int(Value1)

if __name__ == '__main__':
    main()
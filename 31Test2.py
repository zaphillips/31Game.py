# Zachary Phillips
# 31Test2.py

from graphics import *
from buttonFunction import *
from deck import Deck
import time
import random

def main():

    width = 1200
    height = 800
    win = GraphWin('31 Prototype', width, height)

    winnerText = Text(Point(width/2, 200), '')
    winnerText.setStyle('bold')
    winnerText.setSize(16)

    scoreText = Text(Point(width/2, 220), '')
    scoreText.setStyle('bold')
    scoreText.setSize(15)

    quitText = Text(Point(width/2, 100), 'Press enter to play again or press q to quit.')
    quitText.setStyle('bold')
    quitText.setFill('red')
    quitText.setSize(16)

    playing = True

    while playing:
        playerDeck, computerDeck = play(width, height, win)
        computerDeckImages = revealComputerHand(width, height, computerDeck)
        for card in computerDeckImages:
            card.draw(win)
            time.sleep(0.5)
        scoreText.setText(str(getHandValue(playerDeck)) + '     vs.     ' + str(getHandValue(computerDeck)))
        scoreText.draw(win)
        winner = getWinner(playerDeck, computerDeck)
        winnerText.setText(winner)
        winnerText.draw(win)
        quitText.draw(win)

        userInput = win.checkKey()

        while userInput not in ['Return', 'q']:
            userInput = win.checkKey()
        if userInput == 'q':
            playing = False
        else:
            playing = True

        scoreText.undraw()
        winnerText.undraw()
        quitText.undraw()

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
    if Suit1 != Suit2 and Suit1 != Suit3 and Suit2 != Suit3:
        if int(Value1) >= int(Value2) and int(Value1) >= int(Value3):
            return int(Value1)
        if int(Value2) >= int(Value1) and int(Value2) >= int(Value3):
            return int(Value2)
        if int(Value3) >= int(Value1) and int(Value3) >= int(Value2):
            return int(Value3)
    if Suit1 == Suit2:
        if (int(Value1) + int(Value2)) > int(Value3):
            return int(Value1) + int(Value2)
        else:
            return int(Value3)
    if Suit1 == Suit3:
        if (int(Value1) + int(Value3)) > int(Value2):
            return int(Value1) + int(Value3)
        else:
            return int(Value2)
    if Suit2 == Suit3:
        if (int(Value2) + int(Value3)) > int(Value1):
            return int(Value2) + int(Value3)
        else:
            return int(Value1)

def getWinner(playerDeck: list, computerDeck: list )-> str:
    playerValue = getHandValue(playerDeck)
    computerValue = getHandValue(computerDeck)
    if playerValue > computerValue:
        return 'You are the winner!'
    elif playerValue < computerValue:
        return 'Better luck next time, the computer is the winner.'
    else:
        return "It's a tie."

def revealComputerHand(width: int, height: int, computerDeck: list):
    card1Suit, card1Name, card1Value = computerDeck[0].split()
    card2Suit, card2Name, card2Value = computerDeck[1].split()
    card3Suit, card3Name, card3Value = computerDeck[2].split()
    computerCard1 = Image(Point(width - 100, height / 4), card1Name + card1Suit + ".png")
    computerCard2 = Image(Point(width - 100, (height / 2)), card2Name + card2Suit + ".png")
    computerCard3 = Image(Point(width - 100, (height / 4) * 3), card3Name + card3Suit + ".png")
    return [computerCard1, computerCard2, computerCard3]

def play(width: int, height: int, win: GraphWin):
    controlDeck = Deck()
    controlDeck.shuffle()
    controlComputerDeck(width, height, win)

    deck = Image(Point(width / 2 + 80, height / 2), 'red_back_2.png')
    deck.draw(win)

    discardCard = [controlDeck.draw()]
    discardSuit, discardName, discardValue = discardCard[0].split()
    discard = Image(Point(width / 2 - 80, height / 2), discardName + discardSuit + ".png")
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
        playerDeckImages[n - 1].draw(win)
        print("You drew a " + playerName + " of " + playerSuit + "s with a value of " + playerValue)

    print(playerDeck)

    computerDeck = []

    for n in range(1, 4):
        card = controlDeck.draw()
        computerDeck.append(card)
        computerSuit, computerName, computerValue = card.split()
        print("The computer drew a " + computerName + " of " + computerSuit + "s with a value of " + computerValue)

    print(computerDeck)

    decisionDeckImage = Image(Point(width/2, discard.getAnchor().getY() + 200), 'placeholder.png')

    playerDeckText = Text(Point(playerDeckImages[0].getAnchor().getX(), 62.5), 'Player Deck')
    playerDeckText.setStyle('bold')
    playerDeckText.setSize(16)

    playerDeckText.draw(win)

    knockButton = Rectangle(Point(playerDeckImages[0].getAnchor().getX() - 62.5, height - 90),
                            Point(playerDeckImages[0].getAnchor().getX() + 62.5, height - 65))
    knockButton.setFill('gray')

    knockButtonText = Text(knockButton.getCenter(), 'Knock')
    knockButtonText.setStyle('bold')

    while True:

        if controlDeck.deck == []:
            return playerDeck, computerDeck

        knockButton.draw(win)
        knockButtonText.draw(win)

        playerClick = win.getMouse()

        if buttonClicked(playerClick, knockButton):
            return playerDeck, computerDeck
        else:
            knockButtonText.undraw()
            knockButton.undraw()

        computerTurn = False

        if imageClicked(playerClick, discard):
            computerTurn = True
            discard.undraw()
            outline = createOutline(discard)
            outline.draw(win)
            discard.draw(win)
            playerClick = win.getMouse()
            while (imageClicked(playerClick, playerDeckImages[0])) == False and (
            imageClicked(playerClick, playerDeckImages[1])) == False and (
            imageClicked(playerClick, playerDeckImages[2])) == False:
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
            elif imageClicked(playerClick, playerDeckImages[1]):
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
            elif imageClicked(playerClick, playerDeckImages[2]):
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
            computerTurn = True
            deck.undraw()
            outline = createOutline(deck)
            outline.draw(win)
            deck.draw(win)
            playerDraw = controlDeck.draw()
            drawSuit, drawName, drawValue = playerDraw.split()
            decisionDeckImage = Image(Point(width / 2, discard.getAnchor().getY() + 200), drawName + drawSuit + '.png')
            decisionDeckImage.draw(win)
            playerClick = win.getMouse()
            while (imageClicked(playerClick, playerDeckImages[0])) == False and (
            imageClicked(playerClick, playerDeckImages[1])) == False and (
            imageClicked(playerClick, playerDeckImages[2])) == False and imageClicked(playerClick, discard) == False:
                playerClick = win.checkMouse()
            if imageClicked(playerClick, playerDeckImages[0]):
                decisionDeckImage.undraw()
                decisionDeck.append(playerDraw)
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
            elif imageClicked(playerClick, playerDeckImages[1]):
                decisionDeckImage.undraw()
                decisionDeck.append(playerDraw)
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
            elif imageClicked(playerClick, playerDeckImages[2]):
                decisionDeckImage.undraw()
                decisionDeck.append(playerDraw)
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
            elif imageClicked(playerClick, discard):
                decisionDeckImage.undraw()
                decisionDeck.append(playerDraw)
                print(decisionDeck)
                discardCard.append(decisionDeck[0])
                discardSuit, discardName, discardValue = discardCard[-1].split()
                discard = Image(Point(width / 2 - 80, height / 2), discardName + discardSuit + ".png")
                discard.draw(win)
                decisionDeck = []

            outline.undraw()

        if computerTurn:

            if controlDeck.deck == []:
                return playerDeck, computerDeck

            computerTurnText = Text(Point(width/2, height - 50), 'The computer is thinking ')
            computerTurnText.setSize(14)
            computerTurnText.draw(win)
            sleepTime = random.randint(2, 3)
            for n in range(sleepTime):
                time.sleep(1)
                computerTurnUpdate = computerTurnText.getText() + ' .'
                computerTurnText.setText(computerTurnUpdate)

            computerTurnText.undraw()

            if getHandValue(computerDeck) == 31:
                computerTurnText.setText("The computer has knocked!")
                computerTurnText.draw(win)
                time.sleep(1)
                computerTurnText.undraw()
                return playerDeck, computerDeck
            if getHandValue(computerDeck) > 20:
                if random.randint(1, 20) == 10:
                    computerTurnText.setText("The computer has knocked!")
                    computerTurnText.draw(win)
                    time.sleep(1)
                    computerTurnText.undraw()
                    return playerDeck, computerDeck
            if getHandValue(computerDeck) < 20:
                if random.randint(1, 50) == 25:
                    computerTurnText.setText("The computer has knocked!")
                    computerTurnText.draw(win)
                    time.sleep(1)
                    computerTurnText.undraw()
                    return playerDeck, computerDeck
            discardaltList1 = [discardCard[-1], computerDeck[1], computerDeck[2]]
            discardaltList2 = [computerDeck[0], discardCard[-1], computerDeck[2]]
            discardaltList3 = [computerDeck[0], computerDeck[1], discardCard[-1]]
            discardaltList1Value = getHandValue(discardaltList1)
            discardaltList2Value = getHandValue(discardaltList2)
            discardaltList3Value = getHandValue(discardaltList3)
            print(str(discardaltList1Value) + ' ' + str(discardaltList2Value) + ' ' + str(discardaltList3Value))
            print('Hands: ' + str(discardaltList1) + ' ' + str(discardaltList2) + ' ' + str(discardaltList3))
            if discardaltList1Value > getHandValue(computerDeck) or discardaltList2Value > getHandValue(computerDeck) or discardaltList3Value > getHandValue(computerDeck):
                if discardaltList1Value >= discardaltList2Value and discardaltList1Value >= discardaltList3Value:
                    decisionDeck.append(discardCard[-1])
                    discardCard[-1] = computerDeck[0]
                    discardSuit, discardName, discardValue = discardCard[-1].split()
                    discard = Image(Point(width / 2 - 80, height / 2), discardName + discardSuit + ".png")
                    discard.draw(win)
                    computerDeck[0] = decisionDeck[0]
                    decisionDeck = []
                elif discardaltList2Value >= discardaltList1Value and discardaltList2Value >= discardaltList3Value:
                    decisionDeck.append(discardCard[-1])
                    discardCard[-1] = computerDeck[1]
                    discardSuit, discardName, discardValue = discardCard[-1].split()
                    discard = Image(Point(width / 2 - 80, height / 2), discardName + discardSuit + ".png")
                    discard.draw(win)
                    computerDeck[1] = decisionDeck[0]
                    decisionDeck = []
                elif discardaltList3Value >= discardaltList1Value and discardaltList3Value >= discardaltList2Value:
                    decisionDeck.append(discardCard[-1])
                    discardCard[-1] = computerDeck[2]
                    discardSuit, discardName, discardValue = discardCard[-1].split()
                    discard = Image(Point(width / 2 - 80, height / 2), discardName + discardSuit + ".png")
                    discard.draw(win)
                    computerDeck[2] = decisionDeck[0]
                    decisionDeck = []
            else:
                computerDraw = controlDeck.draw()
                drawaltList1 = [computerDraw, computerDeck[1], computerDeck[2]]
                drawaltList2 = [computerDeck[0], computerDraw, computerDeck[2]]
                drawaltList3 = [computerDeck[0], computerDeck[1], computerDraw]
                drawaltList1Value = getHandValue(drawaltList1)
                drawaltList2Value = getHandValue(drawaltList2)
                drawaltList3Value = getHandValue(drawaltList3)
                print(str(drawaltList1Value) + " " + str(drawaltList2Value) + ' ' + str(drawaltList3Value))
                print('Hands: ' + str(drawaltList1) + " " + str(drawaltList2) + ' ' + str(drawaltList3))
                if drawaltList1Value > getHandValue(computerDeck) or drawaltList2Value > getHandValue(computerDeck) or drawaltList3Value > getHandValue(computerDeck):
                    if drawaltList1Value >= drawaltList2Value and drawaltList1Value >= drawaltList3Value:
                        discardCard.append(computerDeck[0])
                        discardSuit, discardName, discardValue = discardCard[-1].split()
                        discard = Image(Point(width / 2 - 80, height / 2), discardName + discardSuit + ".png")
                        discard.draw(win)
                        computerDeck[0] = computerDraw
                        decisionDeck = []
                    elif drawaltList2Value >= drawaltList1Value and drawaltList2Value >= drawaltList3Value:
                        discardCard.append(computerDeck[1])
                        discardSuit, discardName, discardValue = discardCard[-1].split()
                        discard = Image(Point(width / 2 - 80, height / 2), discardName + discardSuit + ".png")
                        discard.draw(win)
                        computerDeck[1] = computerDraw
                        decisionDeck = []
                    elif drawaltList3Value >= drawaltList1Value and drawaltList3Value >= drawaltList2Value:
                        discardCard.append(computerDeck[2])
                        discardSuit, discardName, discardValue = discardCard[-1].split()
                        discard = Image(Point(width / 2 - 80, height / 2), discardName + discardSuit + ".png")
                        discard.draw(win)
                        computerDeck[2] = computerDraw
                        decisionDeck = []
                else:
                    discardCard.append(computerDraw)
                    discardSuit, discardName, discardValue = discardCard[-1].split()
                    discard = Image(Point(width / 2 - 80, height / 2), discardName + discardSuit + ".png")
                    discard.draw(win)
                    decisionDeck = []

if __name__ == '__main__':
    main()
from graphics import *

def buttonClicked(p: Point, rect: Rectangle)-> bool:
    if p:
        px = p.getX()
        py = p.getY()
        P1x = rect.getP1().getX()
        P1y = rect.getP1().getY()
        P2x = rect.getP2().getX()
        P2y = rect.getP2().getY()
        if (P1x <= px <= P2x) and (P1y <= py <= P2y):
            return True
        else:
            return False
    else:
        return False

def imageClicked(p: Point, image: Image)-> bool:
    if p:
        px = p.getX()
        py = p.getY()
        P1x = image.getAnchor().getX() - 62.5
        P1y = image.getAnchor().getY() - 95.5
        P2x = image.getAnchor().getX() + 62.5
        P2y = image.getAnchor().getY() + 95.5
        if (P1x <= px <= P2x) and (P1y <= py <= P2y):
            return True
        else:
            return False
    else:
        return False
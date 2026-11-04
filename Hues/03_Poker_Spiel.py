import random 

def ziehe_hand(deck, anzahl):
    hand = []
    for i in range(anzahl):
        index = random.randint(0, len(deck)-1-i)
        hand.append(deck[index])
        deck[index] = deck[len(deck)-1-i]
        deck[len(deck)-1-i] = hand[i]
    return hand

def get_Werte(karten, werte):
    ergebnis = []
    for k in karten:
        ergebnis.append(k%werte)
    return ergebnis

def get_Farben(gesamt_karten,karten, farben):
    ergebnis = []
    bereich = gesamt_karten//farben
    for k in karten:
        ergebnis.append(k//bereich)
    return ergebnis

def check_Paar(hand):
    for x in hand:
        for y in hand:
            if x == y:
                break
            if x%13 == y%13:
                return True
    return False

def check_gleiche_Karten(werte):
    gleiche = []
    ref = 0
    zaehler = 0

    for i in range(len(werte)):
        if werte[i] == werte[ref]:
            zaehler += 1
        else:
            if zaehler > 1:
                gleiche.append(zaehler)
            zaehler = 1
            ref = i    

    if zaehler > 1:
        gleiche.append(zaehler)
    
        
    return gleiche
        


def check_Strasse(werte):
    

    if werte == [0, 1, 2, 3, 12]:      
        return [True, False]           

    for i in range(len(werte)):
        if(werte[0] != werte[i]-i):
            return [False, False]

    if(werte[len(werte)-1] == 12):
        return [True, True]
    return [True, False]

def check_flush(farben):
    
    for i in range(len(farben)):
        if(farben[0] != farben[i]):
            return False
    return True

def rate_hand(hand):
    farben = get_Farben(52,hand,4)
    farben.sort()
    werte = get_Werte(hand, 13)
    werte.sort()

    flush = check_flush(farben)
    straight = check_Strasse(werte)

    if(flush == True):
        if(straight[0] == True):
            if(straight[1] == True):
                return 0
            return 1

    gleiche_Karten = check_gleiche_Karten(werte)

    if(4 in gleiche_Karten):
        return 2

    if (3 in gleiche_Karten) and (2 in gleiche_Karten):
        return 3

    if flush == True:
        return 4

    if straight[0] == True:
        return 5

    if 3 in gleiche_Karten:
        return 6

    if 2 in gleiche_Karten:
        if len(gleiche_Karten) > 1:
            return 7
        return 8
    return 9

def init_stats():
    result = {}
    for i in range(10):
        result[i] = 0
    return result

def sim_hande(times):
    pokerdeck = list(range(52))
    stats = init_stats()
    for _ in range(times):
        hand = ziehe_hand(pokerdeck, 5)
        ergebnis_hand = rate_hand(hand)
        stats[ergebnis_hand] += 1

    return stats



if __name__ == "__main__":
    
    # pokerdeck = list(range(52))
    # gezogene_hand = ziehe_hand(pokerdeck, 5)
    # Karten = []
    # for e in gezogene_hand:
    #     wert = e%13
    #     farbe = e // 13
    #     Karten.append([farbe,wert])
    # print(gezogene_hand)
    # print(Karten)
    # print(check_Paar(gezogene_hand))
    # print(check_Strasse([13,3,4,2,1]))
    # print(check_flush([0,1,2,3,4]))
    # print(check_gleiche_Karten([0,14,26,13,1]))
    # print(rate_hand([0,0,0,2,2]))
    times = int(input("Wie oft soll simuliert werden?"))
    stats = sim_hande(times)
    print(stats)

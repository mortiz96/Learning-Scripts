import random
import collections
#comment
PALOS = ['S', 'H', 'D', 'C']
VALORES = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def create_deck():
    deck = []
    for palo in PALOS:
        for valor in VALORES:
            deck.append((palo, valor)) #Retorna una tupla de PALO, VALOR
    return deck


def draw(deck, hand_size):
    mano = random.sample(deck, hand_size)
    return mano

#Escalera de color
def straight_flush(hand):
    is_flush=False
    suit=[]

    for card in hand:
        suit.append(card[0])

    c_straight_flush=dict(collections.Counter(suit))
    
    if any(x in c_straight_flush.values() for x in [5]):
        is_flush=True
        
    return is_flush

#Escalera
def straight(deck, runs):
    s_count=0
    s_r_count=0

    for hand in deck:
        values=[]

        for card in hand:
            values.append(card[1])

        for n, i in enumerate(values):
            if i in ['J']:
                values[n]='11'
            if i in ['Q']:
                values[n]='12'
            if i in ['K']:
                values[n]='13'
            if i in ['Ace']:
                values[n]='1'

        for n, i in enumerate(values): #Convertir los valores a int
            values[n]=int(values[n])

        values_sorted=sorted(values)
        
        straight=True #Se asume que es escalera
        flush=False#Se asume que no es color

        for i in range(len(values_sorted)-1):
            if values_sorted[i]+1!=values_sorted[i+1]:
                straight=False
        
        if straight==True:
            s_count+=1
            #print(hand)

            flush=straight_flush(hand)#Verificar que si la escalera es de color o no
            if flush==True:
                s_r_count+=1
                #print(hand)

    straight_p=s_count/runs
    straight_F_p=s_r_count/runs   

    print(f'Straight: {s_count}, P(Straight)= {straight_p}\n')
    print(f'Straight Flush: {s_r_count}, P(Straight Flush)= {straight_F_p}\n')


def royal_flush(hand):
    values=[]
    royal_flush=False

    for card in hand:
        values.append(card[1])

    if all(x in values for x in ['J', 'Q','K','Ace','10']):
        royal_flush=True

    return royal_flush

                
            
def flush(deck, runs):
    flush=0
    r_flush=0

    for hand in deck:
        suit=[]
        for card in hand:
            suit.append(card[0])
        
        counter_suit=dict(collections.Counter(suit))

        if any(x in counter_suit.values() for x in [5]): #5 cards of the same suit
            flush+=1
            #print(hand)
            royal=royal_flush(hand)
            if royal==True:
                r_flush+=1
                #print(hand)

    r_flush_p=r_flush/runs
    flush_p=flush/runs

    print(f'Flush: {flush}, P(Flush)= {flush_p}\n')
    print(f'Royal Flush: {r_flush}, P(Royal Flush)= {r_flush_p}\n')



def clones(deck, runs):
    pairs, tok, fok, full, two_pairs = 0,0,0,0,0
    #tok: Three of a kind
    #fok: Four of a kind

    for hand in deck:# Analizar cada mano dentro de la lista draw_results

        values = []# Lista para analizar los valores de cada carta
        for card in hand:#Análisis de cada carta dentro de cada mano
            values.append(card[1]) #Accede al segundo elemento de la tupla 

        counter = dict(collections.Counter(values)) #key: "values" 

        #Full House
        if all(x in counter.values() for x in [3, 2]):
            full+=1
            #print(hand)

        #pairs
        if any(x in counter.values() for x in [2]):
            pairs+=1
            #print(hand)
            

        #Three of a kind
        if any(x in counter.values() for x in [3]):
            tok+=1
            #print(hand)

        #Four of a kind
        if any(x in counter.values() for x in [4]):
            fok+=1
            #print(hand)

        #Two pairs
        if pairs==2:
            two_pairs+=1
            #print(hand)
                   
    tok_p=tok/runs
    fok_p=fok/runs
    pair_p = pairs / runs
    two_pairs_p=two_pairs/runs
    full_p=full/runs

    print(f'Three of a kind: {tok}, P(Three of a kind)= {tok_p}\n')
    print(f'Four of a kind: {fok}, P(four of a kind)= {fok_p}\n')
    print(f'Pairs: {pairs}, P(pairs)= {pair_p}\n')
    print(f'Two Pairs: {two_pairs}, P(Two pairs)= {two_pairs_p}\n')
    print(f'Full: {full}, P(Full)= {full_p}\n')



def main(cards_amount, runs):
    deck = create_deck()
    draw_results = [] #es una lista de listas

    for _ in range(runs):
        hand = draw(deck, cards_amount)
        draw_results.append(hand)

    print(f'\nIf **{cards_amount}** cards are drawn:\n')

    clones(draw_results, runs)
    flush(draw_results,runs)
    straight(draw_results, runs)

    print(f'The experiment was run {runs} times\n')
    print('https://www.cardplayer.com/rules-of-poker/hand-rankings')


if __name__ == '__main__':
    hand_size = int(input('Cards drawn: '))
    runs = int(input('Experiment runs: '))

    main(hand_size, runs)
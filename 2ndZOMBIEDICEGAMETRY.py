import time
#iekshaa suuta itemus, aaraa met indeksus


#3dice rolling every time
#footsteps defo rolling plus add more from cup until 3 dice for every roll
#count brains, shotguns

import random


greendice = {'name': 'green', 'faces' : ['footsteps', 'brains', 'brains', 'footsteps','brains','shotgun']}
yellowdice ={'name': 'yellow', 'faces' :['footsteps','shotgun','shotgun', 'footsteps','brains','shotgun']}
reddice ={'name': 'red', 'faces': ['footsteps', 'brains', 'brains', 'footsteps','shotgun','shotgun']}

### THE 13 DICE HAVE BEEN ADDED TO THE RANDOMIZEDDICE LIST TOTALLY RANDOM
availabledice = [greendice, greendice, greendice, greendice, yellowdice, yellowdice, yellowdice, yellowdice, yellowdice, reddice, reddice, reddice, reddice]
readytousedice = []
randomizeddice = []

#this function takes available dice and randomly moves it to randomizeddice
#every player needs a dice set
#the dice set gets reset (randomized after end of every round)

readytousedice = availabledice.copy()
for i in range(13):
    diceindex = random.randint(0,len(readytousedice) - 1)
    popped = readytousedice.pop(diceindex)
    randomizeddice.append(popped)

############## ADD PAYERS TO THE GAME
playerlist = []
deadlist = []
# namelist = ['Guntars', 'Evita','Kristers']
namelist = []

while True:
    # playerinput = input('autofill?')
    playerinput = 'y'
    if playerinput == 'y':
        namelist = ['Guntars', 'Evita', 'Kristers', 'Janis']
        break
    else:
        while True:
            playerinput = input('Input player name or n to play the game:')
            if playerinput == 'n':
                break
            else:
                namelist.append(playerinput)
                continue
        break





for line in namelist:
    print(line)

# totalroundsinput = input('How many rounds would you like to play?:')
totalroundsinput = 3

######################################## adding players here ##



for i in range(len(namelist)):
    item = {'name':namelist[i], 'shotgun' : 0, 'brains' : 0, 'index': i}
    playerlist.append(item)


for item in playerlist:
    print(item)



def justify(input, type):
    while True:
        if type == 'r':
            print(input.rjust(50, ' '))
            break
        elif type == 'l':
            print(input.ljust(50, ' '))
            break
        elif type == 'c':
            print(input.center(50, ' '))
            break
        else:
            print('please select r(ight), l(eft) or c(enter)')
            input('you forgot to add the type, now you must suffer')
            continue

def selectplayer(player):
    #players ir iekshaa, vajag nextindex
    for item in playerlist:
        if player == item:
            #shis atrod indeksu, kuraa vietaa player atrodas playerlist
            index = playerlist.index(item)
            #vajag atrast nextplayerindex
            if len(playerlist) - 1 == index:
                nextplayerindex = 0
            else:
                nextplayerindex = index + 1

    return nextplayerindex


def playerlistlen():
    print('len playerlist', len(playerlist))
    for item in playerlist:
        print(item['name'])

def deadplayer(player):

#    time.sleep(1)
    lastindex = 0
    nextindex = 0
    for item in playerlist:
        if player == item:
            index = playerlist.index(item)
            print('player index found', index)

            print('marker 1 - finding lastindex')
            if index - 1 > 0:
                lastindex = index - 1
            elif index - 1 == 0:
                lastindex = 0
            else:
                lastindex = False
                print('lastindex problem line 133, not possible however')

            print('lastindex found', lastindex)

            if len(playerlist) >= 2:
                popped = playerlist.pop(index)
                deadlist.append(popped)
                if index == 0:
                    nextindex = 0
                    return nextindex
                elif index == 1:
                    nextindex = 1
                    print('TRIGGERED B')
                    return nextindex
                elif index > 1:
                    nextindex = index
                    print('TRIGGERED C')
                    return nextindex
            elif len(playerlist) == 1:
                popped = playerlist.pop(index)
                deadlist.append(popped)
                nextindex = 0
                print('TRIGGERED D')
                playerlistlen()
                return nextindex
            elif len(playerlist) == 0:
                print('No more players left in the playerlist, round over')
                print('Returning None, how is this possible??? line 192')
                print('TRIGGERED E')
                playerlistlen()
                return None


####################################

#this is rolling sequence
def roll():
    currentdice = randomizeddice.copy()
    currentfootsteps = []
    loopsteps = []
    roundfaces = {'shotgun': 0, 'brains': 0}
    rollcount = 0
    red, yellow, green = 0,0,0

    rollcount += 1
    txtt = 'Roll' + ' ' + str(rollcount)
    justify(txtt, 'c')

    print('You have 13 dice')
        #randomizeddice, currentdice, useddice = [], [], []
    for i in range(3):
        # justify('Rolling...', 'c')
        # time.sleep(0.5)
        index = random.randint(0, len(currentdice)-1)
        popped = currentdice.pop(index)
        face = popped['faces'][random.randint(0,5)]
        if face == 'footsteps':
            currentfootsteps.append(popped)

        #jaazin kureejie bija tie dice, kuriem ir footsteps. ja nav footsteps, tad pass on to face count to roundfaces
        #currentfootsteps savaac visus dice ar footsteps
        #ja face == roundfaces key, tad value ir +1. Shaadi pieskaitam current faces

        if face in roundfaces:
            roundfaces[face] +=1

        #PHASE 2 - CHECK IF CURRENTFOOTSTEPS ARE 3 AND IF THEY ARE, ROLL THE 3 DICE
                #IF THERY AREN'T ADD MORE DICE FROM POT AND ROLL THE 3 DICE
                # INSTEAD OF RANDOM DICE THAT WERE RANDOMLY DRAWN FROM RANDOMIZEDDICE BEFORE , NOW THEY ARE KNOWN DICE FROM CURRENTDICE PLUS ONE OR TWO FROM RANDOMIZEDDICE
# done - exit point for 3 shotguns
    print('')
    justify('You have collected:', 'c')
    for k,v in roundfaces.items():
        txt = str(k) + ', ' + str(v)
        justify(txt,'r')
    if roundfaces['shotgun'] >= 3:
        txt = '3 SHOTGUNS!!! ROUND OVER FOR YOU a (this is triggered when in the first roll all 3 are shotguns)'
        justify(txt,'c')
        roundfaces['brains'] = 0
        return roundfaces #### I think this is the culprit - don't joke around with return statement, it finishes off the function
    print('Dice Left:')
    # print(str(len(currentdice)).rjust(50, ' '))
    justify(str(len(currentdice)), 'r')
    for line in currentdice:
        if line['name'] == 'red':
            red += 1
        elif line['name'] == 'yellow':
            yellow += 1
        elif line['name'] == 'green':
            green += 1
    #info text
    colors = red, 'red,', yellow, 'yellow, and', green, 'green'
    colors = str(colors).replace('(', '').replace(')','').replace('\'','').replace(',','')
    justify(colors, 'r')
    #info text
    #reset roll colours
    red, yellow, green = 0, 0, 0
    #reset roll colours
    while True: # this is for if someone does not answer the quetion with y or n if they want to continue or not
        justify('ROLL AGAIN a? y/n', 'c')
        inputrollagain = input().lower()
        if inputrollagain == 'y':
            rollcount += 1
            txt = 'Roll ' +  str(rollcount)
            justify(txt, 'c')
    #remove from 2 places the below thecause it won't be needed any more after currentdice is installed in randomizeddice places
            while True:
#this is the repeat roll after the first roll. dunno why it needed to be separated but ok... Possibly because of missing currentfootsteps not being 3
                # print('BEFORE WE REFILL, LET\'S CHECK THE LEN(CURRENTFOOTSTPES)')
                # print('len currentfootsteps', len(currentfootsteps))
                # print('you pressed y, you chose to roll again')
                # print('before rolling we need to refill dice after last roll')
                #HERE WE REFILL DICE

                if len(currentfootsteps) < 3:
                    if 3 - len(currentfootsteps) < len(currentdice):
                        for i in range(3 - len(currentfootsteps)):
                            popped = currentdice.pop(random.randint(0, len(currentdice) - 1) )
                            #print('added', popped['name'])
                            currentfootsteps.append(popped)
                            #HERE CURRENTFOOTSTEPS ARE REFILLED AND i HAVE FULL SET, NOW i NEED TO ROLL THE SET TO SEE THE OUTCOME OF THE DICE - THE FACES TO BE COUNTED
                            #TE BUUS GARAAM, JO JA RANDOMIZEDICE IR 1 BET VAJAG 2, TAD BUUS ERRORS
                    else:
                        #TE TAA PROBLEEMA IR NOVEERSTA
    # done - exit point for out of dice

                        txt = 'NOT ENOUGH DICE IN THE POT ONLY ' +  str(len(currentdice)) +  ' left'
                        justify(txt, 'l')
                        justify('ROUND OVER', 'c')
                        return roundfaces
                # elif len(currentfootsteps) == 3:
                #     print('AUTOROLL WITH 3 DICE')
                # print('8888888DICE HAVE BEEN REFILLED FROM RANDOMIZEDDICE TO CURRENTFOOTSTEPS AND WE ARE READY TO ROLL')
                for i in range(3):
                    # justify('Rolling...', 'c')
                    # time.sleep(0.5)
                    # print('')
                    # print('')
                            #CHECK THIS WHOLE SECTION FOR OUTPUTS AND SUBRTRACTIONS
                    # print('len currentfootsteps before popping - IF 3 THEN WE ARE GOOD', len(currentfootsteps))
                    index = random.randint(0, len(currentfootsteps) - 1)
                    # print('index ANYWHERE BETWEEN 0 AND 2:', index)
                    popped = currentfootsteps.pop(index)
                    # print('popped = THIS SHOWS WHICH ELEMENT WAS REMOVED FROM CURRENTFOOTSTEPS', popped)
                    # print('len currentfootsteps after popping (REMOVING)', len(currentfootsteps))
                    face = popped['faces'][random.randint(0, 5)]
                    # print('RANDOMLHY SELECTED FACE OF THAT REMOVED ELEMENT', face)
                    if face == 'footsteps':
                        loopsteps.append(popped)
                    if face in roundfaces:
                        roundfaces[face] += 1
                currentfootsteps = loopsteps
                ## HERE LOOPSTEPS BECOME CURRENTFOOTSTEPS, NOW WE NEED TO FILL IN WITH STUFF FROM MAIN RANDOM LIST randomizedice
                ##while loop starts here because of loopsteps
                            #CHECK THIS WHOLE SECTION FOR OUTPUTS AND SUBRTRACTIONS

                # print('roundfaces OTHER ROLL', roundfaces)
     #done - exit point for 3 shotguns

                justify('You have collected:', 'c')
                for k, v in roundfaces.items():
                    print(k, v)
#triggering ass to jump to the next round you bastard
                if roundfaces['shotgun'] >= 3:
                    txtt = '3 SHOTGUNS!!! ROUND OVER FOR YOU b'
                    justify(txtt, 'c')
                    roundfaces['brains'] = 0
                    return roundfaces
                print('Dice left:')
                justify(str(len(currentdice)), 'r')
                for line in currentdice:
                    if line['name'] == 'red':
                        red += 1
                    elif line['name'] == 'yellow':
                        yellow +=1
                    elif line['name'] == 'green':
                        green +=1
                colorss = str(colors).replace('(', '').replace(')', '').replace('\'', '').replace(',', '')
                justify(colorss, 'r')
                red, yellow, green = 0,0,0
                justify('ROLL AGAIN A? y/n', 'c')
                inputrollagain = input().lower()
                if inputrollagain == 'y':
                    rollcount += 1
                    print('Roll', rollcount)
                    continue
    #done - exit point for not wanting to roll again - done
                elif inputrollagain == 'n':
                    #end result
                    return roundfaces
                    break
            break
        elif inputrollagain == 'n':
    #done - exit point for not wanting to roll again - done
            txttt = 'You fool, this round is over for you'
            justify(txttt, 'c')
            return roundfaces
            # roundfaces
            #end result
            break
        else:
            print('Please enter y for yes and n for no')
            continue



        #I don't need to check for randomizeddice, I need to check for currentfootsteps is at least 3
        #and if there are no more randomizeddice available, then the round is over for this player

#roll()


#initialize player
print('=' * 50)
print('THE ZOMBIE DICE GAME')
rules = '''The rules:
Every player has 13 dice in the pot
Every roll you have to roll 3 dice. If you don't have 3 dice, you finish the round and count the brains.
Player re-rolls the dice with footsteps and draws the missing dice from the pot if he has less than 3.
If a player gets 3 shotguns in a round, he then collects 0 brains in that round.
All dice have 2 shotgun faces. Green have more brains, Red have more shotguns and Yellow have equal number of brains and faces.
'''

print(rules)
# input('Press Enter to continue.....')


player = playerlist[0]
#STEPS OF THE GAME
#game starts with player selected
#player rolls, maybe dies, the brains have added to his brain count
#if 3 shotguns, no brains awarded in that round, deadplayer gets triggered and next player selected by the same deadplayer
#deadplayer takes the player and puts it in deadplayer list, all the rest players keep playring and get selected next based on #
#if they didn't get 3 shotguns
#3 shotguns and deadplayer work together.
#deadplayer() triggers next player in case of 3 shotguns
#selectplayer() triggers next player in case of ending turn not dying
#most brains of 10 rounds
#when player dies, he then gets 0 brains, but can wait another round after all the others have finished rolling
                # start of game
#************************************************************************
# playerinput = input('Enter y to continue... or n not to continue')
playerinput = 'y'
while True:
    if playerinput == 'y':
        print('It\'s a me - Mario, let\'s a GOOOOO')
        break
    elif playerinput == 'n':
        print('We will play anyway. You don\'t have any brains...')
        break
    else:
        print('Ha ha!!! You stupid')
        break

round = 0
while True: # this loop is to count rounds and to exit after 10 round or whatever number or rounds is selected
    player = playerlist[0]
    print('start of round', round + 1)
    templist = []
    while True: # -- all action happens in this block
                    #vajag lai reset playerlist katra raunda saakumaa
                    #ar katru raundu vairaak speeleetaaji ir popped. vajag lai vinji saiet atpakalj playerlist vai arii izmantot buferi

        endofround = ''
        endround = ''
        print('=' * 50)
        justify(player['name'], 'c')
        justify('Round ' + str(round + 1), 'c')
        # input('Press enter to continue....')
        roundfaces = roll()
        # print('*** checking roundfaces for '.upper(),player['name'].upper(), roundfaces)
        player['brains'] += roundfaces['brains']
        player['shotgun'] += roundfaces['shotgun']
        if roundfaces['shotgun'] >= 3: # if more than 3 shotguns in a round face after a roll
            justify('Dead meat', 'c')

            if playerlist.index(player) == len(playerlist) - 1 and len(playerlist) == 0: #te jau ir nomainiits uz raunds beidzaas ar peedeejo speeleetaaju
                print('why is this finishing the game? is the playerlist 0?')
                endround = 'yes'

            # print('***index stuff***')
            # print('current index', playerlist.index(player))
            # print('playerlist BEFORE')
            for item in playerlist:
                print(item['name'])
            nextplayerindex = deadplayer(player)                       #te met aaraa playerus kas palikushi
            if nextplayerindex >= len(playerlist):
                print('the index is out of scope')
                print('the index is', nextplayerindex)
                print('the lenght of playerlist is', len(playerlist))
                break
            print('glukainais nextplayerindex', nextplayerindex)
            input('carry onn')
            if len(playerlist) == 0:
                print('finally the len of playerlist is 0, endround  == yes a')
                endround = 'yes'
            elif len(playerlist) > 0:
                player = playerlist[nextplayerindex]
                print('next player', player)

            # print('nextplayerindex, this is where the error comes from')
            # print('list index is out of range')
            # print('nextplayerindex:', nextplayerindex)

            if endround == 'yes':
                break
        else: #if there are not 3 shotguns
            thistext = 'Player ' +  player['name'] +  ' has finished the round, he didn\'t die'

            justify(thistext, 'c')
            player['brains'] += roundfaces['brains']
            if playerlist.index(player) == len(playerlist) - 1 and len(playerlist) == 0: #te jau ir nomainiits uz raunds beidzaas ar peedeejo speeleetaaju
                endround = 'yes'
            # if player['index'] == 3:
            #     print('player [index] is 3')
            #     endround = 'yes'
            nextplayerindex = selectplayer(player)
            player = playerlist[nextplayerindex]

            if endround == 'yes':
                player = playerlist[0]
                break

    round += 1
    txt = '*************End of round ' +  str(round) + ' *******************************8'
    justify(txt, 'c')

    #here we add everything back to playerlist

    for item in playerlist:
        deadlist.append(item)
        print(len(deadlist), 'len deadlist')
    playerlist.clear()
    for i in range(len(deadlist)):
        for item in deadlist:
            if item['index'] == i:
                playerlist.append(item)
        print(len(playerlist), 'len playerlist')
    deadlist.clear()

    if round >= int(totalroundsinput):
        break
    else:
        continue

txt = 'Let\'s count final score:'
justify(txt, 'c')
for line in playerlist:
    print('Name: ', line['name'])
    print('Total Brains: ')
    justify(str(line['brains']), 'r')
    print('Total Shotguns: ')
    justify(str(line['shotgun']), 'r')
    print('*' * 50)

print('')
print('Thank you for playing this silly game I made! Ur a star')





#use 3 dices per roll
# footsteps defo rolling plus add more from cup until 3 dice for every roll
# count brains, shotguns
#player['name] shotgun brain


print('I will now write things to consider when programming a game like this')
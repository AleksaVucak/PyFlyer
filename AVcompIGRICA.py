#AV Computer Igrica FSE
#Jetpack Joyride/Flappy Bird
#January 23rd, 2022
##############################################################
###Basic's (Music, Fonts, Screen size)###

from pygame import *
from random import *

screen = display.set_mode((1400, 830))
display.set_caption("AV's Jetpack Joyride")
myClock = time.Clock()

#Initializing music and fonts
font.init()
mixer.init()

athleticFont = font.Font("data/New Athletic M54.ttf", 50)
mixer.music.load("data/menuMusic.mp3")

###########################################################################
###Loading in graphics/images###

menuBackground=image.load("data/menuBackground.jpg").convert()
gameLogo=image.load("data/gameLogo.png")
gameLogo=transform.scale(gameLogo,(990,375))
screen.blit(gameLogo,(0,0))
showcaseSkin1=image.load("data/showcaseSkin1.png")
showcaseSkin2=image.load("data/showcaseSkin2.png")
showcaseSkin3=image.load("data/showcaseSkin3.png")
background1=image.load("data/background.png").convert()
background2=image.load("data/background.png").convert()
backButton=image.load("data/backNormal.png")
backButtonHover=image.load("data/backHover.png")
backButtonPressed=image.load("data/backPressed.png")
arcadeButton=image.load("data/arcadeNormal.png")
arcadeButtonHover=image.load("data/arcadeHover.png")
arcadeButtonPressed=image.load("data/arcadePressed.png")
settingsButton=image.load("data/settingsNormal.png")
settingsButtonHover=image.load("data/settingsHover.png")
settingsButtonPressed=image.load("data/settingsPressed.png")
shopButton=image.load("data/shopNormal.png")
shopButtonHover=image.load("data/shopHover.png")
shopButtonPressed=image.load("data/shopPressed.png")
laserOn1=image.load("data/laserOn1.png")
laserOn2=image.load("data/laserOn2.png")
laserOn3=image.load("data/laserOn3.png")
laserOn4=image.load("data/laserOn4.png")
laserOn5=image.load("data/laserOn5.png")
laserOff=image.load("data/laserOff.png")
plateNormal=image.load("data/plateNormal.png")
continueButtonNormal=image.load("data/continueButtonNormal.png")
continueButtonHover=image.load("data/continueButtonHover.png")
returnToMenuButtonNormal=image.load("data/returnButtonNormal.png")
returnToMenuButtonHover=image.load("data/returnButtonHover.png")
gameOverLevels=image.load("data/levelsGameOver.png")
gameOverArcade=image.load("data/gameOverArcade.png")
skin1ImageNormal=image.load("data/shopSkin1Normal.png")
skin1ImageHover=image.load("data/shopSkin1Hover.png")
skin2ImageNormal=image.load("data/shopSkin2Normal.png")
skin2ImageHover=image.load("data/shopSkin2Hover.png")
skin3ImageNormal=image.load("data/shopSkin3Normal.png")
skin3ImageHover=image.load("data/shopSkin3Hover.png")
shopTitle=image.load("data/shopTitleImage.png")
settingsTitle=image.load("data/settingsTitleImage.png")
arcadeTitle=image.load("data/arcadeTitle.png")
bombImage=image.load("data/bombImage.png")
skin1Selected=image.load("data/shopSkin1Selected.png")
skin2Selected=image.load("data/shopSkin2Selected.png")
skin3Selected=image.load("data/shopSkin3Selected.png")
congratsScreen=image.load("data/congratsScreen.png")
arcadeInformationImage=image.load("data/arcadeInformationPage.png")
playArcadeButtonNormal=image.load("data/playArcadeButtonNormal.png")
playArcadeButtonHover=image.load("data/playArcadeButtonHover.png")
playAgainButtonNormal=image.load("data/playAgainButtonNormal.png")
playAgainButtonHover=image.load("data/playAgainButtonHover.png")
arcadeWinPage=image.load("data/arcadeWin.png")
settingsPageImage=image.load("data/settingsPageImage.png")
unmuteNormal=image.load("data/unmuteNormal.png")
unmuteHover=image.load("data/unmuteHover.png")
unmuteSelected=image.load("data/unmuteSelected.png")
muteNormal=image.load("data/muteNormal.png")
muteHover=image.load("data/muteHover.png")
muteSelected=image.load("data/muteSelected.png")
checkNormal=image.load("data/checkNormal.png")
checkHover=image.load("data/checkHover.png")
checkSelected=image.load("data/checkSelected.png")
uncheckNormal=image.load("data/uncheckNormal.png")
uncheckHover=image.load("data/uncheckHover.png")
uncheckSelected=image.load("data/uncheckSelected.png")

###Setting Rects###
arcadeRect = Rect(150, 655, arcadeButton.get_width(), arcadeButton.get_height())
shopRect = Rect(900, 655, shopButton.get_width(), shopButton.get_height())
settingsRect = Rect(1025, 20, settingsButton.get_width(), settingsButton.get_height())
backRect = Rect(50, 50, backButton.get_width(), backButton.get_height())
continueRect = Rect(618, 635, continueButtonNormal.get_width(), continueButtonNormal.get_height())
playAgainRect = Rect(618, 635, playAgainButtonNormal.get_width(), playAgainButtonNormal.get_height())
returnToMenuRect = Rect(976, 635, returnToMenuButtonNormal.get_width(), returnToMenuButtonNormal.get_height())
skin1Rect = Rect(50, 320, skin1ImageNormal.get_width(), skin1ImageNormal.get_height())
skin2Rect = Rect(525, 320, skin2ImageNormal.get_width(), skin2ImageNormal.get_height())
skin3Rect = Rect(1000, 320, skin3ImageNormal.get_width(), skin3ImageNormal.get_height())
fpsCheckRect = Rect(690, 335, checkNormal.get_width(), checkNormal.get_height())
fpsUncheckRect = Rect(790, 335, checkNormal.get_width(), checkNormal.get_height())
soundEffectsUnmuteRect = Rect(905, 420, checkNormal.get_width(), checkNormal.get_height())
soundEffectsMuteRect = Rect(1005, 420, checkNormal.get_width(), checkNormal.get_height())
musicUnmuteRect = Rect(555, 505, checkNormal.get_width(), checkNormal.get_height())
musicMuteRect = Rect(655, 505, checkNormal.get_width(), checkNormal.get_height())
settingsPageImageRect = settingsPageImage.get_rect(midtop=(screen.get_width()/2, 275))
titleRect = shopTitle.get_rect(midtop=(screen.get_width()/2, 75))
gameEndRect = gameOverLevels.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
arcadeInformationRect = arcadeInformationImage.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
logoRect = gameLogo.get_rect(midtop=(screen.get_width()/2,1))
showcaseRect = showcaseSkin1.get_rect(midbottom=(screen.get_width() / 2, 1080))
playArcadeButtonRect = playArcadeButtonNormal.get_rect(midtop=(screen.get_width()/2, 650))
returnToMenuRectMiddle = returnToMenuButtonNormal.get_rect(midtop=(screen.get_width()/2, 635))
arcadeReturnRectMiddle = returnToMenuButtonNormal.get_rect(midtop=(screen.get_width()/2, 660))

#########################################################################################################################
###Variables/Music###

running = True
speed = 20
frame = 0
level = 1
playerY = 415
gameMode = "menu"
backgroundX1 = 0
backgroundX2 = background1.get_width()
scrollCount = 0
verticalVelocity = 0
gravity = 1
jumpSpeed = -12
scrollSpeed = 1
arcadeScrollSpeed = 1
deadAnimTimer = 0
immuneTimer = 0
winTimer = 0
laserPositions = []
arcadeLaserPositions = []
staticCoinPositions = []
arcadeStaticCoinPositions = []
dynamicCoinPositions = []
arcadeDynamicCoinPositions = []
bombPositions = []
arcadeBombPositions = []
playerDead = False
arcadePlayerDead = False
deadMan = False
playerWon = False
arcadePlayerWon = False
totalDistancePixels = 0
insufficientFundsError = 0
amountInsufficient = 0
arcadeScore = 0
immune = False
coinsAdded = False
flyAnimations = []
runAnimations = []
jumpAnimations = []
landAnimations = []
deathAnimations = []
winAnimations = []
bombDeath = False

coinsCollected = 0
coinsInAccount = 000
selectedCharacter = 0    # 0 - First Colour 1 - Second Colour 2 - Third Colour
coinMultiplier = 1
arcadeHighscore = 0
arcadeCoinsHighscore = 0
showFPS = True
soundEffectsMuted = False
musicMuted = False

if not musicMuted:
    mixer.music.play(-1)
elif musicMuted:
    mixer.music.pause()
laserDeath = mixer.Sound("data/laserDeath.mp3")
coinCollect = mixer.Sound("data/coinEaten.mp3")
explosionSound = mixer.Sound("data/bombExploding.mp3")

##########################################################################################
###Calling functions###

def readData():
    # Function that reads all of the data from the "gameInformation" txt file. This data is then assigned to variables that are used throughout the game.
    global coinsInAccount, selectedCharacter, coinMultiplier, prestigeAlready, arcadeHighscore, arcadeCoinsHighscore, showFPS, soundEffectsMuted, musicMuted
    infoFile = open("data/gameInformation.txt")    # Opening the information file
    coinsInAccount = int(infoFile.readline())
    selectedCharacter = int(infoFile.readline())  # 0 - First character 1 - Second character 2 - Third character
    coinMultiplier = int(infoFile.readline())    # 1 - Normal 5 - Prestige Master Multiplier
    arcadeHighscore = int(infoFile.readline())
    arcadeCoinsHighscore = int(infoFile.readline())
    showFPSFile = int(infoFile.readline())    # 0 - Don't Show 1 - Show
    soundEffectsMutedFile = int(infoFile.readline())    # 0 - Not Muted 1 - Muted
    musicMutedFile = int(infoFile.readline())

    infoFile.close()

    if showFPSFile == 0:
        showFPS = False
    elif showFPSFile == 1:
        showFPS = True

    if soundEffectsMutedFile == 0:
        soundEffectsMuted = False
    elif soundEffectsMutedFile == 1:
        soundEffectsMuted = True

    if musicMutedFile == 0:
        musicMuted = False
    elif musicMutedFile == 1:
        musicMuted = True


def writeData():
    #    Function that writes the data to the "gameInformation" txt file. This data includes variables used in the game that may have changed.
    outputFile = open("data/gameInformation.txt")    # Opening the file to overwrite any existing content

    if showFPS:
        showFPSFile = 1
    elif not showFPS:
        showFPSFile = 0

    if soundEffectsMuted:
        soundEffectsMutedFile = 1
    elif not soundEffectsMuted:
        soundEffectsMutedFile = 0

    if musicMuted:
        musicMutedFile = 1
    elif not musicMuted:
        musicMutedFile = 0
    
class Animation:    # Class for animations that makes displaying much easier
    def __init__(self, imagePrefix, count):
        self.imageCount = count    # imageCount is now the same as count
        self.images = []    # images is a blank list

        for i in range(self.imageCount):    # Looping through the length of images (image count/number if images)
            filename = "data/" + imagePrefix + "{:0>5}".format(i) + ".png"    # Using {:0>5} to number format 'i' into a 5 length 5 field fill with 0s
            self.images.append(image.load(filename))    # Loading and adding the images to the images list

    def display(self, xposition, yposition):
        imageIndex = frame // speed % self.imageCount    # Finding image the animation is on
        screen.blit(self.images[imageIndex], (xposition, yposition))    # Displaying the image at the x and y position

##########################################################################################################################################################################
###Sprites###
        
runCol1Animation = Animation("RunCol1", 6)    # Initializing the animations
flyCol1Animation = Animation("FlyCol1", 6)
wonCol1Animation = Animation("WonCol1", 13)
jumpCol1Animation = Animation("JumpCol1", 5)
landCol1Animation = Animation("LandCol1", 4)
deathCol1Animation = Animation("DeathCol1", 6)
runCol2Animation = Animation("RunCol2", 6)
flyCol2Animation = Animation("FlyCol2", 6)
wonCol2Animation = Animation("WonCol2", 13)
jumpCol2Animation = Animation("JumpCol2", 5)
landCol2Animation = Animation("LandCol2", 4)
deathCol2Animation = Animation("DeathCol2", 6)
runCol3Animation = Animation("RunCol3", 6)
flyCol3Animation = Animation("FlyCol3", 6)
wonCol3Animation = Animation("WonCol3", 13)
jumpCol3Animation = Animation("JumpCol3", 5)
landCol3Animation = Animation("LandCol3", 4)
deathCol3Animation = Animation("DeathCol3", 6)
coinAnimation = Animation("coinStatic", 6)
explosionAnimation = Animation("explosion", 15)

runAnimations.append(runCol1Animation)    # Appending the animations to the lists for their corresponding action (All colours of each action are in the lists)
runAnimations.append(runCol2Animation)
runAnimations.append(runCol3Animation)
flyAnimations.append(flyCol1Animation)
flyAnimations.append(flyCol2Animation)
flyAnimations.append(flyCol3Animation)
winAnimations.append(wonCol1Animation)
winAnimations.append(wonCol2Animation)
winAnimations.append(wonCol3Animation)
jumpAnimations.append(jumpCol1Animation)
jumpAnimations.append(jumpCol2Animation)
jumpAnimations.append(jumpCol3Animation)
landAnimations.append(landCol1Animation)
landAnimations.append(landCol2Animation)
landAnimations.append(landCol3Animation)
deathAnimations.append(deathCol1Animation)
deathAnimations.append(deathCol2Animation)
deathAnimations.append(deathCol3Animation)

############################################################################################################################
###Interactions###

def menuInteraction():
    # Function that is responsible for the interactions on the menu page. Displays hover images where needed and changes pages if clicked correctly
    global gameMode
    if arcadeRect.collidepoint(mx, my):
        if click:
            gameMode = "arcadeMode"
        elif mb[0]:
            screen.blit(arcadeButtonPressed, arcadeRect)
        else:
            screen.blit(arcadeButtonHover, arcadeRect)
    if shopRect.collidepoint(mx, my):
        if click:
            gameMode = "shop"
        elif mb[0]:
            screen.blit(shopButtonPressed, shopRect)
        else:
            screen.blit(shopButtonHover, shopRect)
    if settingsRect.collidepoint(mx, my):
        if click:
            gameMode = "settingsPage"
        elif mb[0]:
            screen.blit(settingsButtonPressed, settingsRect)
        else:
            screen.blit(settingsButtonHover, settingsRect)


def shopInteraction():
    # Function that is responsible for the interactions on the shop page. Displays hover images where needed and changes pages if clicked correctly
    global selectedCharacter, coinsInAccount, insufficientFundsError, amountInsufficient
    if skin1Rect.collidepoint(mx, my):
        if click:
            selectedCharacter = 0
        elif selectedCharacter != 0:
            screen.blit(skin1ImageHover, skin1Rect)
    if skin2Rect.collidepoint(mx, my):
            if click:
                selectedCharacter = 1
            elif selectedCharacter != 1:
                screen.blit(skin2ImageHover, skin2Rect)
    if skin3Rect.collidepoint(mx, my):
            if click:
                selectedCharacter = 2
            elif selectedCharacter != 2:
                screen.blit(skin3ImageHover, skin3Rect)

def displayBackButton():
    # Function that is responsible for the interaction with the back button. It brings you back to the menu.
    global gameMode, click, mb, mx, my
    screen.blit(backButton, backRect)
    if backRect.collidepoint(mx, my) and insufficientFundsError == 0:    # You could only use it if there isn't an error
        if click:
            gameMode = "menu"
        elif mb[0]:
            screen.blit(backButtonPressed, backRect)
        else:
            screen.blit(backButtonHover, backRect)


def drawMenu():
    # Function that is responsible for "drawing" all of the things on the menu page.
    screen.blit(menuBackground, (0, 0))
    screen.blit(gameLogo, logoRect)
    screen.blit(arcadeButton, arcadeRect)
    screen.blit(shopButton, shopRect)
    screen.blit(settingsButton, settingsRect)
    if selectedCharacter == 0:
        screen.blit(showcaseSkin1, showcaseRect)
    if selectedCharacter == 1:
        screen.blit(showcaseSkin2, showcaseRect)
    if selectedCharacter == 2:
        screen.blit(showcaseSkin3, showcaseRect)


def displayCoinsInAccount():
    # Function that is responsible for displaying the amount of coins in your account.
    coinAnimation.display(1720, 50)    # Displaying the coin amount with the coin animated "shining"
    coinsText = athleticFont.render(str(coinsInAccount), True, (255, 255, 255))
    screen.blit(coinsText, (5, 0))


def drawShop():
    # Function that is responsible for "drawing" all of the things on the shop page.
    screen.blit(menuBackground, (0, 0))
    screen.blit(shopTitle, titleRect)
    displayBackButton()
    if selectedCharacter == 0:    # Series of if statements showing the skins as locked or unlocked dependant on if you purchased it or not
        screen.blit(skin1Selected, skin1Rect)
    else:
        screen.blit(skin1ImageNormal, skin1Rect)
    if selectedCharacter == 1:
        screen.blit(skin2Selected, skin2Rect)
    else:
        screen.blit(skin2ImageNormal, skin2Rect)
    if selectedCharacter == 2:
        screen.blit(skin3Selected, skin3Rect)
    else:
        screen.blit(skin3ImageNormal, skin3Rect)


def drawArcadePage():
    # Function that is responsible for "drawing" all of the things on the arcade page.
    screen.blit(menuBackground, (0, 0))
    screen.blit(arcadeTitle, titleRect)
    displayBackButton()
    screen.blit(arcadeInformationImage, arcadeInformationRect)
    arcadeHighscoreText = athleticFont.render("{:0>6}".format(arcadeHighscore), True, (255, 255, 255))    # Displaying highscore screen
    screen.blit(arcadeHighscoreText, (760, 365))
    arcadeCoinsHighscoreText = athleticFont.render("{:0>3}".format(arcadeCoinsHighscore), True, (255, 255, 255))
    screen.blit(arcadeCoinsHighscoreText, (965, 420))
    screen.blit(playArcadeButtonNormal, playArcadeButtonRect)    # Displaying the play arcade button along with the rectangle to check for interaction


def arcadeInteraction():
    # Function that is responsible for the interactions on the arcade page. Displays hover images where needed and changes pages if clicked correctly
    global gameMode
    if playArcadeButtonRect.collidepoint(mx, my):    # If you press play, you play the arcade game mode
        if click:
            gameMode = "playArcade"
            setupArcade()
        else:
            screen.blit(playArcadeButtonHover, playArcadeButtonRect)


def setupArcade():
    # Function that is responsible for the placing obstacles for the arcade mode, resetting important values and setting up the speed and background
    global arcadeScrollSpeed, coinsCollected, arcadePlayerDead, coinsAdded, totalDistancePixels, backgroundX1, backgroundX2, bombDeath, deadMan, arcadePlayerWon
    if not musicMuted:
        mixer.music.pause()
    arcadeScrollSpeed = 11
    createArcadeLasers()
    createArcadeCoins()
    createArcadeBombs()
    coinsCollected = 0
    totalDistancePixels = 0
    backgroundX1 = 0
    backgroundX2 = background1.get_width()
    arcadePlayerDead = False
    deadMan = False
    coinsAdded = False
    bombDeath = False
    arcadePlayerWon = False


def createArcadeLasers():
    # Function that is responsible for the creation of the lasers within the arcade.
    global arcadeLaserPositions
    arcadeLaserPositions.clear()
    for i in range(330):
        xpos = randint(1260, 999990)  # We don't want a laser within the first 300 pixels and since 29760 is the end, we want the last laser at least 100 pixels before the end
        ypos = randint(25, 770)  # Difference between sprite height and laser height is 30 so 800 - 30
        arcadeLaserPositions.append([xpos, ypos])


def createArcadeCoins():
    # Function that is responsible for the creation of the coins within the arcade.
    global arcadeStaticCoinPositions, arcadeDynamicCoinPositions
    arcadeStaticCoinPositions.clear()
    arcadeDynamicCoinPositions.clear()
    for i in range(randint(150, 330)):  # Generating static coins
        xpos = randint(1260, 999990)  # Generating random X for static coin
        ypos = randint(25, 770)  # Generating random y for static coin
        arcadeStaticCoinPositions.append([xpos, ypos])
    for i in range(randint(20, 50)):  # Generating dynamic coins
        xpos = randint(1260, 999990)
        originalypos = randint(350, 700)  # Generating random y for original dynamic coin
        ypos = randint(225, 570)
        arcadeDynamicCoinPositions.append([xpos, ypos, originalypos, 3])

##################################################################################################################################################
###Arcade Creation###

def createArcadeBombs():
    # Function that is responsible for the creation of the bombs within the arcade.
    global arcadeBombPositions
    arcadeBombPositions.clear()
    for i in range(randint(3, 5)):
        xpos = randint(1260, 999990)  # Generating random X position
        arcadeBombPositions.append([xpos, 925])  # Appending the random xpos but all with the same Y so the bomb is on the ground


def drawArcadeLasers():
    # Function that is responsible for "drawing" lasers on the arcade levels.
    global arcadeLaserPositions
    for i in range(len(arcadeLaserPositions)):
        if arcadeLaserPositions[i][0] < 1400 and not immune:  # Doesn't draw the laser if you are immune, only draws when immunity expires
            screen.blit(laserOn1, (arcadeLaserPositions[i][0], arcadeLaserPositions[i][1]))
        elif arcadeLaserPositions[i][0] < 1400 and not immune:  # Doesn't draw the laser if you are immune, only draws when immunity expires
            screen.blit(laserOn2, (arcadeLaserPositions[i][0], arcadeLaserPositions[i][1]))
        elif arcadeLaserPositions[i][0] < 1400 and not immune:  # Doesn't draw the laser if you are immune, only draws when immunity expires
            screen.blit(laserOn3, (arcadeLaserPositions[i][0], arcadeLaserPositions[i][1]))
        elif arcadeLaserPositions[i][0] < 1400 and not immune:  # Doesn't draw the laser if you are immune, only draws when immunity expires
            screen.blit(laserOn4, (arcadeLaserPositions[i][0], arcadeLaserPositions[i][1]))
        elif arcadeLaserPositions[i][0] < 1400 and not immune:  # Doesn't draw the laser if you are immune, only draws when immunity expires
            screen.blit(laserOn5, (arcadeLaserPositions[i][0], arcadeLaserPositions[i][1]))
        else:
            screen.blit(laserOff, (arcadeLaserPositions[i][0], arcadeLaserPositions[i][1]))
        arcadeLaserPositions[i][0] -= arcadeScrollSpeed


def drawArcadeCoins():
    # Function that is responsible for "drawing" coins on the arcade levels.
    global arcadeStaticCoinPositions, arcadeDynamicCoinPositions
    for i in range(len(arcadeStaticCoinPositions)):  # The loop is drawing the coins at random positions according to what we appended earlier to the staticCoinsPositions list
        coinAnimation.display(arcadeStaticCoinPositions[i][0], arcadeStaticCoinPositions[i][1])
        arcadeStaticCoinPositions[i][0] -= arcadeScrollSpeed
    for i in range(len(arcadeDynamicCoinPositions)):  # Displaying the animated dynamic coin based off the positions appended earlier
        coinAnimation.display(arcadeDynamicCoinPositions[i][0], arcadeDynamicCoinPositions[i][1])
        if arcadeDynamicCoinPositions[i][1] < arcadeDynamicCoinPositions[i][2] - 200 or arcadeDynamicCoinPositions[i][1] > arcadeDynamicCoinPositions[i][2] + 200:
            arcadeDynamicCoinPositions[i][3] = -arcadeDynamicCoinPositions[i][3]
        arcadeDynamicCoinPositions[i][1] += arcadeDynamicCoinPositions[i][3]
        arcadeDynamicCoinPositions[i][0] -= arcadeScrollSpeed

    coinAnimation.display(1720, 50)  # Displaying the coin sprite
    coinsText = athleticFont.render(str(coinsCollected), True, (255, 255, 255))
    screen.blit(coinsText, (1800, 45))


def drawArcadeBombs():
    # Function that is responsible for "drawing" bombs on the arcade levels.
    global arcadeBombPositions
    for i in range(len(arcadeBombPositions)):
        screen.blit(bombImage, (arcadeBombPositions[i][0], arcadeBombPositions[i][1]))  # Generating the bomb at the position of the list
        arcadeBombPositions[i][0] -= arcadeScrollSpeed


def moveArcadeScene():
    # Function that is responsible for "drawing" the scene and moving it.
    global backgroundX1, backgroundX2, arcadeScrollSpeed, totalDistancePixels, arcadeScore
    screen.blit(background1, (backgroundX1, 0))
    screen.blit(background2, (backgroundX2, 0))
    if not arcadePlayerDead:
        if totalDistancePixels > -1000000:  # If we haven't reached the end of the level (4 times through the background - half of the screen size)
            backgroundX1 -= arcadeScrollSpeed
            backgroundX2 -= arcadeScrollSpeed
            totalDistancePixels -= arcadeScrollSpeed
    if backgroundX1 <= -background1.get_width():    # Resetting the background to its original position if it is fully off screen
        backgroundX1 = backgroundX2 + background1.get_width()
    if backgroundX2 <= -background2.get_width():
        backgroundX2 = backgroundX1 + background2.get_width()
    arcadeScrollSpeed = 11 + -totalDistancePixels // 27760
    arcadeScore = -totalDistancePixels


def moveArcadePlayer():
    # Function that is responsible for movement and display of the character within the arcade mode
    global verticalVelocity, playerY, gameMode, deadMan
    # Moving the player
    if totalDistancePixels <= -999690:    # 999690 is going through 1 level 33 times, making arcade fun but challenging
        if playerY > 800:
            playerY = 415
            verticalVelocity = 0
        verticalVelocity += gravity
    else:
        if not arcadePlayerDead and not arcadePlayerWon:
            if playerY > 800:
                playerY = 415
                verticalVelocity = 0
            elif playerY < 25:
                playerY = 25
            if playerY < 800:
                verticalVelocity += gravity
            if flying and totalDistancePixels > -999900:
                verticalVelocity = jumpSpeed
        elif arcadePlayerDead:
            verticalVelocity += gravity
            if playerY > 800:
                playerY = 800
                verticalVelocity = 0
    playerY += verticalVelocity

    # Displaying the animations
    if not arcadePlayerDead:
        if flying:
            if playerY > 700:
                jumpAnimations[selectedCharacter].display(640, playerY)
            else:
                flyAnimations[selectedCharacter].display(640, playerY)
        else:
            if totalDistancePixels > -999990 and playerY == 800:
                runAnimations[selectedCharacter].display(640, playerY)
            elif arcadePlayerWon:
                winAnimations[selectedCharacter].display(640, playerY)
            else:
                landAnimations[selectedCharacter].display(640, playerY)
    else:
        if playerY < 800:
            landAnimations[selectedCharacter].display(640, playerY)
        elif playerY == 800:
            deadMan = True
            deathAnimations[selectedCharacter].display(640, playerY)


def checkArcadeCollisions():
    # Function that is responsible checking for any collision between the player and coins, lasers, or bombs within the arcade mode
    global arcadePlayerDead, coinsCollected, bombDeath
    for i in range(len(arcadeLaserPositions)):  # Looping for the amount of indexes in arcadeLaserPositions list
        laserHitbox = Rect(arcadeLaserPositions[i][0], arcadeLaserPositions[i][1], 32, 305)  # Initializing the hit box of the laser
        if playerHitbox.colliderect(laserHitbox) and not immune:  # Checking for collision with the player and laser
            arcadePlayerDead = True
            if not soundEffectsMuted:
                laserDeath.play()
            break
    for i in range(len(arcadeBombPositions)):  # Looping for the amount of indexes in ArcadeBombPositions list
        bombHitbox = Rect(arcadeBombPositions[i][0], arcadeBombPositions[i][1], 100, 100)  # Initializing bomb hitbox
        if playerHitbox.colliderect(bombHitbox) and not immune:  # Checking for collision with bomb
            arcadePlayerDead = True
            if not soundEffectsMuted:
                explosionSound.play()
            bombDeath = True
            del arcadeBombPositions[i]
            break
    for i in range(len(arcadeStaticCoinPositions)):  # Looping for the amount of indexes in staticCoinPositions list
        coinHitbox = Rect(arcadeStaticCoinPositions[i][0], arcadeStaticCoinPositions[i][1], 50, 50)  # initializing static coin hitbox
        if playerHitbox.colliderect(coinHitbox):  # Checking for collision with static coin and player
            coinsCollected += 1
            if not soundEffectsMuted:
                coinCollect.play()
            del arcadeStaticCoinPositions[i]
            break
    for i in range(len(arcadeDynamicCoinPositions)):  # Looping for the amount of indexes in dynamicCoinPositions list
        coinHitbox = Rect(arcadeDynamicCoinPositions[i][0], arcadeDynamicCoinPositions[i][1], 50, 50)  # Initializing dynamic coin hitbox
        if playerHitbox.colliderect(coinHitbox):  # Checking for collision with player and dynamic coin
            coinsCollected += 1
            if not soundEffectsMuted:
                coinCollect.play()
            del arcadeDynamicCoinPositions[i]
            break


def checkArcadeConditions():
    # Function that is responsible for checking for a condition
    global arcadePlayerWon, gameMode, winTimer, deadAnimTimer
    if totalDistancePixels <= -100000:  # If statements checking conditions, checking if player travelled the amount of pixels to win
        arcadePlayerWon = True
    if arcadePlayerWon:  # Checking if the player won, if they did sends them to the winPage
        winTimer += 1
        if winTimer == 135:
            gameMode = "arcadeWinPage"
            winTimer = 0
    if deadMan:  # Checking if player is dead, if so send them to the gameOver page
        deadAnimTimer += 1
        if deadAnimTimer == 45:
            gameMode = "arcadeGameOver"
            deadAnimTimer = 0
        if bombDeath and deadAnimTimer < 15:
            explosionAnimation.display(600, 700)


def drawArcadeGameOver():
    # Function that is responsible for "drawing" the game over screen when dying in the arcade level.
    screen.blit(gameOverArcade, gameEndRect)
    coinsCollectedText = athleticFont.render("{} x{}".format(coinsCollected, coinMultiplier), True, (255, 255, 255))  # Displaying the amount of coins you collected during the level and with your prestige multiplier
    screen.blit(coinsCollectedText, (947, 345))
    totalCoinsText = athleticFont.render(str(coinsInAccount), True, (255, 255, 255))  # Amount of total coins you have in your account
    screen.blit(totalCoinsText, (785, 400))
    scoreText = athleticFont.render("{:0>6}".format(arcadeScore), True, (255, 255, 255))
    screen.blit(scoreText, (577, 292))
    screen.blit(playAgainButtonNormal, playAgainRect)  # Displaying continue button if you have enough coins
    screen.blit(returnToMenuButtonNormal, returnToMenuRect)  # Displaying return to menu button1


def checkArcadeScore():
    # Function that is responsible for checking if a new highscore has been set, both for coins and for the actual score
    global arcadeHighscore, arcadeCoinsHighscore
    if arcadeScore > arcadeHighscore:    # Displaying a new high score if previous high score is beaten
        arcadeHighscore = arcadeScore
    if coinsCollected > arcadeCoinsHighscore:    # Displaying a new coin score if previous high score is beaten
        arcadeCoinsHighscore = coinsCollected


def arcadeGameOverInteraction():
    # Function that is responsible for the interaction with the arcade's game over page
    global gameMode, coinsAdded, coinsInAccount
    if not coinsAdded:
        coinsInAccount += coinsCollected * coinMultiplier    # Adding new coins collected into total
        coinsAdded = True
        checkArcadeScore()
    if playAgainRect.collidepoint(mx, my):    # Checking for collision with the play again button
        if click:
            setupArcade()
            gameMode = "playArcade"
        else:
            screen.blit(playAgainButtonHover, playAgainRect)
    if returnToMenuRect.collidepoint(mx, my):    # Checking if mouse collides with return to menu button returning you to menu
        if click:
            gameMode = "menu"
        else:
            screen.blit(returnToMenuButtonHover, returnToMenuRect)


def drawArcadeWinPage():
    # Function that is responsible for "drawing" the win page when winning in the arcade level.
    screen.blit(arcadeWinPage, gameEndRect)
    coinsCollectedText = athleticFont.render("{} x{}".format(coinsCollected, coinMultiplier), True, (255, 255, 255))  # Displaying the amount of coins you collected during the level and with your prestige multiplier
    screen.blit(coinsCollectedText, (960, 405))
    totalCoinsText = athleticFont.render(str(coinsInAccount), True, (255, 255, 255))  # Amount of total coins you have in your account
    screen.blit(totalCoinsText, (785, 454))
    scoreText = athleticFont.render("{:0>6}".format(arcadeScore), True, (255, 255, 255))
    screen.blit(scoreText, (580, 350))
    screen.blit(returnToMenuButtonNormal, arcadeReturnRectMiddle)


def arcadeWinPageInteraction():
    # Function that is responsible for the interaction with the arcade's win page
    global gameMode
    if arcadeReturnRectMiddle.collidepoint(mx, my):    # Returning you to menu
        if click:
            gameMode = "menu"
        else:
            screen.blit(returnToMenuButtonHover, arcadeReturnRectMiddle)


def displayArcadeScore():
    # Function that is responsible for displaying the arcade score
    arcadeScoreText = athleticFont.render("{:0>6}".format(arcadeScore), True, (255, 255, 255))
    screen.blit(arcadeScoreText, (50, 50))    # Displaying your score while in the arcade

#######################################################################################################################################
###Settings Interactions###

def settingInteraction():
    # Function that is responsible for the interaction with the settings page
    global coinsInAccount, coinMultiplier, selectedCharacter, showFPS, soundEffectsMuted, musicMuted
    if fpsCheckRect.collidepoint(mx, my):    # Making show FPS button interactive (Showing and hiding FPS)
        if not showFPS:
            if click:
                showFPS = True
            else:
                screen.blit(checkHover, fpsCheckRect)
    if fpsUncheckRect.collidepoint(mx, my):
        if showFPS:
            if click:
                showFPS = False
            else:
                screen.blit(uncheckHover, fpsUncheckRect)
    if soundEffectsUnmuteRect.collidepoint(mx, my):    # Making sound effects button interactive
        if soundEffectsMuted:
            if click:
                soundEffectsMuted = False    # If the sound effects button is muted and you check it off, it will unmute it
            else:
                screen.blit(unmuteHover, soundEffectsUnmuteRect)
    if soundEffectsMuteRect.collidepoint(mx, my):
        if not soundEffectsMuted:
            if click:
                soundEffectsMuted = True
            else:
                screen.blit(muteHover, soundEffectsMuteRect)
    if musicUnmuteRect.collidepoint(mx, my):    # If the music button is muted and you check it off, it will unmute it
        if musicMuted:
            if click:
                musicMuted = False
                mixer.music.unpause()    # If any music was paused it will now play
            else:
                screen.blit(unmuteHover, musicUnmuteRect)
    if musicMuteRect.collidepoint(mx, my):
        if not musicMuted:    # If music is not muted and you check it, it will mute the music
            if click:
                musicMuted = True
                mixer.music.pause()    # If any music was playing, it will now pause
            else:
                screen.blit(muteHover, musicMuteRect)


def drawSettings():
    # Function that is responsible for "drawing" all of the things on the settings page.
    screen.blit(menuBackground, (0, 0))    # Drawing settings page
    screen.blit(settingsTitle, titleRect)
    screen.blit(settingsPageImage, settingsPageImageRect)

    if showFPS:    # If you have show fps on, it will draw a box with a check in it
        screen.blit(checkSelected, fpsCheckRect)
    else:
        screen.blit(checkNormal, fpsCheckRect)
    if not showFPS:    # If you have show fps off, it will draw a box with a uncheck symbol in it
        screen.blit(uncheckSelected, fpsUncheckRect)
    else:
        screen.blit(uncheckNormal, fpsUncheckRect)

    if not soundEffectsMuted:
        screen.blit(unmuteSelected, soundEffectsUnmuteRect)    # Drawing a unmute icon if sound effects are not muted and selected
    else:
        screen.blit(unmuteNormal, soundEffectsUnmuteRect)
    if soundEffectsMuted:    # If the sound effects are muted, use the muted icon
        screen.blit(muteSelected, soundEffectsMuteRect)
    else:
        screen.blit(muteNormal, soundEffectsMuteRect)

    if not musicMuted:    # Drawing a mute or unmute icon dependant on if the music is muted or unmuted
        screen.blit(unmuteSelected, musicUnmuteRect)
    else:
        screen.blit(unmuteNormal, musicUnmuteRect)
    if musicMuted:
        screen.blit(muteSelected, musicMuteRect)
    else:
        screen.blit(muteNormal, musicMuteRect)

    displayBackButton()


def displayFPS():
    # Function that is responsible for displaying the frames per second in the bottom right corner
    fps = int(myClock.get_fps())
    fpsText = athleticFont.render(str(fps), True, (255, 255, 255))
    screen.blit(plateNormal, (1275, 725))
    screen.blit(fpsText, (1307, 745))

#################################################################################################################################
###MAIN GAME LOOP###

while running:    # Main loop of the game, nearly all functions are called on from here
    click = False
    flying = False
    for evt in event.get():
        if evt.type == QUIT:
            running = False
##            writeData()
        if evt.type == MOUSEBUTTONDOWN and evt.button == 1:
            click = True
    keys = key.get_pressed()    # Getting the keys pressed, the mouse positions, and the mouse buttons that are pressed
    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()
    playerHitbox = Rect(700, playerY + 35, 110, 195)    # Average player hitbox dimensions
    if keys[K_SPACE] and not playerWon:    # If you haven't won and you are pressing space, the character will fly (flying being true will activate the movePlayer part responsible for vertical lift)
        flying = True
    if gameMode == "menu":    # If the page is menu, draw it along with allowing interaction, and displaying coins
        if not mixer.music.get_busy() and not musicMuted:
            mixer.music.unpause()    # If the music is not muted, this line lets it play
        drawMenu()
        menuInteraction()
        displayCoinsInAccount()
    elif gameMode == "arcadeMode":    # Calling all of the functions needed for the arcade page (not the game but the page before it)
        drawArcadePage()
        arcadeInteraction()
    elif gameMode == "playArcade":    # Calling all of the functions needed for the arcade game
        moveArcadeScene()
        moveArcadePlayer()
        if not arcadePlayerDead:    # If the player is not dead then the score is displayed, lasers, bombs, and coins are drawn, and we check for collisions (All done through individual functions)
            displayArcadeScore()
            drawArcadeLasers()
            drawArcadeCoins()
            drawArcadeBombs()
            checkArcadeCollisions()
        checkArcadeConditions()
    elif gameMode == "arcadeGameOver":    # Calling all of the functions needed for the arcade's game over page
        drawArcadeGameOver()
        arcadeGameOverInteraction()
    elif gameMode == "arcadeWinPage":    # Calling all of the functions needed for the arcade's win page
        drawArcadeWinPage()
        arcadeWinPageInteraction()
    elif gameMode == "shop":    # Calling all of the functions needed for the shop page
        drawShop()
        if insufficientFundsError == 0:    # If there is no error then you could interact
            shopInteraction()
        else:
            insufficientFundsWarning()    # If there is an error then the function that displays the error is called upon
        displayCoinsInAccount()
    elif gameMode == "settingsPage":    # Calling all of the functions needed for the settings page
        drawSettings()
        if insufficientFundsError == 0:    # If there is no error then you could interact
            settingInteraction()
        else:
            insufficientFundsWarning()
        displayCoinsInAccount()
    elif gameMode == "winPage":    # Calling all of the functions needed for the level's win page
        drawWinPage()
        winPageInteraction()
    if showFPS:    # If the fps is toggled to show, the function that shows the fps is called
        displayFPS()
    frame += 1    # Adding to the frame, used for my animation class
    myClock.tick(60)
    display.flip()
quit()


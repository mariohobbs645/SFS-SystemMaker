import os
import json
print("Welcome to SFS System Maker")
print("©2024 Mariohobbs")
def smhelp():
    print("use command smhelp() to access the help menu")
    print("Use command 'setup()' to setup a system")
    print("Use command 'hmap()' to create a heightmap")
    print("Use command 'pd()' to create a planet")
    print("a guide on basic usage: https://spaceflight-simulator.fandom.com/wiki/Planet_Editor_Tutorial")
def setup():
    #Setup the planet pack
    #Creates Import Settings file and obtains the variables in the file
    file = "Import_Settings.txt"
    dp = input("Include Default Planets?(true/false) ")
    dh = input("Include Default Heightmaps?(true/false) ")
    dt = input("Include Default Textures?(true/false) ")
    hs = input("Hide Stars In Atmosphere?(true/false) ")
    #Converts the input into a string that'll be written soon
    ist = '{\n  "includeDefaultPlanets"; '+dp+","+'\n'+'  "includeDefaultHeightmaps": '+dh+","+'\n'+'  "includeDefaultTextures": '+dt+','+'\n'+'  "hideStarsInAtmosphere": '+hs+"\n"+"}"
    with open(file, 'w') as file:
        # Write content to the file
        file.write(ist)
     
    print("Import_Settings.txt Created Successfully")
    #Creates Space_Center_Data.txt
    file = "Space_Center_Data.txt"
    ad = input("Input where the space center will be (EX: Earth, Mars; use the name of the planet ")
    an = input("What will the angle of the space center be? ")
    hp = input("What will be the launchpad's horizontal position (In the frame of reference of the space center ")
    he = input("What will be the height of the launchpad? ")
    #Converts your data into a string
    ist = '{\n  "address": "'+ad+'",\n  "angle": '+an+',\n  "position_Launchpad": {\n    "horizontalPosition": '+hp+',\n    "heightVe": '+he+'\n  }\n}'
    with open(file, 'w') as file:
        # Write content to the file
        file.write(ist)
    print("Space_Center_Data.txt Created Successfully ")
    #Create Version.txt
    file = "Version.txt"
    ve = input("What version is this pack for? ")
    with open(file, 'w') as file:
        # Write content to the file
        file.write(ve)
    print("Version.txt Created")
    os.mkdir("Heightmap Data")
    os.mkdir("Planet Data")
    os.mkdir("Texture Data")
    print("Heightmap Folder Created!")
    print("Planet Data Folder Created!")
    print("Textures Folder Created")
    print("Basic Setup Completed")
def hmap():
    #Get a name for the heightmap
    hname = input("What will the heightmap be called?")
    file = "Heightmap Data/"+hname+".txt"
    point = 0
    heightmap = []
    #Repeatedly asks for the points
    while not point == "quit":
        point = input("Input a point or type quit if you are done ")
        if not point == "quit":
            heightmap.append(point)
    print(heightmap)
    heightmapstring = '{\n    "points": ['
    count = 0
    #Add the data from user to a string
    for i in heightmap:
        if count == 0:
            heightmapstring = heightmapstring+"\n"+"        "+i
            count = count+1
        else:
            heightmapstring = heightmapstring+",\n"+"        "+i
    heightmapstring = heightmapstring+"\n    ]\n}"
    with open(file, 'w') as file:
        # Write heightmap string to the file
        file.write(heightmapstring)
         
def pd():
    #Get a name for the planet
    file = "Planet Data/"+input("What will the planet be called? ")+".txt"
    version = input("What Version? ")
    #basedata
    radius = input("What is the Radius? ")
    gravity = input("What is the Gravity? ")
    timewarp = input("What is the timewarp height? ")
    vah = input("what is the velocity arrows height?")
    #mapcolor
    mapcolor ='    "mapColor": {\n      "r": '
    r = input("what is the red color value?")
    g = input("what is the green color value?")
    b = input("what is the blue color value?")
    a = input("what is the alpha value?")
    sig = input("Is the object significant (true/false)? ")
    rotcam = input("Does the object rotate the camera?")
    #Atmospheric physics data
    athe = input("At what height does the atmosphere start at?")
    aden = input("what is the atmospheric density? ")
    curve = input("what is the atmospheric curve?")
    parmul = input("what is the parachute multiplier?")
    upat = input("How high the atmosphere is, between 0.1 and 0.5")
    swi = input("What is the shockwave intensity?")
    mhvm = input("what is the minimum Heating Velocity Multiplier?")
    #Atmospheric Visuals Data
    print(json.dumps({'version': version, '6': 7}, sort_keys=True, indent=4))

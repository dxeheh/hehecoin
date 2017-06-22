import string, random, os, json, msvcrt, time, encoder, decoder

#   Hehecoin Miner
#   Ryan Earll
#   ryangearll@gmail.com
#   @ryanxea

VERSION = "1.1"
DATEUPDATED = "6/22/2017"
os.system('color a')

def getKey():               # Returns the key.txt as a string
    with open("key.txt", "r") as f:ret = f.read()
    return ret

def clearScreen():          # Clears the screen and prints the header at the top
    os.system('cls')
    print("Hehecoin Miner v" + VERSION + ", Last Updated " + DATEUPDATED + "\n\n")

def exitProgram(d = None):          # Provides the user with a prompt before exiting. If given a dictionary, encodes it accordingly and saves to wallet.txt
    if not d==None:
        updateWallet(d)
    input("\nPress enter to exit...\n")
    quit()

def updateWallet(d):
    with open("wallet.txt", "w") as f:f.write(encoder.encode(getKey(), json.dumps(d)))

def getWallet():            # Returns the decoded wallet as a dictionary
    with open("wallet.txt", "r") as f:wal = f.read()
    return json.loads(decoder.decode(getKey(), wal))

def mine():                 # Starts mining for hehecoin
    clearScreen()
    d = getWallet()
    print("Server handshake verified, initializing mining process...")
    for _ in range(4):
        time.sleep(1)
        print("...")
    print("Beginning mining process. Press any button to stop.\n")
    while True:
        search = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(4096))
        x = 3
        for x in range(len(search)):
            if search[x]==search[x-1] and search[x]==search[x-2] and search[x]==search[x-3]:
                d["Coins"] += 1
                print("A coin has been found! Added to wallet.     New balance: " + str(d["Coins"]))
                updateWallet(d)
        time.sleep(0.2)
        if msvcrt.kbhit():break

                            # Start the "main" function

clearScreen()
if not os.path.isfile("wallet.txt"):
    print("No wallet.txt found in current directory, please move it here or use Hehecoin Core to create a new one.")
    exitProgram()

if not os.path.isfile("key.txt"):
    print("\nkey.txt not found in current directory. Please move it here and restart Hehecoin Miner.")
    exitProgram()

while True:
    clearScreen()
    i = input("\n1. Mine\n2. Exit\n")
    if i=="2":quit()
    elif i=="1":mine()

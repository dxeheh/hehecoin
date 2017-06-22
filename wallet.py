import string, random, os, json, encoder, decoder

#   Hehecoin Core
#   Ryan Earll
#   ryangearll@gmail.com
#   @ryanxea

VERSION = "1.1"
DATEUPDATED = "6/22/2017"
os.system('color a')

def keyGen():               # Creates a 256 character private key to key.txt for use with encode/decode
    key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(128))
    with open("key.txt", "w+") as f:f.write(key)

def getKey():               # Returns the key.txt as a string
    with open("key.txt", "r") as f:ret = f.read()
    return ret

def addressGen():           # Returns a 256 character public address for recieving Hehecoin
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(128))

def newWallet():            # Creates a new wallet and key for use with Hehecoin Core
    keyGen()
    info = {"Address" : addressGen(),
            "Coins" : 0}
    j = json.dumps(info)
    j = encoder.encode(getKey(), j)
    with open("wallet.txt", "w+") as f:f.write(j)

def getWallet():            # Returns the decoded wallet as a dictionary
    with open("wallet.txt", "r") as f:wal = f.read()
    return json.loads(decoder.decode(getKey(), wal))

def showWallet():           # Clears screen and displays information about wallet
    clearScreen()
    d = getWallet()
    print("Your wallet info:\n")
    print("Public Address: " + d["Address"])
    print("Coins: " + str(d["Coins"]) + "\n\n")

def sendCoin(send, n):      # "Sends" coins to an address
    showWallet()
    d = getWallet()
    if n<=0:
        print("You cannot do that.")
        input("Press enter to continue...")
    elif n>d["Coins"]:
        print("You do not have " + str(n) + " coins to send. Please try again")
        input("Press enter to continue...")
    else:
        d["Coins"] -= n
        with open("wallet.txt", "w") as f:f.write(encoder.encode(getKey(), json.dumps(d)))
        showWallet()
        print(str(n) + " coins have been transferred to that address.")
        input("Press enter to continue...")

def clearScreen():          # Clears the screen and prints the header at the top
    os.system('cls')
    print("Hehecoin Core v" + VERSION + ", Last Updated " + DATEUPDATED + "\n\n")

def exitProgram(d = None):  # Provides the user with a prompt before exiting. If given a dictionary, encodes it accordingly and saves to wallet.txt
    if not d==None:
        with open("wallet.txt", "w") as f:f.write(encoder.encode(getKey(), json.dumps(d)))
    input("\nPress enter to exit...\n")
    quit()

                            # Start the "main" function

clearScreen()
if not os.path.isfile("wallet.txt"):
    while True:
        choice = input("No wallet.txt found in current directory, would you like to create one? (y/n)\n")
        if choice.upper() == "Y":
            newWallet()
            break
        elif choice.upper() == "N":
            print("\nPlease move your wallet.txt to the current directory and restart Hehecoin Core.")
            exitProgram()

if not os.path.isfile("key.txt"):
    print("\nkey.txt not found in current directory. Please move it here and restart Hehecoin Core.")
    exitProgram()

while True:
    showWallet()
    i = input("\n1. Send coins\n2. Exit\n")
    if i=="1":
        showWallet()
        sendCoin(input("Enter public address to send coins to:\n"), int(input("\nEnter amount of coins to send:\n")))
    elif i=="2":quit()

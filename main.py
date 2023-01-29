import hashlib
import hmac
import string
import random


def randomString(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class provablyFair:

    def __init__(self, serverSeed, clientSeed, nonce, secretSald):
        self.serverSeed = serverSeed
        self.clientSeed = clientSeed
        self.nonce = nonce
        self.secretSald = secretSald
        self.charsroll = 15
        self.maxroll = 100000

    def get_roll(self):
        key = str(self.clientSeed) + "-" + str(self.nonce)
        h = hmac.new(key.encode(), self.serverSeed.encode(), hashlib.sha512).hexdigest()
        dec = (int(h[0:self.charsroll], 16) % self.maxroll)
        return int(dec) + 1

    def publicHash(self):
        return hmac.new(self.secretSald.encode(), self.serverSeed.encode(), "sha256").hexdigest()


if __name__ == "__main__":

    #example generate pf data
    serverSeed = randomString(16)
    clientSedd = "ABCD"
    nonce = 0
    secretSald = randomString(12)
    data = provablyFair(serverSeed, clientSedd, nonce, secretSald)
    print(data.get_roll())
    print(data.publicHash())
    print("--------------------------------")

    #example checker
    serverSeed = "fLKT8YGsZaMgc6Iz"
    secretSald = "mgV7y7knLq3Wmx3z"
    clientSedd = "dPatyUJVyQ5obfzg"
    publicHash = "f85ff47ac66c7c039bbe24748ac13a206159fc24418c7a994de50682132a27e3"
    nonce = 2
    roll = 81080

    data = provablyFair(serverSeed, clientSedd, nonce, secretSald)

    print(bcolors.OKCYAN + "Your publicHash: ", publicHash)
    print(bcolors.OKCYAN + "Your roll: ", roll)

    print(bcolors.OKCYAN +"Generated publicHash: ", data.publicHash())
    print(bcolors.OKCYAN +"Generated roll: ", data.get_roll())


    if (data.publicHash() == publicHash) and (data.get_roll() == roll):
        print(bcolors.OKGREEN + "The data is identical, everything is fine")
    else:
        print(bcolors.FAIL + "Roll is invalid")

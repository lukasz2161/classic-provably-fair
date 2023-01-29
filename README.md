The classic provably fair system used on gaming sites

<code>
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
  </code>

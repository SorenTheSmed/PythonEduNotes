import hashlib

def genPossibleCombos(letters, goal):
    for first in letters:
        combination = first
        hashedCombination = hashlib.md5(combination.encode('utf-8')).hexdigest()

        if hashedCombination == goal:
            print("Successfully found the target: ", combination)
            break

        for second in letters:
            combination = first + second
            hashedCombination = hashlib.md5(combination.encode('utf-8')).hexdigest()

            if hashedCombination == goal:
                print("Successfully found the target: ", combination)
                break

            for third in letters:
                combination = first + second + third
                hashedCombination = hashlib.md5(combination.encode('utf-8')).hexdigest()

                if hashedCombination == goal:
                    print("Successfully found the target: ", combination)
                    break

                for fourth in letters:
                    combination = first + second + third + fourth
                    hashedCombination = hashlib.md5(combination.encode('utf-8')).hexdigest()

                    if hashedCombination == goal:
                        print("Successfully found the target: ", combination)
                        break

                    for fifth in letters:
                        combination = first + second + third + fourth + fifth
                        hashedCombination = hashlib.md5(combination.encode('utf-8')).hexdigest()

                        if hashedCombination == goal:
                            print("Successfully found the target: ", combination)
                            break

                        for sixth in letters:
                            combination = first + second + third + fourth + fifth + sixth
                            hashedCombination = hashlib.md5(combination.encode('utf-8')).hexdigest()

                            if hashedCombination == goal:
                                print("Successfully found the target: ", combination)
                                break


hashList = ["c4ded2b85cc5be82fa1d2464eba9a7d3", "48dc9b7120d05f513380683985a9d7a4", "c4ca4238a0b923820dcc509a6f75849b", "e10adc3949ba59abbe56e057f20f883e"]

for hashes in hashList:
    genPossibleCombos("0123456789", hashes)



"""
Find the clear-text version of these:

c4ded2b85cc5be82fa1d2464eba9a7d3
48dc9b7120d05f513380683985a9d7a4
c4ca4238a0b923820dcc509a6f75849b
e10adc3949ba59abbe56e057f20f883e

"""
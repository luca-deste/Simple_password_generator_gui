import string
import random
elements = [string.ascii_letters,string.digits,'^\|!"£$%&/()=?+*']
strElem = ''.join(elements)
def generatePassword():
    passw = []
    for x in range(20):
        passw.append(random.choice(strElem))
        #print(passw)
    passString = ''.join(passw)
    print(passString)
    return passString

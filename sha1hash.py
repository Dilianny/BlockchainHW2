import hashlib
import time
import sys
if len(sys.argv)<2:
    print "Hash not entered"
else:
    hash = sys.argv[1]
    tries=0
    #salt="f0744d60dd500c92c0d37c16174cc58d3c4bdd8e"
    salted=""
    start = time.clock()
    with open("10-million-password-list-top-1000000.txt") as passwords:
        for guess in passwords.readlines():
            tries=tries+1
            guess = guess.strip()
            if (len(sys.argv) == 2):
                if hashlib.sha1(bytes(guess)).hexdigest() != hash:
                    continue
                elif hashlib.sha1(bytes(guess)).hexdigest() == hash:
                    end =time.clock()
                    print "number of tries: ", tries
                    print "time taken: ", end-start, "seconds."
                    print "password is: ", guess
                    break
            elif (len(sys.argv)==3):
                if hashlib.sha1(bytes(guess)).hexdigest() == sys.argv[2]:
                    salted = guess
                    print "salt text is: ", salted
                for passw in passwords.readlines():
                    passw= passw.strip()
                    saltedp = salted + passw
                    print saltedp
                    if hashlib.sha1(bytes(saltedp)).hexdigest() == hash:
                        end =time.clock()
                        print "number of tries: ", tries
                        print "time taken: ", end-start, "seconds."
                        print "password is: ", passw
                        break
                    else:
                        print "Password not found"

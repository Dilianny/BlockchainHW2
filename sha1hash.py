import hashlib
import time
import sys
if len(sys.argv)<2:
    print "Hash not entered"
else:
    hash = sys.argv[1]
    tries=0
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
                start = time.clock()
                if hashlib.sha1(bytes(guess)).hexdigest() == sys.argv[2]:
                    salted = guess.strip()
                    print "salt text is: ", salted
                    with open("10-million-password-list-top-1000000.txt") as passwords:
                        for guess in passwords.readlines():
                            guess= guess.strip()
                            saltedp = salted + guess
                            tries=tries+1
                            if hashlib.sha1(bytes(saltedp)).hexdigest() != sys.argv[1]:
                                continue
                            elif hashlib.sha1(bytes(saltedp)).hexdigest() == sys.argv[1]:
                                end =time.clock()
                                print "number of tries: ", tries
                                print "time taken: ", end-start, "seconds."
                                print "password is: ", guess
                                break
                            #else:
                                #print "Password not found"

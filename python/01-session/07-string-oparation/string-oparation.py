hacking="hello how are you"

print(hacking)   #hello how are you
print(len(hacking))  #17  (kiyak thoda kiyala)
print(hacking.count("l"))  #2 (l akuru vala count eka)

print(hacking.upper())   #HELLO HOW ARE YOU  (capital letter)
print(hacking.lower())   #hello how are you  (Simple letter)
 
print(hacking.index("a"))  #10  (mulinma a hamba vena thana)

print(hacking[3:12])  #lo how ar  (3-12 print venava)

print(hacking[4:12:3]) #ooa (4-12 venakan  3n 3n pana pana)
print("-------------------------------------------------")

email="nipuna@gmail.com, piyumal@gmail.com, sanu@gmail.com"

print(email.split(","))  #['nipuna@gmail.com', ' piyumal@gmail.com', ' sanu@gmail.com']  (list ekakata da ganna onne nam)

print(email.endswith(".com"))  #True  (.com valin ivara vena eva thiyenavada balanava)
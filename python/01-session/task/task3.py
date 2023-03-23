print("*"*10)
print("hay i am ing-bot, but i hate \"ing\"")

word=input("enter word : ")
endWord=word.endswith("ing")

if(endWord):
    print(word[0:-3])
else:
    print(word)
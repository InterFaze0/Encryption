alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s"
,"t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]




characterList = []
def encryption():
    text = input("Şifrelenecek olan kelimeyi girin: ")
    text = text.lower()
    text = text.split()
    for a in text:
        k = 0
        for i in a:
             k = k + 1 
             characterList.append(alphabet[alphabet.index(i) + k])
        characterList.append('-')   
    newtext = str(characterList)
    newtext = newtext.replace("[","")
    newtext = newtext.replace("]","")
    newtext = newtext.replace(",","")
    newtext = newtext.replace("'","")
    newtext = newtext.replace(" ","")
    newtext = newtext.replace("-"," ")

    print(newtext)         
            

newCharacterList = []
def decryption():
    textOne = input("decript kodunu girin: ")
    textOne = textOne.split()
    for a in textOne:
        k = 0
        for i in a:
            k = k + 1
            newCharacterList.append(alphabet[alphabet.index(i) - k])
        newCharacterList.append("-")
    newtext = str(newCharacterList)
    newtext = newtext.replace("[","")
    newtext = newtext.replace("]","")
    newtext = newtext.replace(",","")
    newtext = newtext.replace("'","")
    newtext = newtext.replace(" ","")
    newtext = newtext.replace("-"," ")
    

    print(newtext)    

chose = input("Bir metin şifrelemek için 'T',bir şifre çözmek için ise 'F' tuşuna basın: ")
chose = chose.lower()
if(chose == "t"):
    encryption()
elif(chose == "f"):
    decryption()





input("Kapatmak için herhangi 'Enter' tuşuna basın")







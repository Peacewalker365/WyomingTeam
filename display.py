import random

def border():
     print("\n******************************************\n")

def menu(strList):
    border()    
    i = 1
    for str in strList:
        print(i, ". " + str + '\n')
        i += 1    
    border()
    
def story(strList):
    border()
    
    random.seed()
    i = random.randint(0, len(strList) - 1)
    print(strList[i])
        
    border()


def video():
     border()
     print("Video is now playing")
     border()

def DisplayBoard():
    print(f"{Game_SET[0]}|{Game_SET[1]}|{Game_SET[2]}")
    print("------")
    print(f"{Game_SET[3]}|{Game_SET[4]}|{Game_SET[5]}")
    print("------")
    print(f"{Game_SET[6]}|{Game_SET[7]}|{Game_SET[8]}\n")
def CHECK_WINNER(STNG):
    winner=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for sets in winner:
        if(Game_SET[sets[0]]+Game_SET[sets[1]]+Game_SET[sets[2]]==STNG+STNG+STNG):
            return 1
            break


if __name__=="__main__":
    Game_SET=['1','2','3','4','5','6','7','8','9']
    c=0
    while(True):
        while(True):
            print("X Turn")
            X=int(input("Please enter the position\n"))
            if X>9 or Game_SET[X-1]=='X' or Game_SET[X-1]=='O':
                print("Invalid Input please enter again")
            else:
                Game_SET[X-1]='X'
                c=c+1
                break
        DisplayBoard()
        y=CHECK_WINNER('X')
        if y==1:
            print("X is a Winner")
            break
        if c==9:
            print("Match is Draw")
            break
        while(True):
            print("O Turn")
            O=int(input("Please enter the position\n"))
            if O>9 or Game_SET[O-1]=='X' or Game_SET[O-1]=='O':
                print("Invalid Input please enter again\n")
            else:
                Game_SET[O-1]='O'
                c=c+1
                break
        DisplayBoard()
        y=CHECK_WINNER('O')
        if y==1:
            print("O is a Winner")
            break




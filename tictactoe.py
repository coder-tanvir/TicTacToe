
import random
import copy


class TIC_TAC_TOE:
    def __init__(self):
        self.alive=True;
        self.depth=1000;
        self.player='X';
        self.computer='O';
        self.user='X';
        self.winner=None;
        self.board=["_","_","_","_","_","_","_","_","_"];

    def displayboard(self):
        for i in range (0,3):
            print(self.board[i],end='');
            print('|',end='');
        print('\n',end='');
        print('------');
        for i in range(0,3):
            print(self.board[3+i],end='');
            print('|',end='');
        print('\n',end='');
        print('------');
        for i in range(0,3):
            print(self.board[6+i],end='');
            print('|',end='');
        print('\n',end='');
        print('------');


    def moves(self):
        arr=[];
        for i in range(9):
            if self.board[i]=="_":
                arr.append(i);
        return arr;

    def playerhandler(self,choice):
        self.user=choice;
        if(choice=='X'):
            self.computer='O';
            print("User is 'X' and AI is 'O'" );
        elif(choice=='O'):
            self.computer='X';
            print("User is 'O' and AI is 'X'");

    def validmoves(self, index, player):
        if(index<=9):
            while(self.board[index]!="_"):
                print("Enter a number of an empty slot");
                index=int(input("Enter a valid move please"))-1
            self.board[index]=player;
        else:
           print("Please enter a valid number please");

           
         

        

         
          

            
            
        



    def changeturn(self):
        if(self.player=='O'):
            self.player='X';
        elif(self.player=='X'):
            self.player='O';


    def inputtaker(self):
        self.displayboard();
        print("Please enter a slot number");
        #userinput=(int(input))-1;
        self.validmoves(int(input("Your turn Next: ")) - 1, self.player);

    def victory(self):
        if(self.board[0]==self.board[1]==self.board[2] and self.board[0]!="_" and self.board[1]!="_" and self.board[2] != "_"):
            self.alive=False;
            self.winner=self.board[1];
        if(self.board[3]==self.board[4]==self.board[5] and self.board[3]!="_" and self.board[4]!="_" and self.board[5] != "_"):
            self.alive=False;
            self.winner=self.board[4];
        if(self.board[6]==self.board[7]==self.board[8] and self.board[6]!="_" and self.board[7] !="_" and self.board[8]!="_"):
            self.alive=False;
            self.winner=self.board[7];
        #column
        if(self.board[0]==self.board[3]==self.board[6] and self.board[0]!="_" and self.board[3]!="_" and self.board[6]!="_" ):
            self.alive=False;
            self.winner=self.board[3];
        if(self.board[1]==self.board[4]==self.board[7] and self.board[1]!="_" and self.board[4]!="_" and self.board[7]!="_"):
            self.alive=False;
            self.winner=self.board[4];
        if(self.board[2]==self.board[5]==self.board[8] and self.board[2]!="_" and self.board[5]!="_" and self.board[8]!="_" ):
            self.alive=False;
            self.winner=self.board[5];
        #diagonals
        if(self.board[0]==self.board[4]==self.board[8] and self.board[0]!="_" and self.board[4]!="_" and self.board[8]!="_"):
            self.alive=False;
            self.winner=self.board[4];
        if(self.board[2]==self.board[4]==self.board[6] and self.board[2]!="_" and self.board[4]!="_" and self.board[6]!="_"):
            self.alive=False;
            self.winner=self.board[2];
        if("_" not in self.board and self.alive==True):   #Draw
            self.alive=False;
            self.winner=None;
        #Else no victor has emerged

game=TIC_TAC_TOE();
depth=1000;

def montecarlosearch(index):
    deepgame=copy.deepcopy(game);
    deepgame.validmoves(index,deepgame.player);
    deepgame.changeturn();
    deepgame.victory();
    while deepgame.alive is True:
        deepgameindex=deepgame.moves();
        randindex=random.randint(0,8);
        while randindex not in deepgameindex:
            randindex=random.randint(0,8);

        deepgame.validmoves(randindex,deepgame.player);
        deepgame.victory();
        deepgame.changeturn();
    if(deepgame.computer=='X' and deepgame.winner=='X'):
        return 2;
    if(deepgame.computer=='O' and deepgame.winner=='O'):
        return 2;
    if(deepgame.computer=='X' and deepgame.winner=='O'):
        return -2;
    if(deepgame.computer=='O' and deepgame.winner=='X'):
        return -2;
    else:
        return 1;       


def montecarlocaller():
    newlegalindex=game.moves();
    count={};
    for i in newlegalindex:
        count[i]=0;
    for i in newlegalindex:
        for j in range(depth):
            count[i]=count[i]+(montecarlosearch(i));

    nextmove=newlegalindex[0];
    nextwin=count[nextmove];

    for i in count:
        if count[i]>=nextwin:
            nextmove=i;
            nextwin=count[nextmove]

    game.validmoves(nextmove,game.player);




#####################################

def play_a_new_game():
    global game
    game = TIC_TAC_TOE()
    
    game.playerhandler(input("'X' is first Player.'O' is second. User get to choose: ").upper())

    if game.user == 'X':
        game.inputtaker()
    else:
        montecarlocaller()
        game.changeturn()
        game.inputtaker()

    while game.alive is True:
        game.changeturn()
        montecarlocaller()
        game.displayboard()
        game.victory()
        if game.alive is True:
            game.changeturn()
            arr2=game.moves();
            print("Empty slot numbers are:")
            for i in range(len(arr2)):
                arr2[i]=arr2[i]+1;
            print(arr2)
                
            game.inputtaker()
            game.displayboard()
            game.victory()

    print("################ GAME FINISHED ####################\n")
    print("################ Result ###########################\n")
    if (game.winner == game.user and game.alive==False):
        print("USER WINS!")
    elif (game.winner == game.computer and game.alive==False):
        print("AI WINS!")
    else:
        print("The Game is Drawn")

if __name__ == '__main__':
    play_a_new_game()



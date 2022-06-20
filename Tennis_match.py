#Tennis_match.py

'''This script simulates a tennis match between two players by providing the probablity
    the player wins when he is serving.'''

import random

class Player:

    def __init__(self, prob) -> None:
        self.prob = prob
        self.points = 0
        self.games = 0
        self.set = 0
        
    def __str__(self) -> str:
        return str

    def winsPoint(self) -> bool:
        return random.uniform(0,1) <= self.prob

    def get_points(self) -> int:
        return self.points

    def inc_points(self) -> int:
        self.points += 1

    def reset_players_points(self) -> int:
        self.points = 0

    def get_games(self) -> int:
        return self.games

    def inc_games(self) -> int:
        self.games += 1

    def reset_players_games(self):
        self.games = 0

    def get_set(self) -> int:
        return self.set
    
    def inc_set(self):
        self.set += 1

class Tennis_match:

    def __init__(self, probA, probB) -> None:
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        self.server = self.playerA 
        self.reciever = self.playerB
        self.set_num = [0, self.playerA]

    def __str__(self) -> str:
        return str

    def coin_toss(self):
        if random.uniform(0,1) < 0.5:
            print(f'\n PlayerB has won the coin toss! \n')
            self.set_num[1] = self.playerB
            self.server = self.playerB
            self.reciever = self.playerA
        else:
            print(f'\nPlayerA has won the coin toss!\n')

    def sim_point(self):
        if self.server.winsPoint():
            self.server.inc_points()
        else:
            self.reciever.inc_points()

    def sim_game(self):
        while not self.GameisOver():
            self.sim_point()
        # increment the game total for winner of game
        a, b = self.getPoints()
        if a > b:
            self.playerA.inc_games()
        else:
            self.playerB.inc_games()
        
    def sim_set(self):
        while not self.SetisOver():
            self.sim_game()
            self.print_game_score()
            self.resetPoints()
            self.change_server()
        # if games are tied at 6-6 play tiebreaker
        a, b = self.getGames()
        if a == b:
            self.TiebreakGame()
        # increment the set total for winner of set
        a, b = self.getGames()
        if a > b:
            self.playerA.inc_set()
        else:
            self.playerB.inc_set()
        print('----------------------------')

    def TiebreakGame(self):
        self.sim_point() # the first player has the first serve
        self.change_server()
        if self.set_num[0] < 5:
            while not self.tiebreakGameOver(): 
                self.sim_point() # the next player has the next two serves
                if not self.tiebreakGameOver(): # the second serve of a player in a tiebreak
                    self.sim_point() 
                    self.change_server()
        else:
            while not self.tiebreakFinal(): 
                self.sim_point() # the next player has the next two serves
                if not self.tiebreakFinal(): # the second serve of a player in a tiebreak
                    self.sim_point() 
                    self.change_server()
            
        a, b = self.getPoints()
        if a > b:
            self.playerA.inc_games()
        else:
            self.playerB.inc_games()
            
        self.print_game_score()
            
    def play(self):
        while not self.matchOver():
            self.nextSet()
            self.sim_set()
            self.resetGames()
            self.swapFirstServe()

    def GameisOver(self):
        # The winner of a game is the first player to reach 4 point while the opponent has less than
        a,b = self.getPoints()
        return (a > 3 and a - b >= 2) or (b > 3 and b - a >= 2)

    def tiebreakGameOver(self):
        a,b = self.getPoints()
        return (a > 6 and a - b >= 2) or (b > 6 and b - a >= 2)

    def tiebreakFinal(self):
        a,b = self.getPoints()
        return (a >= 10 and a - b >= 2) or (b >= 10 and b - a >= 2)

    def SetisOver(self):
        a,b = self.getGames()
        return (a >= 6 and a - b >= 2) or (b >= 6 and b - a >= 2) or (a == 6 and b == 6) #the last option leads to a tiebreaker game

    def matchOver(self):
        a,b = self.getSets()
        return a == 3 or b == 3

    def getPoints(self):
        return self.playerA.get_points(), self.playerB.get_points()
    
    def getGames(self):
        return self.playerA.get_games(), self.playerB.get_games()

    def getSets(self):
        return self.playerA.get_set(), self.playerB.get_set()

    def resetPoints(self):
        self.playerA.reset_players_points(), self.playerB.reset_players_points()

    def resetGames(self):
        self.playerA.reset_players_games(), self.playerB.reset_players_games()

    def nextSet(self):
        self.set_num[0] += 1

    def print_game_score(self):
        points_a,points_b = self.getPoints()
        game_a,game_b = self.getGames()
        if self.server == self.playerA:
            print(f'A {points_a}:{points_b} B ==> {game_a}:{game_b}')
        else:
            print(f'B {points_b}:{points_a} A ==> {game_a}:{game_b}')
        
    def change_server(self):
        # Change who has the serve and who recieves the serve
        if self.server == self.playerA:
            self.server = self.playerB
            self.reciever = self.playerA
        else:
            self.server = self.playerA
            self.reciever = self.playerB

    def swapFirstServe(self):
        if self.set_num[1] == self.playerA:
            self.server = self.playerB
            self.reciever = self.playerA
            self.set_num[1] = self.playerB
        else:
            self.server = self.playerA
            self.reciever = self.playerB   
            self.set_num[1] = self.playerA

def input_player():
    # Input chances of player to win point if he is serving
    while True:
        try:
            a = float(input('Chance of player A to win point when serving: '))
            if a >= 0 and a <= 1:
                break
            elif a >= 0 and a <= 100:
                a /= 100
                break
            else:
                print('Enter a number between 0 and 1')
        except ValueError:
            print("Enter a float between 0 and 1.")
            continue
    
    while True:
        try:
            b = float(input('Chance of player B to win point when serving: '))
            if b >= 0 and b <= 1:
                break
            elif b >= 0 and b <= 100:
                b /= 100
                break
            else:
                print('Enter a number between 0 and 1')
        except ValueError:
            print("Enter a float between 0 and 1.")
            continue
    
    return a,b

def output(game):
    a,b = game.getSets()
    if a > b:
        winner = 'PlayerA'
    else:
        winner = 'PlayerB'
    print(f'{winner} wins {a}:{b}') # add game splits

def main():

    ProbA, ProbB = input_player()
    Game = Tennis_match(ProbA, ProbB)
    Game.coin_toss()
    Game.play()
    output(Game)

if __name__ == '__main__':
    main()
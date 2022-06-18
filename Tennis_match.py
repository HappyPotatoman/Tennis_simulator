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
        if random.uniform(0,1) <= 0.5:
            print(f'\n PlayerB has won the coin toss! \n')
            self.set_num[1] = self.playerB
            self.server = self.playerB
            self.reciever = self.playerA
        else:
            print(f'\nPlayerA has won the coin toss!\n')

    def sim_game(self):
        while not self.GameisOver():
            if self.server.winsPoint():
                self.server.inc_points()
            else:
                self.reciever.inc_points()
        # return who wins game to player object
        a, b = self.getPoints()
        if a > b:
            self.playerA.inc_games()
        else:
            self.playerB.inc_games()

    def nextSet(self):
        self.set_num[0] += 1

    def Set_num(self):
        return self.set_num[0]
            
    def GameisOver(self):
        # The winner of a game is the first player to reach 4 point while the opponent has less than
        a,b = self.getPoints()
        return a > 3 and a - b >= 2 or b > 3 and b - a >= 2

    def getPoints(self):
        return self.playerA.get_points(), self.playerB.get_points()

    def resetPoints(self):
        self.playerA.reset_players_points(), self.playerB.reset_players_points()

    def resetGames(self):
        self.playerA.reset_players_games(), self.playerB.reset_players_games()

    def change_server(self):
        # Change who has the serve and who recieves the serve
        if self.server == self.playerA:
            self.server = self.playerB
            self.reciever = self.playerA
        else:
            self.server = self.playerA
            self.reciever = self.playerB

    def sim_set(self):
        while not self.SetisOver():
            self.sim_game()
            self.print_game_score()
            self.resetPoints()
            self.change_server()
        a, b = self.getGames()
        if a > b:
            self.playerA.inc_set()
        else:
            self.playerB.inc_set()
        print('---------------------------------')

    def SetisOver(self):
        a,b = self.getGames()
        return a > 5 and a-b >= 2 or b > 5 and b - a >= 2
    
    def getGames(self):
        return self.playerA.get_games(), self.playerB.get_games()

    def print_game_score(self):
        points_a,points_b = self.getPoints()
        game_a,game_b = self.getGames()
        server = self.getServer()
        # Tennis_scores = {0:'0', 1: '15', 2: '30', 3:'40'}
        # if points_a > points_b:
        #     points_a = Tennis_scores.get(points_a, 'adv')
        #     points_b = Tennis_scores.get(points_b, '40')
        # else:
        #     points_a = Tennis_scores.get(points_a, '40')
        #     points_b = Tennis_scores.get(points_b, 'adv')
            
        print(f'A {points_a}:{points_b} B ==> {game_a}:{game_b} it was {server} to serve')

    def getSets(self):
        return self.playerA.get_set(), self.playerB.get_set()

    def matchOver(self):
        a,b = self.getSets()
        return a > 2 or b > 2

    def play(self):
        while not self.matchOver():
            self.nextSet()
            self.sim_set()
            self.resetGames()
            self.swapFirstServe()

    def getServer(self):
        if self.server == self.playerA:
            return 'PlayerA'
        else:
            return 'PlayerB'

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
    a = float(input('Define winning percentage of player A when serving: '))
    b = float(input('Define winning percentage of player B when serving: '))
    return a,b

def output(match_res):
    a,b = match_res.getSets()
    winner = 'PlayerA'
    if a > b:
        print(f'{winner} wins with a score of {a}:{b}')
    else:
        winner = 'PlayerB'
        print(f'{winner} wins with a score of {a}:{b}')

def main():

    ProbA, ProbB = input_player()
    Game = Tennis_match(ProbA, ProbB)
    Game.coin_toss()
    Game.play()
    output(Game)

if __name__ == '__main__':
    main()

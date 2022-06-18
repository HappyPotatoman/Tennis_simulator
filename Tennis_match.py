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
        self.set_num = 1

    def coin_toss(self):
        if random.uniform(0,1) <= 0.5:
            print(f'\n PlayerB has won the coin toss! \n')
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
        self.set_num += 1

    def Set_num(self):
        return self.set_num
            
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
        print('-----------------------')

    def SetisOver(self):
        a,b = self.getGames()
        return a > 5 and a-b >= 2 or b > 5 and b - a >= 2
    
    def getGames(self):
        return self.playerA.get_games(), self.playerB.get_games()

    def print_game_score(match_res):
        points_a,points_b = match_res.getPoints()
        game_a,game_b = match_res.getGames()

        print(f'A {points_a}:{points_b} B ==> {game_a}:{game_b}')

    def getSets(self):
        return self.playerA.get_set(), self.playerB.get_set()

    def matchOver(self):
        a,b = self.getSets()
        return a > 2 or b > 2

    def play(self):
        while not self.matchOver():
            self.sim_set()
            self.nextSet()
            self.resetGames()
            self.change_server() # Who has the frist serve?

def input_player():
    # Input chances of player to win point if he is serving
    a = float(input('Define winning percentage of player A when serving: '))
    b = float(input('Define winning percentage of player B when serving: '))
    return a,b

def output(match_res):
    a,b = match_res.getSets()
    num = match_res.Set_num()
    winner = 'PlayerA'
    # Tennis_scores = {'0':0, '1': 15, '2': 30, '3':40}
    # a = Tennis_scores.get(a, 'adv')
    # b = Tennis_scores.get(b, 'adv')
    if a > b:
        print(f'The winner of the {num}. set is: {winner} with the score: {a}:{b}')
    else:
        winner = 'PlayerB'
        print(f'The winner of the {num}. set is: {winner} with the score: {a}:{b}')

def main():

    ProbA, ProbB = input_player()
    Game = Tennis_match(ProbA, ProbB)
    Game.coin_toss()
    Game.play()
    output(Game)

if __name__ == '__main__':
    main()

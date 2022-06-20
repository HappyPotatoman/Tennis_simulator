# Tennis_simulator
It's a script that simulates tennis matches.

Version 0.1.2: Introduced tiebreaks at the ends of sets. If the match goes to 5 sets the tiebreaker is a first to 10 point game instead of a first to 7 point tiebreaker. Also cleaned up the code by introducing some new methods to eliminate code duplication and grouped the methods of the class Match to improve readability.

Version 0.1.1: Corrected the switch of server on start of new set.

Version 0.1: Defines the basic logic of a tennis match between two players. This includes simulation of the most basic component of a tennis match **a point**. From a played point we then added additional components such as games and sets. The script asks for a simple input; the probability player serving wins the point. This input is for now very basic, but leaves room for improvement and more complex logic of how a point is played. 
Some functional ideas to pursue and add to the current state of the script are: 
 - The percentages of the first and second serve. Maybe even a off chance of a let call (ball touches the net when served),
 - Chance of player to return serve,
 - Maybe we can split the chances into three parameters: Serve, attack, defence,
 - Introduction of different play conditions (grass, clay and the other one).

Some structural ideas to improve script readability are:
 - Split the Tennis_match class into subclasses: Point, Game, Set

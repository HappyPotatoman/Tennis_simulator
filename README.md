# Tennis_simulator
It's a script that simulates tennis matches.
Version 0.1: Define the basic logic of a tennis match. This includes simulation of the most basic component of a tennis match **a point**. From a played point we then added additional components such as games and sets. The script asks for a simple input; the probability player serving wins the point. This input is for now very basic, but leaves room for improvement and more complex logic of how a point is played. 
Some functional ideas to pursue and add to the current state of the script are: 
 - The percentages of the first and second serve. Maybe even a off chance of a let call (ball touches the net when served),
 - Chance of player to return serve,
 - Maybe we can split the chances into three parameters: Serve, attack, defence,
 - Introduction of different play conditions (grass, clay and the other one).
Some structural ideas to improve script readability are:
 - Split the Tennis_match class into subclasses: Point, Game, Set

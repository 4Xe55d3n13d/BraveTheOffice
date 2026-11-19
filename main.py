import random
import item
import game
import sys
from argparse import ArgumentParser
    
def main(name, randomizer, challenge, logs):
    '''Creates either a Game or Logging_Game object depending on arguments given and starts the game. 
    
        Args:
            name (str): the name to be used to name the Player_Item object.
            randomizer (bool): Option to enable stat randomization for the player if True.
            challenge (bool): Option to enable challenge mode if True.
            logs (bool): Whether or not a player wants to log their game.
    '''
    if logs:
        newgame = game.Logging_Game(name, randomizer, challenge)
        newgame.play()
    else:
        newgame = game.Game(name, randomizer, challenge)
        newgame.play()    

def parse_args(arglist):
    '''Parses command-line arguments.

    The following optional command-line arguments are defined:

    -r / --randomizer: randomizes the player's stats competely.
        (action: 'store_true')
    
    -c / --challenge: enables challenge mode, making encounters more difficult by raising the stats of the enemies.
        (action: 'store_false')
        
    -l / --logs: logs a player's run in a text file.
        (action: 'store_true')

    Args:
        arglist (list of str): a list of command-line arguments.

    Returns:
        namespace: a namespace with variables 
    '''
    parser = ArgumentParser()
    parser.add_argument('-n', '--name', type = str, default = "Hero",
                        help="Name your character.")
    parser.add_argument('-r', '--randomizer', action = 'store_true',
                        help="Option to randomizes the player's stats competely.")
    parser.add_argument('-c', '--challenge', action = 'store_false',
                        help="Option to enable challenge mode, making encounters more difficult.")
    parser.add_argument('-l', '--logs', action = 'store_true',
                        help="Option to log a player's run.")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.name, args.randomizer, args.challenge, args.logs)
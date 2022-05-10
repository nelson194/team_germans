####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

<<<<<<< HEAD
team_name = 'German'
strategy_name = 'Collude but retaliate'
strategy_description = '''
=======
team_name = 'Germans'
strategy_name = 'Collude but retaliate'
strategy_description = '''\
>>>>>>> d8e645b0f752e1fa592085301b48b82c3a838108
Collude first round. Collude, except in a round after getting 
a severe punishment.'''
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    if len(my_history)==0: # It's the first round; collude.
        return 'c'
<<<<<<< HEAD
    elif my_history[-1]=='c' and their_history[-1]=='b':
        return 'b' # Betray if they were severely punished last time,
    else:
        return 'c' # otherwise collude.

if len(my_history)==0: #first round
    return 'b'
elif my_history[-1]=='b' and thier_history[-1]=='b':
    return 'c'
else:
    return 'b'
=======
    elif my_history[-1]=='c' and their_history[-1]=='b' or my_history[-1]=='b' and their_history[-1]=='b' or my_history[-1]=='b' and their_history[-1]=='c':
        return 'b' # Betray if they were severely punished last time,
    #elif my_history[-1]=='c' and their_history[-1]=='c':
    #    return 'c'
    else:
        return 'c' # otherwise collude.

>>>>>>> d8e645b0f752e1fa592085301b48b82c3a838108

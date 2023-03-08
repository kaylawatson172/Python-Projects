import math
import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower() # converts letter input to lowercase in case user types uppercase
    computer = random.choice(['r', 'p', 's']) # computer randomly chooses from this set

    if user == computer: # r,r; p,p; s,s
        return (0, user, computer)
    if is_win(user, computer):
        return (1, user, computer)
    return (-1, user, computer)

def is_win(player, opponent):
    # winning conditions: r>s, p>r, s>p
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
    return False

def play_best_of(n): # "best of n games" meaning play until someone wins majority of n games
    # winner must win ceil(n/2) games, meaning you must win half; if n is odd, it rounds up to the nearest whole number
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        if result == 0: # tie
            print('You both chose {}. It is a tie.'.format(user))
        elif result == 1: # user wins
            player_wins += 1 # if user wins, score increases by 1
            print('You chose {}. The computer chose {}. You win! \n'.format(user, computer))
        else:
            computer_wins += 1
            print('You chose {}. The computer chose {}. You lose :( \n'.format(user, computer))

    if player_wins > computer_wins:
        print('You won the best of {} games \n'.format(n))
    else:
        print('The computer won the best of {} games. You will get em next time! \n'.format(n))


if __name__ == '__main__':
    play_best_of(3)
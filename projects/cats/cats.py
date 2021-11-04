"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    # selectable paragraphs
    sps = list(filter(select, paragraphs))
    if k < len(sps):
        return sps[k]
    else:
        return ''
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    def contain_topic_words(s):
        s = remove_punctuation(s).lower()
        # check if any words in the paragraph contained in the topic words
        return any(map(lambda w:w in topic, s.split()))
    return contain_topic_words
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    if len(typed_words) == 0:
        return 0.0
    correct = 0
    for t, r in zip(typed_words, reference_words):
        if t == r:
            correct += 1
    return correct / len(typed_words) * 100
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    return len(typed)/5 * (60.0/elapsed)
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    if user_word in valid_words:
        return user_word
    least_diff_word = min(valid_words,
                          key=lambda vw: diff_function(user_word, vw, limit))
    if diff_function(user_word, least_diff_word, limit) <= limit:
        return least_diff_word
    return user_word
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    if start == goal:
        return 0
    elif limit == 0:
        return 1
    elif start == '' or goal == '':
        return max(len(start), len(goal))
    elif start[0] == goal[0]:
        return 0 + shifty_shifts(start[1:], goal[1:], limit)
    else:
        return 1 + shifty_shifts(start[1:], goal[1:], limit-1)
    # END PROBLEM 6

def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    #assert False, 'Remove this line'
    
    if start == goal:
        return 0
    elif limit == 0:
        return 1
    elif start == '' or goal == '':
        return max(len(start), len(goal))
    elif start[0] == goal[0]:
        return pawssible_patches(start[1:], goal[1:], limit)
    else:
        add_diff = 1 + pawssible_patches(start, goal[1:], limit-1)
        remove_diff = 1 + pawssible_patches(start[1:], goal, limit-1)
        substitute_diff = 1 + pawssible_patches(start[1:], goal[1:], limit-1)
        return min(add_diff, remove_diff, substitute_diff) 


def final_diff(start, goal, limit):
    """A diff function. 

    based on the implementation of pawssible_patches, more ideas are involved
    - treat deleting one of two repetitive letters as no change
    - treat swapped adjacent letters as a one change
    - incorporate common mispelling
    """
    #assert False, 'Remove this line to use your final_diff function'
    common_misspellings = {'absense': 'absence',
                           'acceptible': 'acceptable',
                           'judgement': 'judgment',
                           'lightening': 'lightning',
                           'maintainance': 'maintenance'}
    if start == goal:
        return 0
    elif start in common_misspellings:
        return final_diff(common_misspellings[start], goal, limit)
    elif limit == 0:
        return 1
    elif start == '' or goal == '':
        return max(len(start), len(goal))
    elif start[0] == goal[0]:
        return final_diff(start[1:], goal[1:], limit)
    else:
        # check misspe
        add_diff = 1 + final_diff(start, goal[1:], limit-1)
        remove_diff = 1 + final_diff(start[1:], goal, limit-1)
        substitute_diff = 1 + final_diff(start[1:], goal[1:], limit-1)
        if len(start) > 1:
            swap_diff = 1 + final_diff(swap_first_letters(start), goal, limit-1)
            if start[0] == start[1]:
                del_rep_diff = final_diff(start[1:], goal, limit)
            
            return min(add_diff, remove_diff, substitute_diff, swap_diff, del_rep_diff) 
        return min(add_diff, remove_diff, substitute_diff) 

def swap_first_letters(string):
    """ Swap the letters at index 0 and 1 """
    return string[1] + string[0] + string[2:]
    
    



###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    total_words = len(prompt)
    count = 0
    for tp, ans in zip(typed, prompt):
        if tp == ans:
            count+=1
        else:
            break
    ratio = count/total_words
    send({'id': user_id, 'progress': ratio})
    return ratio
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    times = []
    for ts in times_per_player:
        i,j = 0, 1
        pt = []
        while j < len(ts):
            pt.append(ts[j]-ts[i])
            i,j = i+1, j+1
        times.append(pt)
    return game(words, times)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    records = [[] for _ in player_indices] # create the list of lists to return
    for w_ind in word_indices: # words are not repetive in the lists
        p_ind_fastest = sorted(
                player_indices, key=lambda p_ind: time(game, p_ind, w_ind))[0]
        records[p_ind_fastest].append(word_at(game, w_ind))
    return records
    # END PROBLEM 10

def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)

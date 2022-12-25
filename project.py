#!/usr/bin/env python

from dic import clues, colors, distribution
import regex as reg
import sys

__author__ = "Manuel J. Adams"
__version__ = "1.1"

words = open('word_list.txt').read()
word_list = reg.findall('(?<=\n).{5}(?=\n)', words)

def main(): # collects your input
    while True:
        try:
            guess = input('Guess: ').strip().lower()        # accepts AROSE, roBOT, japan
        except:
            sys.exit('\n\nThanks for playing!\n')
        if not guess:
            if not input('Press enter again to exit program'):
                break
            else:
                continue
        if not reg.fullmatch(r'[a-z]{5}', guess):
            print('Enter 5-letter word')
            continue
        if guess not in word_list:
            print('Warning: guess not in word list!')
        while True:
            try:
                clue = input('Clue: ').strip().lower()      # accepts abbAc, 12213
            except:
                sys.exit('\n\nThanks for playing!\n')
            if not reg.fullmatch(r'([a-c]|[1-3]){5}', clue):
                print('Enter clue (a-c / 1-3)')
                continue
            break
        clues = add_clue(guess, clue)
        possible_words = get_possible_words(clues)
        best_words = get_best_words(possible_words)
        for k,v in best_words.items():                      # prints possible words sorted by score
            print(k, v)
        print(len(best_words), 'words')

def add_clue(guess, clue):
    for i in range(5):
        clues[i+1][colors[clue[i]]] += guess[i]
    return clues

def get_possible_words(clues):
    regex_yellows, regex_green, regex_yellow, greys = [], '', '', ''
    for k, v in clues.items():                               # loops over clues to create regular expressions
#GREEN
        g = v['green']
        regex_green = regex_green + g[0] if g else regex_green + '.'
#YELLOW
        y = v['yellow']
        regex_yellow = regex_yellow + '[^'+y+']' if y else regex_yellow + '.'
        if y:
            for char in y:
                regex = '.*' + char + '.*'
                regex_yellows.append(regex) if not regex in regex_yellows else None
#GREY
    for k, v in clues.items():
        g = v['grey']
        for char in g:
            if not char in regex_green and not char in regex_yellow:
                greys = greys + char # adds letter only to grey list (i.e. blocks it) if not needed per green or yellow
    regex_greyandword = '(?<=\n).{5}(?=\n)' if not greys else '(?<=\n)[^' + greys + ']{5}(?=\n)'
    matches = reg.findall(regex_greyandword, words, reg.IGNORECASE)         # filters out grey, and also creates word list
    regexes = regex_yellows + [regex_yellow] + [regex_green]     # all the regular expressions a possible word must match, except grey
    possible_words = []
    for word in matches:
        possible = True
        for regex in regexes:
            if not reg.fullmatch(regex, word):      # apply all regular expressions
                possible = False
                break
        possible_words.append(word) if possible else None
    return possible_words

def get_best_words(words):                          # sort words by score (based on frequency of letters in word list itself)
    count_dic = {}
    for word in words:
        value, letters = 0, ''
        for char in word:
            value = value + distribution[char] if not char in letters else value # add value for same letter only once
            letters += char
        count_dic[word] = value
    count_dic_sorted = {k: v for k, v in sorted(count_dic.items(), key=lambda item: item[1])}
    return count_dic_sorted

if __name__ == '__main__':
    main()


from project import add_clue, get_possible_words, get_best_words
from dic import clues

def test_add_clue():
    len_before = len(clues[2]['yellow'])
    add_clue('arose', '32333')
    add_clue('flirt', 'ccaab')
    len_after = len(clues[2]['yellow'])
    assert len_after - len_before == 1
    assert len(clues[4]['green']) == 1
    assert clues[3]['grey'][-1] == 'o'

def test_get_possible_words():
    assert get_possible_words(clues) == ['twirp', 'third', 'twirk']

def test_get_best_words():
    dic = get_best_words(['python', 'c', 'potter'])
    assert dic['c'] == 2744


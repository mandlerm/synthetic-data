import itertools
import sys
import csv
import word_strings
import starter_grammars as sg
from nltk.grammar import Nonterminal
from nltk.grammar import CFG


def generate(grammar, start=None, depth=None, n=None):
    """
    Generates an iterator of all sentences from a CFG.

    :param grammar: The Grammar used to generate sentences.
    :param start: The Nonterminal from which to start generate sentences.
    :param depth: The maximal depth of the generated tree.
    :param n: The maximum number of sentences to return.
    :return: An iterator of lists of terminal tokens.
    """
    if not start:
        start = grammar.start()
    if depth is None:
        depth = sys.maxsize

    iter = _generate_all(grammar, [start], depth)

    if n:
        iter = itertools.islice(iter, n)

    return iter


def _generate_all(grammar, items, depth):
    if items:
        try:
            for frag1 in _generate_one(grammar, items[0], depth):
                for frag2 in _generate_all(grammar, items[1:], depth):
                    yield frag1 + frag2
        except RuntimeError as _error:
            if _error.message == "maximum recursion depth exceeded":
                # Helpful error message while still showing the recursion stack.
                raise RuntimeError(
                    "The grammar has rule(s) that yield infinite recursion!!"
                ) from _error
            else:
                raise
    else:
        yield []


def _generate_one(grammar, item, depth):
    if depth > 0:
        if isinstance(item, Nonterminal):
            for prod in grammar.productions(lhs=item):
                for frag in _generate_all(grammar, prod.rhs(), depth - 1):
                    yield frag
        else:
            yield [item]


def _execute_hs(hs_grammar):
    # hs_file = open("hs_test_pre_run.csv", "a+")
    # hs_fw = csv.writer(hs_file)
    # hs_fw.writerow(['text', 'hate-speech'])

    grammar = CFG.fromstring(hs_grammar)
    for n, sent in enumerate(generate(grammar), 1):
        # hs_fw.writerow([" " .join(sent), "true"])
        print("%3d. %s" % (n, " ".join(sent)))
    # hs_file.close()

def _execute_clean(grammar):
    # hs_file = open("hs_test_pre_run.csv", "a+")
    # hs_fw = csv.writer(hs_file)
    # hs_fw.writerow(['text', 'hate-speech'])

    grammar = CFG.fromstring(grammar)
    for n, sent in enumerate(generate(grammar), 1):
        # hs_fw.writerow([" " .join(sent), "true"])
        print("%3d. %s" % (n, " ".join(sent)))
    # hs_file.close()

def _execute_false_pg(grammar):
    # hs_file = open("hs_test_pre_run_false_pg.csv", "a+")
    # hs_fw = csv.writer(hs_file)
    # hs_fw.writerow(['text', 'hate-speech'])

    grammar = CFG.fromstring(grammar)
    for n, sent in enumerate(generate(grammar), 1):
        # hs_fw.writerow([" " .join(sent), "true"])
        print("%3d. %s" % (n, " ".join(sent)))
    # hs_file.close()

def _execute_false_non_pg(grammar):
    # hs_file = open("hs_test_pre_run_false_non_pg.csv", "a+")
    # hs_fw = csv.writer(hs_file)
    # hs_fw.writerow(['text', 'hate-speech'])

    grammar = CFG.fromstring(grammar)
    for n, sent in enumerate(generate(grammar), 1):
        # hs_fw.writerow([" " .join(sent), "true"])
        print("%3d. %s" % (n, " ".join(sent)))
    # hs_file.close()


# S -> Pre_hs NPh | NPh VPa_past_benign | Nh_clean HS_clause | Vt_hs_present PPp | Adj_hs PPp
def hs_grammar():
    g = '''
    S -> Pre_hs NPh 
    PgN ->  PPs | PPp 
    Noun_clean -> Animals | Food | Humans
    Animals -> N_animals_single | N_animals_plural
    Food -> N_food_single | N_food_plural
    Humans -> N_human_single | N_human_plural

    NPh -> Adj_hs PgN | Det Adj_hs PgN | Adv_hs Adj_hs PgN | Det Adv_hs Adj_hs PgN 
    VPa_past_benign -> Vt_clean_past Noun_clean Adv_clean | Vt_clean_past PgN | Vt_clean_past Noun_clean | Vt_clean_past Det Adj_hs Noun_clean

    Nh_clean -> Det Humans Vt_clean_past  
    HS_clause -> Det Adj_hs PgN | Det N_hate_speech_single | Det N_hate_speech_plural | Vt_hs_past PgN | Vt_hs_past Det Adj_hs PgN 
    
    Vt_hs_present -> 'burn'
    Vt_clean_past -> 'swept'
    Det -> 'the'
    Pre_hs -> 'you are'
    Adj_hs -> 'dirty'
    Adv_hs -> 'fucking'
    Adj_clean -> 'lovely'
    Adv_clean -> 'softly'
    PPs -> 'Jew'
    PPp -> 'Jews'
    N_animals_single -> 'dog'
    N_animals_plural -> 'dogs'
    N_food_single -> 'pizza'
    N_food_plural -> 'burgers'
    N_human_single -> 'doctor'
    N_human_plural -> 'nurses'
    N_hate_speech_single -> 'lesbo'
    N_hate_speech_plural -> 'faggots'

    '''
    return g

def hs_grammar_false_pg():
    g = '''
    Pre_hs_false -> 'you are'
    Det -> 'a'
    Adj_clean -> 'brisk'
    Adv_clean -> 'sweetly'
    Vt_clean_past -> 'threw'
    Vt_clean_present -> 'help'
    N_human_single -> 'mom'
    N_human_plural -> 'doctors'
    N_food_single -> 'banana' | 'pizza'
    N_food_plural -> 'cakes'
    N_animal_single -> 'kangaroo'
    N_animal_plural -> 'bears'
    Animals -> N_animal_single | N_animal_plural
    PPs -> 'Jew'
    PPp -> 'Jews'
    '''
    return sg.hs_grammar_false_pg() + g


def hs_grammar_false_non_pg():
    g = '''
    Pre_hs_false -> 'you are'
    Det -> 'a'
    Adj_clean -> 'brisk'
    Adv_clean -> 'sweetly'
    Vt_clean_past -> 'threw'
    Vt_clean_present -> 'help'
    Adj_hs -> 'dirty'
    Adv_hs -> 'fucking'
    Vt_hs_past -> 'gassed'
    Vt_hs_present -> 'burn'
    N_human_single -> 'mom'
    N_human_plural -> 'doctors'
    N_food_single -> 'banana' | 'pizza'
    N_food_plural -> 'cakes'
    N_animals_single -> 'kangaroo'
    N_animal_plural -> 'bears'
    Animals -> N_animal_single | N_animal_plural

    '''
    return sg.hs_grammar_false_non_pg() + g




def clean():
    str =  '''
    Pre_clean -> 'you are'
    Det -> 'a'
    Adj_clean -> 'aboard'
    Adv_clean -> 'sweetly'
    Vt_clean_past -> 'threw'
    Vt_clean_present -> 'help'
    N_human_single -> 'mom'
    N_human_plural -> 'doctors'
    N_food_single -> 'banana' | 'pizza'
    N_food_plural -> 'cakes'
    N_animal_single -> 'kangaroo'
    N_animal_plural -> 'bears'
    Animals -> N_animal_single | N_animal_plural
    
    '''
    return sg.clean_grammar() + str

if __name__ == "__main__":
    # grammar = hs_grammar()
    # _execute_hs(grammar)
    # grammar = clean()
    # _execute_clean(grammar)
    # grammar = hs_grammar_false_pg()
    # print(grammar)
    # _execute_false_non_pg(grammar)

    grammar = hs_grammar_false_non_pg()
    print(grammar)
    _execute_false_non_pg(grammar)
    # print(grammar)

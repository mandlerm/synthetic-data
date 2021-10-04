
import itertools
import sys
import csv
# sys.path.insert(0, '~/Code/synthetic_data\modules')

import word_strings
import starter_grammars_v4 as sg
from nltk.grammar import Nonterminal
from nltk.grammar import CFG


########### Execute methods. Run the grammar script and output to csv
def _execute_clean(grammar, filename):
    f = open(filename, "a+")
    fw = csv.writer(f)
    fw.writerow(['lan', 'text', 'hate-speech'])
    g = CFG.fromstring(grammar)

    for n, sent in enumerate(generate(g), 1):
        fw.writerow(['eng', " ".join(sent), 0])
        print(f"eng, {' '.join(sent)}, 0")
  
    f.close()


###########  Grammar generation methods
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

######### Set up methods. Acquire the correct grammar
def _setup_version_v2_4():

    str = sg.surgical_clean_grammar() + word_strings.prof_plural() + word_strings.prof_single() + word_strings.noun_animals_plural() + word_strings.noun_animals_singular() + word_strings.protected_groups_plural() + word_strings.protected_groups_single() + word_strings.adjectives_hs() + word_strings.noun_human_plural() + word_strings.noun_human_single() + word_strings.adjectives_neg() + word_strings.protected_group_adj() + word_strings.noun_things_single() + word_strings.noun_things_plural() + word_strings.keyboard_smashes() + word_strings.noun_animals_singular_non_hs() + word_strings.noun_animals_plural_non_hs()
    
    return str


if __name__ == "__main__":
    surgical_clean = _setup_version_v2_4()
   
    # _execute_clean(surgical_clean,"v4_clean_a.csv")
    # _execute_clean(surgical_clean,"v4_clean_b.csv")
    # _execute_clean(surgical_clean,"v4_clean_c.csv")
    # _execute_clean(surgical_clean,"v4_clean_d.csv")
    _execute_clean(surgical_clean,"v4_clean_e.csv")
    # _execute_clean(surgical_clean,"v4_clean_f.csv")
    # _execute_clean(surgical_clean,"v4_clean_g.csv")
    # _execute_clean(surgical_clean,"v4_clean_h.csv")
    # _execute_clean(surgical_clean,"v4_clean_i.csv")
    # _execute_clean(surgical_clean,"v4_clean_j.csv")
    # _execute_clean(surgical_clean,"v4_clean_k.csv")
    # _execute_clean(surgical_clean,"v4_clean_l.csv")
   
 
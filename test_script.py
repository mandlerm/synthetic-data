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
    hs_file = open("hs_testing_short.csv", "a+")
    hs_fw = csv.writer(hs_file)
    hs_fw.writerow(['text', 'hate-speech'])

    grammar = CFG.fromstring(hs_grammar)
    for n, sent in enumerate(generate(grammar), 1):
        hs_fw.writerow([" " .join(sent), "true"])
        print("%3d. %s" % (n, " ".join(sent)))

    hs_file.close()


def hs_grammar():
    g = '''
    S -> Pre NPh | NPh VPa | NPh VPb | NPh VPc

    NPh -> Adjhs PgN | Det Adjhs PgN | Advhs Adjhs PgN | Det Advhs PgN | Det Advhs Adjhs PgN  

    VPa -> Vt PgN | Vt Ns | Vt PgN Adjhs | Vt Ns Adjhs 
    VPb -> Vi | Vi Advhs
    VPc -> Vd Nhs Ns | Vd Nhs Ns Advhs

    Pre -> 'you are' | 'she is'
    Det -> 'a' | 'the'
    Adjhs -> 'dirty' | 'awful' | 'retarted'
    Advhs -> 'violently' | 'terribly' | 'miserably'

    PgN -> 'Jew' | 'Christian'
    Vt -> 'gassed' | 'choked'
    Ns -> 'kangaroo' | 'rice'
    Vi -> 'burnt' | 'fought' 
    Vd -> 'rid' | 'suspected'
    Nhs -> 'nurse' | 'sister' 
    '''
    return g



if __name__ == "__main__":
    grammar = hs_grammar()
    print(grammar)

    _execute_hs(grammar)
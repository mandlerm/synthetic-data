
import itertools
import sys
import csv
import word_strings
import starter_grammars as sg
from nltk.grammar import Nonterminal
from nltk.grammar import CFG


def _hs_testing():
    #### hs_pre_nph
    # str = sg.hs_pre_nph() + word_strings.pre_hs() + word_strings.determiners() + word_strings.protected_groups_single() + word_strings.protected_groups_plural() + word_strings.adjectives_hs() + word_strings.adverbs_hs() + word_strings.vt_hs() + word_strings.vi_hs() + word_strings.vd_hs()
    # hs_file = open("hs_pre_nph3.csv", "a+")
    # hs_fw = csv.writer(hs_file)
    # hs_fw.writerow(['text', 'hate-speech'])

    # grammar = CFG.fromstring(str)
    # for n, sent in enumerate(generate(grammar), 1):
    #     hs_fw.writerow([" " .join(sent), "true"])
    #     print("%3d. %s" % (n, " ".join(sent)))

    # hs_file.close()

    ### hs_pnh_vpa
    # str = sg.hs_pnh_vpa() + word_strings.pre_hs() + word_strings.determiners() + word_strings.protected_groups_single() + word_strings.protected_groups_plural() + word_strings.adjectives_hs() + word_strings.adverbs_hs() + word_strings.vt_hs() + word_strings.vi_hs() + word_strings.vd_hs()
    # hs_file = open("hs_pnh_vpa5.csv", "a+")
    # hs_fw = csv.writer(hs_file)
    # hs_fw.writerow(['text', 'hate-speech'])

    # grammar = CFG.fromstring(str)
    # for n, sent in enumerate(generate(grammar), 1):
    #     hs_fw.writerow([" " .join(sent), "true"])
    #     print("%3d. %s" % (n, " ".join(sent)))

    # hs_file.close()

    # #### hs_nph_vpb
    # str = sg.hs_nph_vpb() + word_strings.pre_hs() + word_strings.determiners() + word_strings.protected_groups_single() + word_strings.protected_groups_plural() + word_strings.adjectives_hs() + word_strings.adverbs_hs() + word_strings.vt_hs() + word_strings.vi_hs() + word_strings.vd_hs()
    # hs_file = open("hs_nph_vpb3.csv", "a+")
    # hs_fw = csv.writer(hs_file)
    # hs_fw.writerow(['text', 'hate-speech'])

    # grammar = CFG.fromstring(str)
    # for n, sent in enumerate(generate(grammar), 1):
    #     hs_fw.writerow([" " .join(sent), "true"])
    #     print("%3d. %s" % (n, " ".join(sent)))

    # hs_file.close()

    ####  hs_nph_vpc
    str = sg.hs_nph_vpc() + word_strings.pre_hs() + word_strings.determiners() + word_strings.protected_groups_single() + word_strings.protected_groups_plural() + word_strings.adjectives_hs() + word_strings.adverbs_hs() + word_strings.vt_hs() + word_strings.vi_hs() + word_strings.vd_hs() + word_strings.noun_humans_single() +  word_strings.noun_things_single()
    hs_file = open("hs_nph_vpc5.csv", "a+")
    hs_fw = csv.writer(hs_file)
    hs_fw.writerow(['text', 'hate-speech'])

    grammar = CFG.fromstring(str)
    for n, sent in enumerate(generate(grammar), 1):
        print("%3d. %s" % (n, " ".join(sent)))
        hs_fw.writerow([" " .join(sent), "true"])

    hs_file.close()


def _setup_clean_grammar():
    str = sg.clean_grammar() + word_strings.pre_clean() + word_strings.determiners() + word_strings.noun_things_single() + word_strings.noun_things_plural() + word_strings.noun_humans_single() + word_strings.noun_humans_plural() + word_strings.adjectives_clean() + word_strings.adverbs_clean() + word_strings.vt_clean() + word_strings.vi_clean() + word_strings.vd_clean()
    return str

def _setup_hs_false_grammar():
    str = sg.hs_grammar_false() + word_strings.pre_hs_false() + word_strings.determiners() + word_strings.noun_things_single() + word_strings.noun_things_plural() + word_strings.noun_humans_single() + word_strings.noun_humans_plural() + word_strings.adjectives_hs() + word_strings.adverbs_hs() + word_strings.vt_hs() + word_strings.vi_hs() + word_strings.vd_hs()
    return str

def _setup_hs_grammar():
    str = sg.hs_grammar() + word_strings.pre_hs() + word_strings.determiners() + word_strings.protected_groups_single() + word_strings.protected_groups_plural() + word_strings.noun_humans_single() + word_strings.adjectives_hs() + word_strings.adverbs_hs() + word_strings.vt_hs() + word_strings.vi_hs() + word_strings.vd_hs() + + word_strings.noun_things_single()
    return str


def _execute_clean(clean_grammar):
    clean_file = open("hs_clean.csv", "a+")
    clean_fw = csv.writer(clean_file)
    clean_fw.writerow(['text', 'hate-speech'])

    grammar = CFG.fromstring(clean_grammar)
    for n, sent in enumerate(generate(grammar), 1):
        clean_fw.writerow([" " .join(sent), "false"])
        print("%3d. %s" % (n, " ".join(sent)))
  
    clean_file.close()


def _execute_hs(hs_grammar):
    hs_file = open("hs_true.csv", "a+")
    hs_fw = csv.writer(hs_file)
    hs_fw.writerow(['text', 'hate-speech'])

    grammar = CFG.fromstring(hs_grammar)
    for n, sent in enumerate(generate(grammar), 1):
        hs_fw.writerow([" " .join(sent), "true"])
        print("%3d. %s" % (n, " ".join(sent)))

    hs_file.close()


def _execute_hs_false(hs_false_grammar):
    hs_false_file = open("hs_false.csv", "a+")
    hs_false_fw = csv.writer(hs_false_file)
    hs_false_fw.writerow(['text', 'hate-speech'])

    grammar = CFG.fromstring(hs_false_grammar)
    for n, sent in enumerate(generate(grammar), 1):
        hs_false_fw.writerow([" " .join(sent), "false"])
        print("%3d. %s" % (n, " ".join(sent)))

    hs_false_file.close()



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


def demo(N=10):
    pass
    # f1 = "clean_text.csv"
    # clean_file = open(f1, "a+")
    # clean_fw = csv.writer(clean_file)
    # clean_fw.writerow(['text', 'hate-speech'] )
    

    ##############  HS  ###############
    # f2 = "hs_trues.csv"
    # hs_file = open(f2, "a+")
    # hs_fw = csv.writer(hs_file)
    # hs_fw.writerow(['text', 'hate-speech'] )
    # hs_count = 0

    # grammar = CFG.fromstring(hs_grammar)
    # for n, sent in enumerate(generate(grammar, n=N), 1):  # optional second argument to limit number of outputs
    # for n, sent in enumerate(generate(grammar), 1):
        # hs_fw.writerow([" " .join(sent), "true"])
        # hs_count += 1
        # print("%3d. %s" % (n, " ".join(sent)))



    ##############  FAKE-HS  ###############
    # f2 = "hs_falses.csv"
    # hs_falses_file = open(f2, "a+")
    # falses_fw = csv.writer(hs_falses_file)
    # falses_fw.writerow(['text', 'hate-speech'] )
    # hs_false_count = 0

    # grammar = CFG.fromstring(hs_grammar_falses)
    # print(grammar)
    # # for n, sent in enumerate(generate(grammar, n=N), 1):  # optional second argument to limit number of outputs
    # for n, sent in enumerate(generate(grammar), 1):
    #     falses_fw.writerow([" " .join(sent), "false"])
    #     hs_false_count += 1
        # print("%3d. %s" % (n, " ".join(sent)))


    # ##############  CLEAN  ###############
    # f2 = "clean_text.csv"
    # clean_file = open(f2, "a+")
    # clean_fw = csv.writer(clean_file)
    # clean_fw.writerow(['text', 'hate-speech'] )
    # clean_count = 0

    # grammar = CFG.fromstring(clean_grammar)
    # # for n, sent in enumerate(generate(grammar, n=N), 1):  # optional second argument to limit number of outputs
    # for n, sent in enumerate(generate(grammar), 1):
    #     clean_fw.writerow([" " .join(sent), "false"])
    #     clean_count += 1
    #     print("%3d. %s" % (n, " ".join(sent)))


    # print(f"HS: {hs_count}, CLEAN: {clean_count}, False signal: {hs_false_count}")

    # print(f"HS: {hs_count}")


if __name__ == "__main__":
    # clean_grammar = _setup_clean_grammar()
    # _execute_clean(clean_grammar)

    # hs_false_grammar = _setup_hs_false_grammar()
    # _execute_hs_false(hs_false_grammar)
    
    # hs_grammar = _setup_hs_grammar()
    # _execute_hs(hs_grammar)

    _hs_testing()

    

    

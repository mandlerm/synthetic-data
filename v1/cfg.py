
import itertools
import sys
import csv
import word_strings
import starter_grammars as sg
from nltk.grammar import Nonterminal
from nltk.grammar import CFG

######### Set up methods. Acquire the correct grammar
def _setup_clean_grammar():
    str = sg.clean_grammar() + word_strings.pre_clean() + word_strings.determiners() + word_strings.noun_human_single() + word_strings.noun_human_plural() + word_strings.noun_food_singular() + word_strings.noun_food_plural() + word_strings.noun_animals_singular() + word_strings.noun_animals_plural() + word_strings.adjectives_clean() + word_strings.adverbs_clean() + word_strings.vt_clean_past() + word_strings.vt_clean_present()
  
    return str

def _setup_hs_grammar_false_pg():
    str = sg.hs_grammar_false_pg() + word_strings.pre_hs_false_single() + word_strings.pre_hs_false_plural() + word_strings.determiners() + word_strings.noun_things_single() + word_strings.noun_things_plural() + word_strings.noun_food_plural() + word_strings.noun_food_singular() + word_strings.noun_animals_plural() + word_strings.noun_animals_singular() + word_strings.noun_human_single() + word_strings.noun_human_plural() + word_strings.adjectives_clean() + word_strings.adverbs_clean() + word_strings.vt_clean_past() + word_strings.vt_clean_present() + word_strings.protected_groups_plural() + word_strings.protected_groups_single()
   
    return str

def _setup_hs_grammar_false_non_pg():
    str = sg.hs_grammar_false_non_pg() + word_strings.pre_hs_false_single() + word_strings.pre_hs_false_plural() + word_strings.determiners() + word_strings.noun_food_plural() + word_strings.noun_food_singular() + word_strings.noun_animals_plural() + word_strings.noun_animals_singular() + word_strings.noun_human_single() + word_strings.noun_human_plural() + word_strings.adjectives_clean() + word_strings.adverbs_clean() + word_strings.vt_clean_past() + word_strings.vt_clean_present() + word_strings.adjectives_hs() + word_strings.adverbs_hs() + word_strings.vt_hs_present() + word_strings.vt_hs_past() 
   
    return str

def _setup_hs_grammar():
    str = sg.hs_grammar() + word_strings.pre_hs_single() + word_strings.pre_hs_plural() + word_strings.determiners() + word_strings.zt_noun_plural() + word_strings.zt_noun_single() + word_strings.zt_phrase() + word_strings.zt_adj() + word_strings.protected_groups_single() + word_strings.protected_groups_plural() + word_strings.adjectives_hs() + word_strings.adjectives_clean() + word_strings.adverbs_hs() + word_strings.adverbs_clean() + word_strings.vt_hs_present() + word_strings.vt_hs_past() + word_strings.vt_clean_present() + word_strings.vt_clean_past() + word_strings.noun_human_single() + word_strings.noun_human_plural() + word_strings.noun_food_plural() + word_strings.noun_food_singular() + word_strings.noun_animals_singular() + word_strings.noun_animals_plural() + word_strings.noun_hate_speech_plural() + word_strings.noun_hate_speech_single() 

    return str

def _setup_surgical_hs():
    str = sg.surgical_hs_grammar() + word_strings.pre_hs_single() + word_strings.pre_hs_plural() + word_strings.determiners() + word_strings.zt_noun_plural() + word_strings.zt_noun_single() + word_strings.zt_phrase() + word_strings.zt_adj() + word_strings.protected_groups_single() + word_strings.protected_groups_plural() + word_strings.adjectives_hs() + word_strings.adjectives_clean() + word_strings.adverbs_hs() + word_strings.adverbs_clean() + word_strings.vt_hs_present() + word_strings.vt_hs_past() + word_strings.vt_clean_present() + word_strings.vt_clean_past() + word_strings.noun_human_single() + word_strings.noun_human_plural() + word_strings.noun_food_plural() + word_strings.noun_food_singular() + word_strings.noun_animals_singular() + word_strings.noun_animals_plural() + word_strings.noun_hate_speech_plural() + word_strings.noun_hate_speech_single() 

    return str


def _setup_version_v2_3():
    str = sg.surgical_hs_grammar() + word_strings.pre_hs_single() + word_strings.pre_hs_plural() + word_strings.determiners() + word_strings.zt_noun_plural() + word_strings.zt_noun_single() + word_strings.zt_phrase() + word_strings.zt_adj() + word_strings.protected_groups_single() + word_strings.protected_groups_plural() + word_strings.adjectives_hs() + word_strings.adjectives_clean() + word_strings.adverbs_hs() + word_strings.adverbs_clean() + word_strings.vt_hs_present() + word_strings.vt_hs_past() + word_strings.vt_clean_present() + word_strings.vt_clean_past() + word_strings.noun_human_single() + word_strings.noun_human_plural() + word_strings.noun_food_plural() + word_strings.noun_food_singular() + word_strings.noun_animals_singular() + word_strings.noun_animals_plural() + word_strings.noun_hate_speech_plural() + word_strings.noun_hate_speech_single() 

    return str


########### Execute methods. Run the grammar script and output to csv
def _execute_hs_true(clean_grammar, filename):
    f = open(filename, "a+")
    fw = csv.writer(f)
    fw.writerow(['lang', 'text', 'hatespeech'])

    grammar = CFG.fromstring(clean_grammar)
    for n, sent in enumerate(generate(grammar), 1):
        fw.writerow(['eng', " " .join(sent), 1])
        print(f"eng, {' '.join(sent)}, 1 ")
  
    f.close()

def _execute_hs_false(grammar, filename):
    
    f = open(filename, "a+")
    fw = csv.writer(f)
    fw.writerow(['row', 'text', 'hate-speech'])
    grammar = CFG.fromstring(grammar)

    for n, sent in enumerate(generate(grammar), 1):
        fw.writerow([n, " " .join(sent), 0])
        print("%3d. %s" % (n, " ".join(sent)))
  
    f.close()


def _execute_hs_false_pg(hs_false_grammar):
    hs_false_file = open("hs_false_pg.csv", "a+")
    hs_false_fw = csv.writer(hs_false_file)
    hs_false_fw.writerow(['row', 'text', 'hate-speech'])
    grammar = CFG.fromstring(hs_false_grammar)
  
    for n, sent in enumerate(generate(grammar), 1):
        hs_false_fw.writerow([n," " .join(sent), "false"])
        print("%3d. %s" % (n, " ".join(sent)))

    hs_false_file.close()

def _execute_hs_false_non_pg(hs_false_grammar):
    hs_false_file = open("hs_false_non_pg.csv", "a+")
    hs_false_fw = csv.writer(hs_false_file)
    hs_false_fw.writerow(['row', 'text', 'hate-speech'])

    grammar = CFG.fromstring(hs_false_grammar)
    for n, sent in enumerate(generate(grammar), 1):
        hs_false_fw.writerow([n," " .join(sent), "false"])
        print("%3d. %s" % (n, " ".join(sent)))

    hs_false_file.close()




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


if __name__ == "__main__":
    # hs_grammar = _setup_hs_grammar()
    # _execute_hs_true(hs_grammar, "hs_true_r3.csv")
    
    # clean_grammar = _setup_clean_grammar()
    # _execute_hs_false(clean_grammar,"hs_clean_r3.csv")

    # hs_grammar2 = _setup_hs_grammar_false_non_pg()
    # _execute_hs_false(hs_grammar2, "hs_false_non_pg_r3.csv")
    
    # hs_grammar1 = _setup_hs_grammar_false_pg()
    # _execute_hs_false(hs_grammar1,"hs_false_pg_r3.csv")

    surgical_hs = _setup_surgical_hs()
    # _execute_hs_true(surgical_hs,"./v2/v2_a.csv")
    # _execute_hs_true(surgical_hs,"./v2/v2_b.csv")
    _execute_hs_true(surgical_hs,"./v2/v2_c.csv")
    # _execute_hs_true(surgical_hs,"./v2/v2_d.csv")
    # _execute_hs_true(surgical_hs,"./v2/v2_e.csv")
    # _execute_hs_true(surgical_hs,"./v2/v2_f.csv")
    # _execute_hs_true(surgical_hs,"./v2/v2_g.csv")
    # _execute_hs_true(surgical_hs,"./v2/v2_h.csv")
 
  


#####
# Revisit g: which verbs?
# also g: articles in front of some single nouns

# is row 51 different from row 46? those verbs will be in 46 (l & g)




'''
NOTES:
im retarted
im autist



'''
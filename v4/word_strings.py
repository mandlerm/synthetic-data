"""
Module callable from cfg.py. Returns word list for each part of speech
"""

def _read_file(f):
    str = [] 
    count = 0
    with open(f, 'r') as f:
        line = f.readline()
        str.append(f"'{line.strip()}'")
        line = f.readline()
        while line:   
            str.append(" | ")
            s = f"'{line.strip()}'"
            str.append(s)
            line = f.readline()
            # count += 1
 
    sent = ''.join(str)
    # print(f"File: {f} - count: {count}")
    f.close()
    return sent

# Pre_clean ->
def pre_clean():
    str = _read_file("../word_lists/pre_clean.txt")
    return f"Pre_clean -> {str}\n"

# Pre_hs_single ->
def pre_hs_single():
    str = _read_file("../word_lists/pre_hs_s.txt")
    return f"Pre_hs_s -> {str}\n"

# Pre_hs_plural ->
def pre_hs_plural():
    str = _read_file("../word_lists/pre_hs_p.txt")
    return f"Pre_hs_p -> {str}\n"

# Pre_hs_false_s ->
def pre_hs_false_single():
    str = _read_file("../word_lists/pre_hs_false_s.txt")
    return f"Pre_hs_false_s -> {str}\n"

# Pre_hs_false_p ->
def pre_hs_false_plural():
    str = _read_file("../word_lists/pre_hs_false_p.txt")
    return f"Pre_hs_false_p -> {str}\n"

# Det ->
def determiners():
    str = _read_file("../word_lists/determiners.txt")
    return f"Det -> {str}\n"


###################   
# NOUN THINGS (clean & hate speech false)
###################

# Noun things - single
# NthingsS -> 
def noun_things_single():
    str = _read_file("../word_lists/noun_things_single.txt")
    return f"NthingsS -> {str}\n"

# Noun things - plural
# NthingsP ->
def noun_things_plural():
    str = _read_file("../word_lists/noun_things_plural.txt")
    return f"NthingsP -> {str}\n"

# Noun human single  
#  N_human_single ->  
def noun_human_single():
    str = _read_file("../word_lists/people_singular.txt")
    return f"N_human_single -> {str}\n"

# Noun human plural
# N_human_plural -> 
def noun_human_plural():
    str = _read_file("../word_lists/people_plural.txt")
    return f"N_human_plural -> {str}\n"

# Noun food singlar
# N_food_single -> 
def noun_food_singular():
    str = _read_file("../word_lists/food_single.txt")
    return f"N_food_single -> {str}\n"


# Noun food plural
# N_food_plural -> 
def noun_food_plural():
    str = _read_file("../word_lists/food_plural.txt")
    return f"N_food_plural -> {str}\n"


# Noun animal singular
# N_animals_single -> 
def noun_animals_singular():
    str = _read_file("../word_lists/animals_single.txt")
    return f"N_animals_single -> {str}\n"


# Noun animal plural
# N_animals_plural -> 
def noun_animals_plural():
    str = _read_file("../word_lists/animals_plural.txt")
    return f"N_animals_plural -> {str}\n"

# Noun animal singular non-hate speech useage
# N_animals_single_non_hs -> 
def noun_animals_singular_non_hs():
    str = _read_file("../word_lists/animals_single_nonhs.txt")
    return f"N_animals_single_non_hs -> {str}\n"


# Noun animal plural non-hate speech useage
# N_animals_plural_non_hs -> 
def noun_animals_plural_non_hs():
    str = _read_file("../word_lists/animals_plural_nonhs.txt")
    return f"N_animals_plural_non_hs -> {str}\n"

# Noun always hate speech - single
# N_hate_speech_single -> 
def noun_hate_speech_single():
    str = _read_file("../word_lists/hate_speech_noun_single.txt")
    return f"N_hate_speech_single -> {str}\n"

# Noun always hate speech - single
# N_hate_speech_plural -> 
def noun_hate_speech_plural():
    str = _read_file("../word_lists/hate_speech_noun_plural.txt")
    return f"N_hate_speech_plural -> {str}\n"


###################     
# PROTECTED GROUPS
# Used as the nouns in hate speech
###################

# Protected people - single
# PPs -> 
def protected_groups_single():
    str = _read_file("../word_lists/pg_people_single.txt")
    return f"PPs -> {str}\n"

# Protected people - plural
# PPp -> 
def protected_groups_plural():
    str = _read_file("../word_lists/pg_people_plural.txt")
    return f"PPp -> {str}\n"

# Slurs Protected people - single
# PPs -> 
def protected_groups_slurs_single():
    str = _read_file("../word_lists/pg_slurs_single.txt")
    return f"PPss -> {str}\n"

# Slurs Protected people - plural
# PPp -> 
def protected_groups_slurs_plural():
    str = _read_file("../word_lists/pg_slurs_plural.txt")
    return f"PPsp -> {str}\n"



###################    
# Adjectives
###################    

# Adj
# Adj_clean -> 
def adjectives_clean():
    str = _read_file("../word_lists/adj.txt")
    return f"Adj_clean -> {str}\n"


# Adj hate speech + hate speech false
# Adj_hs ->
def adjectives_hs():
    str = _read_file("../word_lists/adj_hs.txt")
    return f"Adj_hs -> {str}\n"

# Negative adjectives, not hate speech
# Adj_neg ->
def adjectives_neg():
    str = _read_file("../word_lists/adj_neg.txt")
    return f"Adj_neg -> {str}\n"

# Adjectives specific for protected groups
# PgAdj ->
def protected_group_adj():
    str = _read_file("../word_lists/protected_group_adjectives.txt")
    return f"PgAdj -> {str}\n"


###################   
# Adverbs
###################  

# Adv
# Adv_clean -> 
def adverbs_clean():
    str = _read_file("../word_lists/adv.txt")
    return f"Adv_clean -> {str}\n"

# Adverb hate speech + hate speech false
# Adv_hs ->
def adverbs_hs():
    str = _read_file("../word_lists/adv_hs.txt")
    return f"Adv_hs -> {str}\n"


###################    
# VERBS  - clean
# ################### 
   
# Verb transitive
# Vt_clean_past ->
def vt_clean_past():
    str = _read_file("../word_lists/vt_clean_past.txt")
    return f"Vt_clean_past -> {str}\n"

# Verb transitive
# Vt_clean_present ->
def vt_clean_present():
    str = _read_file("../word_lists/vt_clean_present.txt")
    return f"Vt_clean_present -> {str}\n"

# Verb intransitive
# Vi ->
def vi_clean():
    str = _read_file("../word_lists/vi.txt")
    return f"Vi -> {str}\n"

# Verb ditransitive
# Vd ->
def vd_clean():
    str = _read_file("../word_lists/vd.txt")
    return f"Vd -> {str}\n"



###################    
# VERBS  - Hate Speech  and Hate Speech False  
###################

# Verb transitive: past 
# Vt_hs_past ->
def vt_hs_past():
    str = _read_file("../word_lists/vt_hs_past.txt")
    return f"Vt_hs_past -> {str}\n"

# Verb transitive: present: 
# Vt_hs_present ->
def vt_hs_present():
    str = _read_file("../word_lists/vt_hs_present.txt")
    return f"Vt_hs_present -> {str}\n"

# Verb intransitive: 
# Vi ->
def vi_hs():
    str = _read_file("../word_lists/vihs.txt")
    return f"Vi -> {str}\n"

# Verb ditransitive: 
# Vd ->
def vd_hs():
    str = _read_file("../word_lists/vdhs.txt")
    return f"Vd -> {str}\n"

# Verb version 2
# Vhs2 ->
def v_hs_2():
    str = _read_file("../word_lists/verb_hs_v2.txt")
    return f"Vhs2 -> {str}\n"


###################################
# Zero Tolerance Lists
# hate speech even as a standalone 

###################################

# Zero Tolerance phrase
# ZTp ->
def zt_phrase():
    str = _read_file("../word_lists/zt_phrase.txt")
    return f"ZTp -> {str}\n"

# Zero Tolerance Noun Single
# ZT_n_s 
def zt_noun_single():
    str = _read_file("../word_lists/zt_noun_single.txt")
    return f"ZT_n_s -> {str}\n"

# Zero Tolerance Noun Plural
# ZT_n_p
def zt_noun_plural():
    str = _read_file("../word_lists/zt_noun_plural.txt")
    return f"ZT_n_p -> {str}\n"

# Zero Adj
# ZT_adj
def zt_adj():
    str = _read_file("../word_lists/zt_adj.txt")
    return f"ZT_adj -> {str}\n"


###################################
# Profanity Lists
# Prof_s ->
###################################

# Profanity single
# Prof_s -> 
def prof_single():
    str = _read_file("../word_lists/profanity_single.txt")
    return f"Prof_s -> {str}\n"

# Profanity plural
# Prof_p -> 
def prof_plural():
    str = _read_file("../word_lists/profanity_plural.txt")
    return f"Prof_p -> {str}\n"



###################################
# Other
###################################

# Keyboard smashes
# Keys-> 
def keyboard_smashes():
    str = _read_file("../word_lists/keyboard_smashes.txt")
    return f"Keys -> {str}\n"
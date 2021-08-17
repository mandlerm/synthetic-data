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
 
    sent = ''.join(str)
    # print(''.join(str)) 
    f.close()
    return sent

def pre_clean():
    str = _read_file("pre_clean.txt")
    return f"Pre -> {str}\n"

def pre_hs():
    str = _read_file("pre_hs.txt")
    return f"Pre -> {str}\n"

def pre_hs_false():
    str = _read_file("pre_hs_false.txt")
    return f"Pre -> {str}\n"

def determiners():
    str = _read_file("determiners.txt")
    return f"Det -> {str}\n"


###################   NOUN THINGS (clean & hate speech false)
# Noun things - single
def noun_things_single():
    str = _read_file("n_things.txt")
    return f"Ns -> {str}\n"

# Noun things - plural
def noun_things_plural():
    str = _read_file("n_things_plural.txt")
    return f"Np -> {str}\n"

# Noun human single    
def noun_humans_single():
    str = _read_file("people_singular.txt")
    return f"Nhs -> {str}\n"

# Noun human plural
def noun_humans_plural():
    str = _read_file("people_plural.txt")
    return f"Nhp -> {str}\n"


###################     PROTECTED GROUPS
######  Used as the nouns in hate speech

# Protected people - single
def protected_groups_single():
    str = _read_file("n_pg_people_single.txt")
    return f"PPs -> {str}\n"

# Protected people - plural
def protected_groups_plural():
    str = _read_file("n_pg_people_plural.txt")
    return f"PPp -> {str}\n"



###################    Adjectives
# Adj
def adjectives_clean():
    str = _read_file("adj.txt")
    return f"Adj -> {str}\n"


# Adj hate speech + hate speech false
def adjectives_hs():
    str = _read_file("adj_hs.txt")
    return f"Adjhs -> {str}\n"


###################   Adverbs
# Adv
def adverbs_clean():
    str = _read_file("adv.txt")
    return f"Adv -> {str}\n"

# Adverb hate speech + hate speech false
def adverbs_hs():
    str = _read_file("adv_hs.txt")
    return f"Advhs -> {str}\n"


###################    VERBS  - clean   
# Verb transitive
def vt_clean():
    str = _read_file("vt.txt")
    return f"Vt -> {str}\n"

# Verb intransitive
def vi_clean():
    str = _read_file("vi.txt")
    return f"Vi -> {str}\n"

# Verb ditransitive
def vd_clean():
    str = _read_file("vd.txt")
    return f"Vd -> {str}\n"



###################    VERBS  - Hate Speech  and Hate Speech False  
# Verb transitive
def vt_hs():
    str = _read_file("vths.txt")
    return f"Vt -> {str}\n"

# Verb intransitive
def vi_hs():
    str = _read_file("vihs.txt")
    return f"Vi -> {str}\n"

# Verb ditransitive
def vd_hs():
    str = _read_file("vdhs.txt")
    return f"Vd -> {str}\n"



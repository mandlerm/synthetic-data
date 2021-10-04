
# TRUE FOR HS:  Version2.1
# Adjhs PgN | Det Adjhs PgN | Advhs Adjhs PgN | Det Advhs PgN | Det Advhs Adjhs PgN  
def surgical_clean_grammar():
    
    # pronoun + protected group
    v4a = '''
    S -> Pro PgN 

    Pro -> 'she' | 'him' | 'they' | 'you' | 'ur' | you 'are' | 'your' | 'i' | 'im' | 'iam' | 'i am'

    PgN ->  PPs | PPp 
    
    '''

    # protected group adjective + noun thing
    v4b = '''
    S -> PgAdj Nthing
    
    Nthing -> NthingsS | NthingsP
    '''

    # profanity + nouns animals
    v4c = '''
    S -> Prof Animals

    Prof -> Prof_p | Prof_s
    Animals -> N_animals_single_non_hs | N_animals_plural_non_hs
    
    '''

    # noun animals + profanity
    v4d = '''
    S -> Animals Prof 

    Prof -> Prof_p | Prof_s
    Animals -> N_animals_single_non_hs | N_animals_plural_non_hs
    '''

    # adj.hs + nouns animals
    v4e = '''
    S -> Adj_hs Animals  

    Animals -> N_animals_single_non_hs | N_animals_plural_non_hs
    '''

    # negative adjectives + people nouns
    v4f = '''
    S -> Adj_neg People 

    People -> N_human_single | N_human_plural
    '''

    # pronouns + profanity
    v4g = '''
    S -> Pro Prof 

    Pro -> 'you guys' | 'you are' | 'you' | 'ur' | 'u r' | 'i' | 'i am' | 'im' | 'we r' | 'we are' | 'were'
    
    Prof -> Prof_p | Prof_s
    '''

    # negative adjective + protected group
    v4h = '''
    S -> Adj_neg PgN  

    PgN ->  PPs | PPp 
    '''

    # protected group + profanity
    v4i = '''
    S -> PgN Prof

    PgN ->  PPs | PPp 

    Prof -> Prof_p | Prof_s
    '''

    # negative adjective + noun.people
    v4j = '''
    S -> Adj_neg People

    People -> N_human_single | N_human_plural
    '''
    
    # noun things + acronyms
    v4k = '''
    S -> Nthing Acr | Acr
    
    Acr -> 'wtf' | 'lmao' | 'lmfao' | 'af' | 'idgaf' | 'smd' | 'dfg' | 'jfc' | 'fk' | 'ffs' | 'tf' | 'thot' | 'rofl' | 'lol'

    Nthing -> NthingsS | NthingsP
    '''

    # keyboard smashes
    v4l = '''
    S -> Keys
    '''
    
    return v4e


def clean_grammar():
    g = '''
    S -> Det N_human_single Vt_clean_past Det N_animals_single
    
    PgN ->  PPs | PPp 
    Noun_clean -> Animals | Food | Humans
    Animals -> N_animals_single | N_animals_plural
    Food -> N_food_single | N_food_plural
    Humans -> N_human_single | N_human_plural

    '''
    return g


# Protected groups with benign adverbs, adjectives and nouns
def hs_grammar_false_pg():
    g = '''
    S -> PPp Vt_clean_past Det Noun_single

    PgN ->  PPs | PPp 
    Noun_clean -> Animals | Food | Humans
    Animals -> N_animals_single | N_animals_plural
    Food -> N_food_single | N_food_plural
    Humans -> N_human_single | N_human_plural
    Noun_single -> PPs | N_animals_single | N_food_single | N_human_single
    Noun_plural -> PPp | N_animals_plural | N_food_plural | N_human_plural

    NPh_single -> Adj_clean PPs | Adv_clean Adj_clean PPs 
    NPh_plural -> Adj_clean PPp | Adv_clean Adj_clean PPp 
    VPa_past_benign ->  Vt_clean_past Det Noun_single | Vt_clean_past Noun_plural  
    
    '''
    return g

# Regular nouns with hate-speech/violent/aggressive adverbs, adjectives and nouns
def hs_grammar_false_non_pg():
    g = '''
    S -> Det Adj_hs N_food_single | Det Adj_hs N_animals_single | Det Adj_hs N_human_single | Vt_hs_past Det N_animals_single | Vt_hs_past N_animals_plural | Vt_hs_past Det N_human_single | Vt_hs_past N_human_plural | Vt_hs_past Det  'fucking' N_animals_single | Vt_hs_past  'the fucking'  N_animals_plural | Vt_hs_past Det 'fucking'  N_human_single | Vt_hs_past 'the fucking'  N_human_plural

    PgN ->  PPs | PPp 
    Noun_clean -> Animals | Food | Humans
    Animals -> N_animals_single | N_animals_plural
    Food -> N_food_single | N_food_plural
    Humans -> N_human_single | N_human_plural
    Noun_single -> PPs | N_animals_single | N_food_single | N_human_single
    Noun_plural -> PPp | N_animals_plural | N_food_plural | N_human_plural

    NPh_single -> Adj_hs Noun_single | Adv_hs Adj_hs Noun_single 
    NPh_plural -> Adj_hs Noun_plural | Adv_hs Adj_hs Noun_plural 
    VPa_past_benign ->  Vt_hs_past Det Noun_single | Vt_hs_past Noun_plural  
    '''
    return g



# TRUE FOR HS
# Adjhs PgN | Det Adjhs PgN | Advhs Adjhs PgN | Det Advhs PgN | Det Advhs Adjhs PgN  
def hs_grammar():
    g = '''
    S -> Vt_hs_present PPp | Vt_hs_present Det PPs  | Vt_hs_present Det N_hate_speech_single  | Vt_hs_present N_hate_speech_plural  | Adj_hs PPp

    PgN ->  PPs | PPp 
    Noun_clean -> Animals | Food | Humans
    Animals -> N_animals_single | N_animals_plural
    Food -> N_food_single | N_food_plural
    Humans -> N_human_single | N_human_plural

    VPa_past_benign ->  Vt_clean_past PgN | Vt_clean_past Noun_clean | Vt_clean_past Det Adj_hs Noun_clean

    Nh_clean -> Det Humans Vt_clean_past 

    HS_clause_simple ->  Adj_hs PgN | Adj_hs ZT_n_p | Adj_hs ZT_n_s | ZT_n_p | ZT_n_s

    HS_clause_complex -> Vt_hs_past Det PgN | Vt_hs_past Det Adj_hs PPs | Adv_hs Adj_hs PgN
    
    '''

    return g


# TRUE FOR HS:  Version2.1
# Adjhs PgN | Det Adjhs PgN | Advhs Adjhs PgN | Det Advhs PgN | Det Advhs Adjhs PgN  
def surgical_hs_grammar():
    v2a = '''
    S -> Pro 'fucking' PgN

    Pro -> 'ur' | 'ure' | 'youre' |  'you are' | 'u r '| 'u are' | 'you r' | 'she' | 'they' | 'he' | 'them' 
    PgN ->  PPs | PPp 
    '''

    v2b = '''
    S -> Pro 'retarted' | Pro 'retard' | Pro 'retards' | Pro 'fucking retarted' | Pro 'fucking retard' | Pro 'fucking retards'

    Pro -> 'ur' | 'ure' | 'youre' |  'you are' | 'u r '| 'u are' | 'you r' | 'she' | 'they' | 'he' | 'them' 
    '''

    v2c = '''
    S -> Noun_single 'is retarded' | Noun_plural 'are retarted' | Noun_plural 'r retarted' | Noun_single 'is fucking retarded' | Noun_plural 'are fucking retarted' | Noun_plural 'r fucking retarted'

    Noun_single -> PPs | N_animals_single | N_food_single | N_human_single
    Noun_plural -> PPp | N_animals_plural | N_food_plural | N_human_plural

    Pro -> 'ur' | 'ure' | 'youre' |  'you are' | 'u r'| 'u are' | 'you r' | 'she' | 'they' | 'he' | 'them' 
    '''

    v2d = '''
    S -> 'retarted' Noun_clean
    
    Noun_clean -> Animals | Food | Humans
    Animals -> N_animals_single | N_animals_plural
    Food -> N_food_single | N_food_plural
    Humans -> N_human_single | N_human_plural

    Noun_single -> PPs | N_animals_single | N_food_single | N_human_single
    Noun_plural -> PPp | N_animals_plural | N_food_plural | N_human_plural

    Pro -> 'ur' | 'ure' | 'youre' |  'you are' | 'u r'| 'u are' | 'you r' | 'she' | 'they' | 'he' | 'them' 
    '''

    v2e = '''
    S -> Ad_jhs PPp | Adj_hs Det PPs 
    '''

    v2f = '''
    S -> Adv_hs Adj_hs PPp | Adv_hs Adj_hs Det PPs 
    '''

    v2g = '''
    S -> PPs HSAnS | PPs HSAnsP

    HSAnS -> 'pig' | 'ape' | 'monkey' | 'rat'
    HSAnP -> 'pigs' | 'apes' | 'monkeys' | 'rats'
    '''

    v2h = '''
    S -> Pro Ugly PPp

    Pro -> 'I' | 'we' 

    Ugly -> | 'hate' | 'sterilize' | 'slaughter' | 'shoot' | 'kill' | 'gas' | 'hang' | 'arrest' | 'ban' | 'beat' | 'slay' | 'oppress' | 'ensalve' | 'loath' | 'despise' | 'abhor' | 'detest'
    '''

    return v2c





'''
fuck
fck
fucking
fcking
 
'''
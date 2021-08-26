
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






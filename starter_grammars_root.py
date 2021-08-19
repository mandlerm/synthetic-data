def clean_grammar():
    g = '''
    S -> Pre_clean Det N_human_single | Pre_clean Det N_animal_single  | Pre_clean Det N_food_single | Det N_human_single Vt_clean_past Det N_animal_single | N_human_plural Vt_clean_past Animals | Det N_human_single Vt_clean_past Det N_food_single |  N_human_plural Vt_clean_past N_food_plural | Det N_animal_single Vt_clean_past Det N_human_single 
    
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
    S -> Pre_hs_false Det PPs | Det NPh_single VPa_past_benign |  NPh_plural VPa_past_benign | Vt_clean_present PPp | Adj_clean PPp

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
    S -> Pre_hs_false Det Noun_single | Det NPh_single VPa_past_benign |  NPh_plural VPa_past_benign 

    Noun_clean -> Animals | Food | Humans
    Animals -> N_animals_single | N_animals_plural
    Food -> N_food_single | N_food_plural
    Humans -> N_human_single | N_human_plural
    Noun_single -> N_animals_single | N_food_single | N_human_single
    Noun_plural -> N_animals_plural | N_food_plural | N_human_plural

    NPh_single -> Adj_hs Noun_single | Adv_hs Adj_hs Noun_single 
    NPh_plural -> Adj_hs Noun_plural | Adv_hs Adj_hs Noun_plural 
    VPa_past_benign ->  Vt_hs_past Det Noun_single | Vt_hs_past Noun_plural  
    '''
    return g


# TRUE FOR HS
# Adjhs PgN | Det Adjhs PgN | Advhs Adjhs PgN | Det Advhs PgN | Det Advhs Adjhs PgN  
def hs_grammar():
    g = '''
    S -> Pre_hs Det HS_clause_simple | Det NPh VPa_past_benign | Nh_clean HS_complex_clause | Vt_hs_present PPp | Adj_hs PPp

    PgN ->  PPs | PPp 
    Noun_clean -> Animals | Food | Humans
    Animals -> N_animals_single | N_animals_plural
    Food -> N_food_single | N_food_plural
    Humans -> N_human_single | N_human_plural

    NPh -> Adj_hs PgN | Adv_hs Adj_hs PgN | Adj_hs N_hate_speech_single
    VPa_past_benign ->  Vt_clean_past PgN | Vt_clean_past Noun_clean | Vt_clean_past Det Adj_hs Noun_clean

    Nh_clean -> Det Humans Vt_clean_past  
    HS_clause_simple -> N_hate_speech_single | Adj_hs PgN

    HS_clause_complex -> Vt_hs_past Det PgN | Vt_hs_past Det Adj_hs PPs | Adv_hs Adj_hs PgN
    '''

    return g







# Adjhs PgN | Det Adjhs PgN | Advhs Adjhs PgN | Det Advhs PgN | Det Advhs Adjhs PgN 
def hs_pre_nph():
    g = '''
    S -> Pre NPh

    NPh -> Adjhs PgN | Det Adjhs PgN | Advhs Adjhs PgN | Det Advhs PgN | Det Advhs Adjhs PgN
    
    PgN ->  PPs | PPp 

    VPa -> Vt PPs | Vt Ns | Vt PPs Adjhs | Vt Ns Adjhs 
    VPb -> Vi | Vi Advhs
    VPc -> Vd Nhs Ns | Vd Nhs Ns Advhs
    '''
    return g

# Adjhs PgN | Det Adjhs PgN | Advhs Adjhs PgN | Det Advhs PgN | Det Advhs Adjhs PgN  
def hs_pnh_vpa():
    g = '''
    S -> NPh VPa

    NPh -> Det Advhs Adjhs PgN
    
    PgN ->  PPs | PPp 

    VPa -> Vt PPs | Vt Ns | Vt PPs Adjhs | Vt Ns Adjhs 
    '''
    return g

# Adjhs PgN | Det Adjhs PgN | Advhs Adjhs PgN | Det Advhs PgN | Det Advhs Adjhs PgN  
def hs_nph_vpb():
    g = '''
    S -> NPh VPb

    NPh -> Advhs Adjhs PgN
    
    PgN ->  PPs | PPp 

    VPb -> Vi | Vi Advhs
    '''
    return g

# Adjhs PgN | Det Adjhs PgN | Advhs Adjhs PgN | Det Advhs PgN | Det Advhs Adjhs PgN  
def hs_nph_vpc():
    g = '''
    S -> NPh VPc

    NPh -> Det Advhs Adjhs PgN  
    
    PgN ->  PPs | PPp 

    VPc -> Vd Nhs Ns | Vd Nhs Ns Advhs
    '''
    return g
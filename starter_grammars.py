



def clean_grammar():
    g = '''
    S -> Pre NPh | Pre NPn | NPh VPa | NPn VPb | NPh VPb | NPh VPc

    NPh -> Det Nh | Nh | Adj Nh | Det Adj Nh | Adv Adj Nh | Det Adj Nh | Det Adv Adj Nh
    NPn -> Det Nn | Nn | Adj Nn | Det Adj Nn | Adv Adj Nn | Det Adj Nn | Det Adv Adj Nn

    N -> Nh | Nn
    Nh -> Nhs | Nhp
    Nn -> Ns | Np

    VPa -> Vt NPh | Vt NPn | Vt NPh Adj | Vt NPn Adj 
    VPb -> Vi | Vi Adv
    VPc -> Vd NPh NPn | Vd NPh NPn Adv
    '''
    return g


# NEGATIVE COMMENTS AGAINST PROTECTED GROUPS BUT NOT HATE SPEECH. Hate speechy adv and Adj against non-protected nouns
def hs_grammar_false():
    g = '''
    S -> Pre NPh | Pre NPn | NPh VPa | NPn VPb | NPh VPb | NPh VPc
    
    NPh -> Det Nh | Nh | Adjhs Nh | Det Adjhs Nh | Advhs Adjhs Nh | Det Adjhs Nh | Det Advhs Adjhs Nh  
    NPn -> Det Nn | Nn | Adjhs Nn | Det Adjhs Nn | Advhs Adjhs Nn | Det Adjhs Nn | Det Advhs Adjhs Nn
    
    Nh -> Nhs | Nhp
    Nn -> Ns | Np
    
    VPa -> Vt Nsh | Vt Nsn | Vt Nsh Adjhs | Vt Nsn Adjhs 
    VPb -> Vi | Vi Advhs
    VPc -> Vd Nsh Nsn | Vd Nsh Nsn Advhs
    '''
    return g

# TRUE FOR HS
# Adjhs PgN | Det Adjhs PgN | Advhs Adjhs PgN | Det Advhs PgN | Det Advhs Adjhs PgN  
def hs_grammar():
    g = '''
    S -> Pre_hs NPh | NPh VPa_past_benign | Nh_clean HS_clause | Vt_hs_present PPp | Adj_hs PPp
    PgN ->  PPs | PPp 
    Noun_clean -> Animals | Food | Humans
    Animals -> N_animals_single | N_animals_plural
    Food -> N_food_single | N_food_plural
    Humans -> N_human_single | N_human_plural

    NPh -> Adj_hs PgN | Det Adj_hs PgN | Adv_hs Adj_hs PgN | Det Adv_hs Adj_hs PgN 
    VPa_past_benign -> Vt_clean_past Noun_clean Adv_clean | Vt_clean_past PgN | Vt_clean_past Noun_clean | Vt_clean_past Det Adj_hs Noun_clean

    Nh_clean -> Det Humans Vt_clean_past  
    HS_clause -> Det Adj_hs PgN | Det N_hate_speech_single | Det N_hate_speech_plural | Vt_hs_past PgN | Vt_hs_past Det Adj_hs PgN 
    
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













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
    S -> Pre NPh | NPh VPa | NPh VPb | NPh VPc

    NPh -> Adjhs PgN | Det Adjhs PgN | Advhs Adjhs PgN | Det Advhs PgN | Det Advhs Adjhs PgN  
    
    PgN ->  PPs | PPp 

    VPa -> Vt PPs | Vt Ns | Vt PPs Adjhs | Vt Ns Adjhs 
    VPb -> Vi | Vi Advhs
    VPc -> Vd Nhs Ns | Vd Nhs Ns Advhs
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

    NPh -> Det Adjhs PgN
    
    PgN ->  PPs | PPp 

    VPa -> Vt PPs | Vt Ns | Vt PPs Adjhs | Vt Ns Adjhs 
    '''
    return g

# Adjhs PgN | Det Adjhs PgN | Advhs Adjhs PgN | Det Advhs PgN | Det Advhs Adjhs PgN  
def hs_nph_vpb():
    g = '''
    S -> NPh VPb

    NPh -> Adjhs PgN | Det Adjhs PgN | Advhs Adjhs PgN | Det Advhs PgN | Det Advhs Adjhs PgN  
    
    PgN ->  PPs | PPp 

    VPb -> Vi | Vi Advhs
    '''
    return g

def hs_nph_vpc():
    g = '''
    S -> NPh VPc

    NPh -> Adjhs PgN | Det Adjhs PgN | Advhs Adjhs PgN | Det Advhs PgN | Det Advhs Adjhs PgN  
    
    PgN ->  PPs | PPp 

    VPc -> Vd Nhs Ns | Vd Nhs Ns Advhs
    '''
    return g









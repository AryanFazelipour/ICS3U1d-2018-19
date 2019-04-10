#  Cigar_Party

def cigar_party(cigars, is_weekend):

    if cigars >= 40 and is_weekend:
        return(True)

    elif cigars >= 40 and cigars <= 60 and is_weekend == False:
        return(True)

    else:
        return(False)


print(cigar_party(30, True))
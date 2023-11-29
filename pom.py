import random
def odaberi_pojam():
    pojmovi = ["hipotermija", "evangelizam","fiksirati","temperatura", "covecanstvo",
               "rodoslavlje","olimpijske igre", "strucna literatura"]
    pojam = random.choice(pojmovi)
    return pojam

def crtice(rec):
    crtice_niz = []
    for i in rec:
        if i!= " ":
            crtice_niz.append("_")
        else:
            crtice_niz.append(" ")
    return crtice_niz

def moje_slovo(rec, crte, sl):
    for i in range(0,len(rec)):
        if rec[i] == sl:
            crte[i] = sl
    return crte

def slovo_u_reci(rec, slovo):
    if slovo in rec:
        return True
    else:
        return False

def convertisseur(a):
    #décimal vers binaire
    d=[]
    while a!=0:
        c=a%2
        a=a//2
        d.append(c)
    d.reverse()
    return tab_vers_str(d)

def convert(a):
    #binaire vers décimal
    a=str(a)
    b=1
    c=0
    for i in range (len(a)):
        c+=int(a[-1-i])*b
        b=b*2
    return c

def tab_vers_str(tab):
    e=""
    for i in range(len(tab)):
        e+=str(tab[i])
    return e
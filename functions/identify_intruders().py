def indentify_intruders():
    n=int(input('Entyer no of ppl who tried to log in:'))
    m=int(input('Enter no of authirzed ppl'))
    attempts=[]
    authorized=[]
    s=set()
    for i in range(n):
        att=input('Enter who tried to log in')
        attempts.append(att)
    for i in range(m):
        aut=input('Enmter who have access')
        authorized.append(aut)
    for j in attempts:
        if j not in authorized:
            s.add(j)
    print(s)
    return(s)
print()
indentify_intruders()
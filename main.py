from random_word import RandomWords
import time

joc=True
print("Introduceti numele: ")
print("Bun venit",input())


def generare():
    print("Ti se genereaza cuvantul...")
    time.sleep(2)
    cuvant=RandomWords().get_random_word()
    # print(cuvant)
    return cuvant

cuvant=generare()
vieti=5
litere_folosite=[] 
cuvinte_gasite=[]

def afisare():
    for c in cuvant:
        if c in litere_folosite or c==cuvant[0] or c==cuvant[len(cuvant)-1]:
            print(c,end="")
        else:
            print("_",end="")
    print("\nvieti:",str(vieti))
    print("ai folosit urmatoarele litere ", litere_folosite)


afisare()

while joc==True:
    while vieti>0:
        ghici=input("\nIntrodu o litera sau cuvantul: ")
        if ghici==cuvant:
            print("\n Felicitari, ai ghicit cuvantul!")
            break
        elif len(ghici)>1:
            vieti-=1
            afisare()
        elif ghici in cuvant and ghici in [cuvant[0],cuvant[len(cuvant)-1]]:
            print("Litera ti a fost data la inceput!")
        elif ghici in cuvant:
            litere_folosite.append(ghici)
            afisare()
        else:
            vieti-=1
            litere_folosite.append(ghici)
            afisare()

    if vieti==0:
        print("ai pierdut")
    else:
        cuvinte_gasite.append(cuvant)


    print("\ncuvinte ghicite pana acum: ",cuvinte_gasite)
    raspuns=input("vrei sa continui?(da/nu): ")
    if raspuns=="da":
        joc=True
        vieti=5
        cuvant=generare()
        litere_folosite=[] 
        afisare()
    else: 
        joc=False




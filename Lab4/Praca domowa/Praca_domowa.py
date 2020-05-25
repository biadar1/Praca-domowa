#zadanie 1
def zadanie1():
    plik=open("podzielne_przez_4.txt","w+")
    for i in range(1,101):
        if i%4==0:
            liczby=[i]
            plik.writelines(str(i)+"\n")
    plik.close()
#zadanie 2
def zadanie2():
    plik=open("podzielne_przez_4.txt","r")
    print(plik.readlines())
    plik.close()
#zadanie 3
def zadanie3():
    with open("dane.txt", "w+") as plik:
        plik.writelines("Piszę kila linijek\n tekstu\n 1\n 2\n")
    with open("dane.txt", "r") as plik:
        for i in plik:
            print(i, end="")
print("Zadanie 1")
zadanie1()
print("Zadanie 2")
zadanie2()
print("Zadanie 3")
zadanie3()
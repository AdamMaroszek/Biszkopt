jaja = 6                        #szt
cukier = 200                    #g
maka =150                       #g
makaziemniaczana = 50          #g
sol = 1                         #szczypta
proszek = 1/4 #                 łyżeczki

print("Jeśli chcesz upiec biszkopt, ale ilość Twoich składników nie zgadza się z tymi z przepisu,\n"
      "lub chcesz zrobić ten biszkopt na więcej osób, podaj mi ilość składnika, \n"
      "do którego obliczymy potrzebną ilość pozostałych składników.\n")
while True:
    print("Wybierz według którego składnika podać proporcje:\n")
    print("1. Jaja\n"
          "2. Cukier\n"
          "3. Mąka\n"
          "4. Mąka ziemniaczana\n"
          "5. Sól\n"
          "6. Proszek do pieczenia")
    print("Twój wybór to:\n"
          "(podaj numer i zatwierdż enterem)")
    x=input()
    if x == "1":
        print("Podaj ilość jaj:")
        jaja2 = int(input())
        propjaja=jaja2/jaja
        print("Cukier:", cukier * propjaja, "g")
        print("Mąka:", maka * propjaja, "g")
        print("Mąka ziemniaczana:", makaziemniaczana * propjaja, "g")
        print("Sól:", sol * propjaja, "szczypty")
        print("Proszek do pieczenia:", proszek * propjaja, "łyżeczki")
    if x == "2":
        print("Podaj ilość cukru w gramach:")
        cukier2 = int(input())
        propcukier=cukier2/cukier
        print("Jaja:", jaja * propcukier, "szt")
        print("Mąka:", maka * propcukier, "g")
        print("Mąka ziemniaczana:", makaziemniaczana * propcukier, "g")
        print("Sól:", sol * propcukier, "szczypty")
        print("Proszek do pieczenia:", proszek * propcukier, "łyżeczki")
    if x == "3":
        print("Podaj ilość mąki w gramach:")
        maka2 = int(input())
        propmaka = maka2 / maka
        print("Jaja:", jaja * propmaka, "szt")
        print("Cukier:", cukier * propmaka, "g")
        print("Mąka ziemniaczana:", makaziemniaczana * propmaka, "g")
        print("Sól:", sol * propmaka, "szczypty")
        print("Proszek do pieczenia:", proszek * propmaka, "łyżeczki")
    if x == "4":
        print("Podaj ilość mąki ziemniaczanej w gramach:")
        makaziemniaczana2 = int(input())
        propmakaziemniaczana = makaziemniaczana2 / makaziemniaczana
        print("Jaja:", jaja * propmakaziemniaczana, "szt")
        print("Cukier:", cukier * propmakaziemniaczana, "g")
        print("Mąka:", maka * propmakaziemniaczana, "g")
        print("Sól:", sol * propmakaziemniaczana, "szczypty")
        print("Proszek do pieczenia:", proszek * propmakaziemniaczana, "łyżeczki")
    if x == "5":
        print("Podaj ilość soli w szczyptach :) :")
        sol2 = int(input())
        propsol = sol2 / sol
        print("Jaja:", jaja * propsol, "szt")
        print("Cukier:", cukier * propsol, "g")
        print("Mąka:", maka * propsol, "g")
        print("Mąka ziemniaczana:", makaziemniaczana * propsol, "g")
        print("Proszek do pieczenia:", proszek * propsol, "łyżeczki")
    if x == "6":
        print("Podaj ilość soli w łyzeczkach :")
        proszek2 = int(input())
        propproszek = proszek2 / proszek
        print("Jaja:", jaja * propproszek, "szt")
        print("Cukier:", cukier * propproszek, "g")
        print("Mąka:", maka * propproszek, "g")
        print("Mąka ziemniaczana:", makaziemniaczana * propproszek, "g")
        print("Sól:", sol * propproszek, "szczypty")
    print("Jeśli chcesz kontynuować naciśnij dowolny klawisz")
    input()

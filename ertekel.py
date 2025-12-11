def ertekeles():
    print("I/A,B:")
    etel=input("\tÉtel neve: ")
    rendelo_neve=input("\tÉtel rendelőjének neve: ")
    ertekeles=int(input("\tÉtékelés(1-5): "))
    print("I/C:")
    if ertekeles<=0:
        print("\tAz értékelés nem lehet negatív!")
    elif ertekeles>5:
        print("\t5 pont feletti értékelés nem elfogadható!")
    else:
        print("\tKöszönjük az értékelést!")

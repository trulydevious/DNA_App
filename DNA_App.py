import PySimpleGUI as sg

# Zamiana DNA na RNA
def transkrypcja(dna):
    """
    Funkcja wykonująca transkrypcję DNA na RNA.
    Args:
        dna (str): sekwencja DNA
    Returns:
        rna (str): sekwencja RNA
    """
    rna = ""
    for i in dna:
        if i == "T":        # Zmiana T na U
            rna += "U"
        else:
            rna += i
    return rna
    # print("3'-", dna, "-5'")
    # print("5'-", rna, "-3'")   # Sekwencja RNA

# Zamiana mRNA na białko
def translacja(rna):
    """
    Funkcja wykonująca translację mRNA na białko.
    Args:
        rna (str): sekwencja RNA
    Returns:
        białko (str): sekwencja białek
    """
    kodon = {"UUU" : "Phe", "CUU" : "Leu", "AUU" : "Ile", "GUU" : "Val",
           "UUC" : "Phe", "CUC" : "Leu", "AUC" : "Ile", "GUC" : "Val",
           "UUA" : "Leu", "CUA" : "Leu", "AUA" : "Ile", "GUA" : "Val",
           "UUG" : "Leu", "CUG" : "Leu", "AUG" : "Met", "GUG" : "Val",
           "UCU" : "Ser", "CCU" : "Pro", "ACU" : "Thr", "GCU" : "Ala",
           "UCC" : "Ser", "CCC" : "Pro", "ACC" : "Thr", "GCC" : "Ala",
           "UCA" : "Ser", "CCA" : "Pro", "ACA" : "Thr", "GCA" : "Ala",
           "UCG" : "Ser", "CCG" : "Pro", "ACG" : "Thr", "GCG" : "Ala",
           "UAU" : "Tyr", "CAU" : "His", "AAU" : "Asn", "GAU" : "Asp",
           "UAC" : "Tyr", "CAC" : "His", "AAC" : "Asn", "GAC" : "Asp",
           "UAA" : "STOP", "CAA" : "Gin", "AAA" : "Lys", "GAA" : "Glu",
           "UAG" : "STOP", "CAG" : "Gin", "AAG" : "Lys", "GAG" : "Glu",
           "UGU" : "Cys", "CGU" : "Arg", "AGU" : "Ser", "GGU" : "Gly",
           "UGC" : "Cys", "CGC" : "Arg", "AGC" : "Ser", "GGC" : "Gly",
           "UGA" : "STOP", "CGA" : "Arg", "AGA" : "Arg", "GGA" : "Gly",
           "UGG" : "Trp", "CGG" : "Arg", "AGG" : "Arg", "GGG" : "Gly"}

    bialka = ""
    for i in range(0, len(rna)-(3+len(rna)%3), 3):          # Generowanie białek
        if kodon[rna[0:3]] != "Met":                        # Sprawdzanie czy napoczątku jest kodon start
            print("Brak kodonu start")
            break
        elif kodon[rna[i:i+3]] == "STOP":                   # Jeśli pojawia się kodon stop, to koniec translacji
            break
        bialka += kodon[rna[i:i+3]]
    return bialka
    # print(bialka)                      # Sekwencja białek

# Drugie okno, które wyświetla wyniki
def okno_2(sek_dna, sek_rna):
    layout_2 = [[sg.Text("Przetworzone dane".upper())],
    [sg.Text("DNA po transkrypcji:", key="DNA",), sg.Text("RNA po translacji:", pad=(290,0))],
    [sg.Text(sek_dna), sg.Text(sek_rna, pad=(383,0))],
    [sg.Exit()]]
    okno_2 = sg.Window("Transkrypcja i translacja", layout_2)
    while True:
        zdarzenie, wartosc = okno_2.read()
        if zdarzenie == sg.WINDOW_CLOSED or zdarzenie == "Exit":
            break
    okno_2.close()

# Pierwsze okno, w którym podaje się dane
def okno_1():
    layout = [[sg.Text("Podaj sekwencję DNA do transkrypcji i RNA do translacji".upper())],
    [sg.Text("DNA", key="DNA"), sg.Text("RNA", pad=(290,0))],
    [sg.InputText(key="dna"), sg.InputText(key="rna")],
    [sg.Button("Dalej"), sg.Exit()]]

    okno = sg.Window("Wprowadzenie danych", layout)

    while True:
        zdarzenie, wartosc = okno.read()
        if zdarzenie == sg.WINDOW_CLOSED or zdarzenie == "Exit":
            break
        if zdarzenie == "Dalej":
            sek_dna = transkrypcja(wartosc["dna"])
            sek_rna = translacja(wartosc["rna"])
        okno.close()
        okno_2(sek_dna, sek_rna)

# Okno startowe ze schematem transkrypcji i translacji
sg.theme("LightBlue")
layout_1 = [[sg.Text("Schemat transkrypcji i translacji".upper())],
[sg.Image(filename="obrazek.png")],
[sg.Button("Dalej")]]
okno = sg.Window("Grafika", layout_1)
while True:
    zdarzenie, wartosc = okno.read()
    if zdarzenie == sg.WINDOW_CLOSED or zdarzenie == "Dalej":
        break
okno.close()
okno_1()

sg.Popup("Praca w programie została zakończona.")
okno.close()

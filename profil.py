from controller import Controller
from hodnoceni import Hodnoceni


class Profil:
    def __init__(self):
        self.pdf = None
        self.jmeno = None
        self.jmeno_dfa = None
        self.prijmeni = None
        self.prijmeni_dfa = None
        self.id_facr = None
        self.id_facr_dfa = None
        self.znamka = None
        self.obtiznost = None
        self.hodnoceni = None

    def dekodujHodnoceni(self, pdf):
        self.pdf = pdf
        jmeno_slovo = pdf.pq('LTTextLineHorizontal:contains("Jméno")')[0]
        self.jmeno = self.ziskej_hlavicku(jmeno_slovo, False)
        self.jmeno_dfa = self.ziskej_hlavicku(jmeno_slovo, True)

        prijmeni_slovo = pdf.pq('LTTextLineHorizontal:contains("{}")'.format("Příjmení"))[0]
        self.prijmeni = self.ziskej_hlavicku(prijmeni_slovo, False)
        self.prijmeni_dfa = self.ziskej_hlavicku(prijmeni_slovo, True)

        id_facr_slovo = pdf.pq('LTTextLineHorizontal:contains("{}")'.format("ID"))[0]
        self.id_facr = self.ziskej_hlavicku(id_facr_slovo, False)
        self.id_facr_dfa = self.ziskej_hlavicku(id_facr_slovo, True)

        znamka_slovo = pdf.pq('LTTextLineHorizontal:contains("{}")'.format("Známka"))[0]
        self.znamka = self.ziskej_hlavicku(znamka_slovo, False)

        obtiznost_slovo = pdf.pq('LTTextLineHorizontal:contains("{}")'.format("Úroveň obtížnosti"))[0]
        self.obtiznost = self.ziskej_hlavicku(obtiznost_slovo, False)

        Controller(pdf)
        self.hodnoceni = Hodnoceni(pdf)
        self.hodnoceni.dekodujHodnoceni()

    def ziskej_hlavicku(self, slovo, jeDFA):
        x0 = float(slovo.get('x0', 0)) - 13
        y0 = float(slovo.get('y0', 0)) - 25
        if jeDFA:
            y0 = float(slovo.get('y0', 0)) - 95
        x1 = float(slovo.get('x1', 0)) + 13
        y1 = float(slovo.get('y1', 0)) - 25
        if jeDFA:
            y1 = float(slovo.get('y1', 0)) - 95
        return self.pdf.pq(
            'LTPage[page_index="0"] LTTextLineHorizontal:overlaps_bbox("%s, %s, %s, %s")' % (x0, y0, x1, y1)).text()

    def printPosudek(self):
        self.printProfil()
        self.hodnoceni.printHodnoceni()

    def printProfil(self):
        print(self.jmeno, self.prijmeni, self.id_facr, self.znamka, self.obtiznost)
        print(self.jmeno_dfa, self.prijmeni_dfa, self.id_facr_dfa)

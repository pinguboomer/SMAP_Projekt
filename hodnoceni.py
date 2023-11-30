from controller import Controller


class Hodnoceni:

    def __init__(self, pdf):
        self.aplikace_interpretace_pf = None
        self.disciplinarni_opatreni = None
        self.fyzicka_kondice = None
        self.spoluprace = None
        self.osobnost_doporuceni = None
        self.pdf = pdf

    def dekodujHodnoceni(self):
        self.aplikace_interpretace_pf = AplikaceInterpretacePF(self.pdf)
        self.aplikace_interpretace_pf.dekodujHodnoceni()
        self.disciplinarni_opatreni = DisclipinarniOpatreni(self.pdf)
        self.disciplinarni_opatreni.dekodujHodnoceni()
        self.fyzicka_kondice = FyzickaKondice(self.pdf)
        self.fyzicka_kondice.dekodujHodnoceni()
        self.spoluprace = Spoluprace(self.pdf)
        self.spoluprace.dekodujHodnoceni()
        self.osobnost_doporuceni = Osobnost(self.pdf)
        self.osobnost_doporuceni.dekodujHodnoceni()

    def printHodnoceni(self):
        self.aplikace_interpretace_pf.printHodnoceni()
        self.disciplinarni_opatreni.printHodnoceni()
        self.fyzicka_kondice.printHodnoceni()
        self.spoluprace.printHodnoceni()
        self.osobnost_doporuceni.printHodnoceni()

    def dejFinalniPopis(self):
        return self.aplikace_interpretace_pf.popis + "\n" + self.disciplinarni_opatreni.popis + \
            "\n" + self.spoluprace.popis + "\n" + self.osobnost_doporuceni.doporuceni


class AplikaceInterpretacePF:
    def __init__(self, pdf):
        self.controller = None
        self.aplikace_interpretace_pf = None
        self.rozhodnuti = None
        self.cit_pro_hru = None
        self.signalizace = None
        self.management_navazani_hry = None
        self.reakce_na_utkani = None
        self.popis = None
        self.pdf = pdf

    def dekodujHodnoceni(self):
        aplikace_interpretace_PF_slovo = \
            self.pdf.pq('LTTextLineHorizontal:contains("{}")'.format("Aplikace a interpretace PF:"))[0]
        page_pq = next(aplikace_interpretace_PF_slovo.iterancestors('LTPage'))
        cislo_stranky = int(page_pq.layout.pageid) - 1
        self.controller = Controller(self.pdf)
        x0, x1, y0, y1, self.aplikace_interpretace_pf = self.controller.ziskej_interpretace_pf(
            aplikace_interpretace_PF_slovo, cislo_stranky)

        y0, y1, self.rozhodnuti = self.controller.ziskej_dalsi_znamku(cislo_stranky, x0, x1, y0, y1)
        y0, y1, self.cit_pro_hru = self.controller.ziskej_dalsi_znamku(cislo_stranky, x0, x1, y0, y1)
        y0, y1, self.signalizace = self.controller.ziskej_dalsi_znamku(cislo_stranky, x0, x1, y0, y1)
        y0, y1, self.pistalka = self.controller.ziskej_dalsi_znamku(cislo_stranky, x0, x1, y0, y1)
        y0, y1, self.management_navazani_hry = self.controller.ziskej_dalsi_znamku(cislo_stranky, x0, x1, y0, y1)
        y0, y1, self.reakce_na_utkani = self.controller.ziskej_dalsi_znamku(cislo_stranky, x0, x1, y0, y1)
        while True:
            y0, y1, popis_1_temp = self.controller.ziskej_dalsi_odstavec(cislo_stranky, x1, y0, y1)
            if popis_1_temp:
                break

        self.popis = popis_1_temp
        while True:
            y0, y1, popis_1_temp = self.controller.ziskej_dalsi_odstavec(cislo_stranky, x1, y0, y1)
            if not popis_1_temp:
                break
            self.popis += " " + popis_1_temp

    def printHodnoceni(self):
        print(self.aplikace_interpretace_pf,
              self.rozhodnuti,
              self.cit_pro_hru,
              self.signalizace,
              self.management_navazani_hry,
              self.reakce_na_utkani)
        print(self.popis)


class DisclipinarniOpatreni:
    def __init__(self, pdf):
        self.controller = None
        self.spravnost_ot = None
        self.proces_ot = None
        self.reakce_na_nch = None
        self.taktika_rizeni = None
        self.komunikace_s_hraci = None
        self.popis = None
        self.pdf = pdf

    def dekodujHodnoceni(self):
        spravnost_ot_slovo = self.pdf.pq('LTTextLineHorizontal:contains("{}")'.format("Správnost udělování OT:"))[0]
        page_pq = next(spravnost_ot_slovo.iterancestors('LTPage'))
        cislo_stranky = int(page_pq.layout.pageid) - 1
        self.controller = Controller(self.pdf)
        x0, x1, y0, y1, self.spravnost_ot = self.controller.ziskej_interpretace_pf(spravnost_ot_slovo, cislo_stranky)

        y0, y1, self.proces_ot = self.controller.ziskej_dalsi_znamku(cislo_stranky, x0, x1, y0, y1)
        y0, y1, self.reakce_na_nch = self.controller.ziskej_dalsi_znamku(cislo_stranky, x0, x1, y0, y1)
        y0, y1, self.taktika_rizeni = self.controller.ziskej_dalsi_znamku(cislo_stranky, x0, x1, y0, y1)
        y0, y1, self.komunikace_s_hraci = self.controller.ziskej_dalsi_znamku(cislo_stranky, x0, x1, y0, y1)
        while True:
            y0, y1, popis_1_temp = self.controller.ziskej_dalsi_odstavec(cislo_stranky, x1, y0, y1)
            if popis_1_temp:
                break

        self.popis = popis_1_temp
        while True:
            y0, y1, popis_1_temp = self.controller.ziskej_dalsi_odstavec(cislo_stranky, x1, y0, y1)
            if not popis_1_temp:
                break
            self.popis += " " + popis_1_temp

    def printHodnoceni(self):
        print(self.spravnost_ot,
              self.proces_ot,
              self.reakce_na_nch,
              self.taktika_rizeni,
              self.komunikace_s_hraci)
        print(self.popis)


class FyzickaKondice:
    def __init__(self, pdf):
        self.controller = None
        self.pozicni_postaveni = None
        self.vyber_mista = None
        self.rychlost_pohyb = None
        self.pdf = pdf

    def dekodujHodnoceni(self):
        fyzicka_kondice_slovo = \
            self.pdf.pq('LTTextLineHorizontal:contains("{}")'.format("Vhodnost a správnost pozičního postavení:"))[0]
        page_pq = next(fyzicka_kondice_slovo.iterancestors('LTPage'))
        cislo_stranky = int(page_pq.layout.pageid) - 1
        self.controller = Controller(self.pdf)
        x0, x1, y0, y1, self.pozicni_postaveni = self.controller.ziskej_fyzicka_kondice(fyzicka_kondice_slovo,
                                                                                        cislo_stranky)

        y0, y1, self.vyber_mista = self.controller.ziskej_dalsi_znamku(cislo_stranky, x0, x1, y0, y1)
        y0, y1, self.rychlost_pohyb = self.controller.ziskej_dalsi_znamku(cislo_stranky, x0, x1, y0, y1)

    def printHodnoceni(self):
        print(self.pozicni_postaveni,
              self.vyber_mista,
              self.rychlost_pohyb)


class Spoluprace:
    def __init__(self, pdf):
        self.controller = None
        self.ocni_kontakt_s_ar = None
        self.skryta_signalizace = None
        self.popis = None
        self.pdf = pdf

    def dekodujHodnoceni(self):
        ocni_kontakt_s_ar_slovo = \
            self.pdf.pq('LTTextLineHorizontal:contains("{}")'.format("Oční kontakt mezi R a AR:"))[0]
        page_pq = next(ocni_kontakt_s_ar_slovo.iterancestors('LTPage'))
        cislo_stranky = int(page_pq.layout.pageid) - 1
        self.controller = Controller(self.pdf)
        x0, x1, y0, y1, self.ocni_kontakt_s_ar = self.controller.ziskej_interpretace_pf(ocni_kontakt_s_ar_slovo,
                                                                                        cislo_stranky)

        y0, y1, self.skryta_signalizace = self.controller.ziskej_dalsi_znamku(cislo_stranky, x0, x1, y0, y1)

        while True:
            y0, y1, popis_1_temp = self.controller.ziskej_dalsi_odstavec(cislo_stranky, x1, y0, y1)
            if popis_1_temp:
                break

        self.popis = popis_1_temp
        while True:
            y0, y1, popis_1_temp = self.controller.ziskej_dalsi_odstavec(cislo_stranky, x1, y0, y1)
            if not popis_1_temp:
                break
            self.popis += " " + popis_1_temp

    def printHodnoceni(self):
        print(self.ocni_kontakt_s_ar,
              self.skryta_signalizace)
        print(self.popis)


class Osobnost:
    def __init__(self, pdf):
        self.controller = None
        self.osobnost = None
        self.chovani_r_utkani = None
        self.chovani_r_mimo_utkani = None
        self.duslednost = None
        self.koncentrace = None
        self.doporuceni = None
        self.pdf = pdf

    def dekodujHodnoceni(self):
        osobnost_slovo = self.pdf.pq('LTTextLineHorizontal:contains("{}")'.format("Osobnost R:"))[0]
        page_pq = next(osobnost_slovo.iterancestors('LTPage'))
        cislo_stranky = int(page_pq.layout.pageid) - 1
        self.controller = Controller(self.pdf)
        x0, x1, y0, y1, self.osobnost = self.controller.ziskej_osobnost(osobnost_slovo, cislo_stranky)

        y0, y1, self.chovani_r_utkani = self.controller.ziskej_dalsi_znamku(cislo_stranky, x0, x1, y0, y1)
        y0, y1, self.chovani_r_mimo_utkani = self.controller.ziskej_dalsi_znamku(cislo_stranky, x0, x1, y0, y1)
        y0, y1, self.duslednost = self.controller.ziskej_dalsi_znamku(cislo_stranky, x0, x1, y0, y1)
        y0, y1, self.koncentrace = self.controller.ziskej_dalsi_znamku(cislo_stranky, x0, x1, y0, y1)

        while True:
            y0, y1, popis_1_temp = self.controller.ziskej_dalsi_odstavec(cislo_stranky, x1, y0, y1)

            if popis_1_temp:
                break
            if y0 < 0:
                cislo_stranky = cislo_stranky + 1
                temp = self.pdf.pq(
                    'LTPage[page_index="{}"] LTTextLineHorizontal:contains("{}")'.format(cislo_stranky, "Doporučení:"))[
                    0]
                y1 = float(temp.get('y1', 0))
                y0 = float(temp.get('y0', 0))

        self.doporuceni = popis_1_temp
        count = 0
        while True:
            y0, y1, popis_1_temp = self.controller.ziskej_dalsi_odstavec(cislo_stranky, x1, y0, y1)
            if not popis_1_temp:
                if count == 1:
                    break
                else:
                    count = count + 1
            else:
                if count == 1:
                    count = 0
            self.doporuceni += " " + popis_1_temp

    def printHodnoceni(self):
        print(self.osobnost, self.chovani_r_utkani,
              self.chovani_r_mimo_utkani,
              self.duslednost,
              self.koncentrace)
        print(self.doporuceni)

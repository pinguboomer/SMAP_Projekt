class Controller:
    def __init__(self, pdf):
        self.pdf = pdf

    def ziskej_interpretace_pf(self, slovo, stranka):
        x0 = float(slovo.get('x0', 0)) + 125
        y0 = float(slovo.get('y0', 0))
        x1 = float(slovo.get('x1', 0)) + 35
        y1 = float(slovo.get('y1', 0))
        return x0, x1, y0, y1, self.pdf.pq(
            'LTPage[page_index="{}"] LTTextLineHorizontal:overlaps_bbox("%s, %s, %s, %s")'.format(stranka) % (
                x0, y0, x1, y1)).text()

    def ziskej_fyzicka_kondice(self, slovo, stranka):
        x0 = float(slovo.get('x0', 0)) + 165
        y0 = float(slovo.get('y0', 0))
        x1 = float(slovo.get('x1', 0)) + 65
        y1 = float(slovo.get('y1', 0))
        return x0, x1, y0, y1, self.pdf.pq(
            'LTPage[page_index="{}"] LTTextLineHorizontal:overlaps_bbox("%s, %s, %s, %s")'.format(stranka) % (
                x0, y0, x1, y1)).text()

    def ziskej_osobnost(self, slovo, stranka):
        x0 = float(slovo.get('x0', 0)) + 65
        y0 = float(slovo.get('y0', 0))
        x1 = float(slovo.get('x1', 0)) + 105
        y1 = float(slovo.get('y1', 0))
        return x0, x1, y0, y1, self.pdf.pq(
            'LTPage[page_index="{}"] LTTextLineHorizontal:overlaps_bbox("%s, %s, %s, %s")'.format(stranka) % (
                x0, y0, x1, y1)).text()



    def ziskej_dalsi_znamku(self, stranka, x0, x1, y0, y1):
        y0 = y0 - 13
        y1 = y1 - 13
        znamka = self.pdf.pq(
            'LTPage[page_index="{}"] LTTextLineHorizontal:overlaps_bbox("%s, %s, %s, %s")'.format(stranka) % (
                x0, y0, x1, y1)).text()
        if str(znamka).isnumeric():
            return y0, y1, znamka
        return y0, y1, None


    def ziskej_text_k_celku(self, stranka, x1, y0, y1):
        y0 = y0 - 20
        y1 = y1 - 20
        x0 = 30
        return y0, y1, self.pdf.pq(
            'LTPage[page_index="{}"] LTTextLineHorizontal:overlaps_bbox("%s, %s, %s, %s")'.format(stranka) % (
                x0, y0, x1, y1)).text()

    def ziskej_dalsi_odstavec(self, stranka, x1, y0, y1):
        y0 = y0 - 13
        y1 = y1 - 13
        x0 = 20
        x1 = 535
        return y0, y1, self.pdf.pq(
            'LTPage[page_index="{}"] LTTextLineHorizontal:overlaps_bbox("%s, %s, %s, %s")'.format(stranka) % (
                x0, y0, x1, y1)).text()

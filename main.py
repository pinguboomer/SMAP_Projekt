import nltk

from pdfquery import PDFQuery
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from profil import Profil

cesty = {'d:\\template_1.pdf', 'd:\\template_2.pdf', 'd:\\template_3.pdf', 'd:\\template_4.pdf', 'd:\\template_5.pdf'}
posudky = []
print("start")
finalniPopisAplikacePF = ""
finalniPopisDisciplinarniOpatreni = ""
finalniPopisSpoluprace = ""
finalniPopisDoporuceni = ""

for cesta in cesty:
    pdf = PDFQuery(cesta)
    pdf.load()
    Rozhodci1 = Profil()
    Rozhodci1.dekodujHodnoceni(pdf)
    #Rozhodci1.printPosudek()
    finalniPopisAplikacePF += Rozhodci1.hodnoceni.aplikace_interpretace_pf.popis
    finalniPopisDisciplinarniOpatreni += Rozhodci1.hodnoceni.disciplinarni_opatreni.popis
    finalniPopisSpoluprace += Rozhodci1.hodnoceni.spoluprace.popis
    finalniPopisDoporuceni += Rozhodci1.hodnoceni.osobnost_doporuceni.doporuceni
    posudky.append(Rozhodci1)
    print(Rozhodci1.prijmeni, Rozhodci1.znamka, " DFA: ", Rozhodci1.prijmeni_dfa)
print()

# print()
# gen_summary = summarize()
# print(gen_summary)
# nltk.download('punkt')
# Creating text parser using tokenization
parser = PlaintextParser.from_string(finalniPopisAplikacePF, Tokenizer("czech"))

# Summarize using sumy TextRank
summarizer = TextRankSummarizer()
summary = summarizer(parser.document, 2)

text_summary = ""
for sentence in summary:
    text_summary += str(sentence)

print(text_summary)
print()
summarizer_lex = LexRankSummarizer()

# Summarize using sumy LexRank
# summary = summarizer_lex(parser.document, 2)
# lex_summary = ""

# for sentence in summary:
#     lex_summary += str(sentence)
# print(lex_summary)

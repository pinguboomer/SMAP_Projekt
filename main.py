import nltk

from pdfquery import PDFQuery
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.kl import KLSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from profil import Profil

cesty = {'d:\\template_1.pdf', 'd:\\template_2.pdf', 'd:\\template_3.pdf', 'd:\\template_4.pdf', 'd:\\template_5.pdf'}
posudky = []
print("start")
finalniPopisAplikacePF = ""
finalniPopisDisciplinarniOpatreni = ""
finalniPopisSpoluprace = ""
finalniPopisDoporuceni = ""
finalniPopis = ""

for cesta in cesty:
    pdf = PDFQuery(cesta)
    pdf.load()
    Rozhodci1 = Profil()
    Rozhodci1.dekodujHodnoceni(pdf)
    finalniPopisAplikacePF += Rozhodci1.hodnoceni.aplikace_interpretace_pf.popis
    finalniPopisDisciplinarniOpatreni += Rozhodci1.hodnoceni.disciplinarni_opatreni.popis
    finalniPopisSpoluprace += Rozhodci1.hodnoceni.spoluprace.popis
    finalniPopisDoporuceni += Rozhodci1.hodnoceni.osobnost_doporuceni.doporuceni
    posudky.append(Rozhodci1)
    print(Rozhodci1.prijmeni, Rozhodci1.znamka, " DFA: ", Rozhodci1.prijmeni_dfa)

print()
finalniPopis = finalniPopisAplikacePF + finalniPopisDisciplinarniOpatreni + finalniPopisSpoluprace + finalniPopisDoporuceni
# print(gen_summary)
# nltk.download('punkt')
# Creating text parser using tokenization
parser = PlaintextParser.from_string(finalniPopis, Tokenizer("czech"))

# Summarize using sumy TextRank
summarizer = TextRankSummarizer()
summary = summarizer(parser.document, 5)

text_summary = ""
for sentence in summary:
    text_summary += str(sentence) + "\n"

print("TextRank:", text_summary)
print()
summarizer_lex = LexRankSummarizer()

# Summarize using sumy LexRank
summary = summarizer_lex(parser.document, 5)
lex_summary = ""

for sentence in summary:
    lex_summary += str(sentence) + "\n"

print("LexRank:", lex_summary)
print()

summarizer_lsa = LsaSummarizer()
# Summarize using sumy LSA
summary = summarizer_lsa(parser.document, 5)

lsa_summary = ""
for sentence in summary:
    lsa_summary += str(sentence) + "\n"

print("LSA:", lsa_summary)
print()

summarizer_kl = KLSummarizer()

# Summarize using sumy KL Divergence
summary = summarizer_kl(parser.document, 5)

kl_summary = ""
for sentence in summary:
    kl_summary += str(sentence)

print("KL Divergence:", kl_summary)
print()

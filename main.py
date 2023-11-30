import nltk

from pdfquery import PDFQuery
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from profil import Profil

print("start")
pdf = PDFQuery('d:\\template_5.pdf')
pdf.load()

Rozhodci1 = Profil()
Rozhodci1.dekodujHodnoceni(pdf)
Rozhodci1.printPosudek()
print()

finalniPopis = Rozhodci1.hodnoceni.dejFinalniPopis()
print(Rozhodci1.hodnoceni.dejFinalniPopis())

# print()
# gen_summary = summarize()
# print(gen_summary)
nltk.download('punkt')
# Creating text parser using tokenization
parser = PlaintextParser.from_string(finalniPopis, Tokenizer("czech"))

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
summary = summarizer_lex(parser.document, 2)
lex_summary = ""

for sentence in summary:
    lex_summary += str(sentence)
print(lex_summary)

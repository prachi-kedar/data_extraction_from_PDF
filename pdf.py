import PyPDF2 as p

file = open("/home/webwerks/Downloads/Machine_Learning_A_Z_Q_A.pdf", "rb")
pd = p.PdfFileReader(file)

x = pd.getPage(12)

# y = pd.getPage(1)

print(x.extractText())
# print(y.extractText())

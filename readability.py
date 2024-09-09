from cs50 import get_string

text = get_string("Text: ")

lenght = len(text)

numletra = 0

numfrase = 0

for i in range(lenght):
    if text[i].isalpha():
        numletra += 1
    if text[i].count(".") or text[i].count("!") or text[i].count("?"):
        numfrase += 1

numpalavra = len(text.split())

meletra = (numletra*100)/numpalavra
mefrase = (numfrase*100)/numpalavra
index = round((0.0588*meletra)-(0.296*mefrase)-15.8)

if index < 1:
    print("Befora Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")

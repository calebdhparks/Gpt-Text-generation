import PyPDF2
import re
with open("hp_input.txt", "w", encoding="utf8") as out_file:
    # for file in glob.glob("*.pdf"):
    file = "Harry Potter - Book 7 - The Deathly Hallows.pdf"
    # with open(file, "r", encoding="utf8") as in_file:
    reader = PyPDF2.PdfReader(file)

    # print the number of pages in pdf file
    print(file)
    print(len(reader.pages))
    page_num = len(reader.pages)

    for i in range(8,page_num):
        # print the text of the first page
        A = re.sub(' +', ' ', reader.pages[i].extract_text())
        split = A.find("\n")
        A = A[split:]
        # print(A[:split])
        split = A.rfind("\n")
        A = A[:split]
        out_file.write(A)
        # print(A)
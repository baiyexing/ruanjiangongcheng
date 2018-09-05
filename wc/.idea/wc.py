chars = 0
word = 0
row = 0
blank_row = 0
code_row = 0
with open("test.txt", "r", encoding = "gbk") as file:
    strs = file.read()
    gr = strs.split("\n")
    row = len(gr)
    for line in gr:
        if line.strip() == '':
            blank_row += 1
        else:
            code_row += 1
            for e in line:
                if e != ' ':
                    chars += 1
print(chars)
print(row)
print(blank_row)
print(code_row)

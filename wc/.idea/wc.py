chars = 0
word = 0
row = 0
blank_row = 0
code_row = 0
flage =0
import sys
#args = sys.args[0]
def main():
    with open("sys.argv[j]", "r", encoding = "gbk") as file:
        strs = file.read()
        gr = strs.split("\n")
        row = len(gr)
        for line in gr:
            i=0
            if line.strip() == '':
                blank_row += 1
            else:
                code_row += 1
                for e in line:
                    i +=1
                    if e != ' ':
                        chars += 1
                    if  e.isalpha() or e.isdigit() or e =='-':
                        flage = 1
                        if i==len(line) and flage == 1:
                            word += 1
                            flage = 0
                    elif flage  == 1 :
                        word += 1
                        flage = 0

    print("字符数为：" ,chars)
    print("总行数为：" , row)
    print("空行数为：" , blank_row)
    print("代码行为：" , code_row)
    print("单词数为:" ,word)
import sys
import os
func = sys.argv[1]
func2 = sys.argv[2]
def readfile(name):
    with open( name, "r", encoding = "gbk") as file:
        chars = 0
        word = 0
        row = 0
        blank_row = 0
        code_row = 0
        comment_row = 0
        flage =0
        chaniese =0
        strs = file.read()
        gr = strs.split("\n")
        row = len(gr)
        for line in gr:
            i=0
            zs = line.split("//")
            zs1 = line.split("/*")
            if line.strip() == ''or len(line.strip()) == 1:
                blank_row += 1
            elif  len(zs[0]) <= 1 or len(zs1[0]) <= 2 : #line.find('/*') > -1 or line.find('//') > -1:
                comment_row += 1
            else:      #len(line.strip()) != 1:
                code_row += 1
                for e in line:
                    i +=1
                    if e != ' ':
                        chars += 1
                    if '\u4e00'<= e <= '\u9fff' :
                        chaniese +=1
                    if   e.isalpha() or e.isdigit() or e =='-' :
                        flage = 1
                        if i==len(line) and flage == 1:
                            word += 1
                            flage = 0
                    elif flage  == 1 :
                        word += 1
                        flage = 0

    return  row,blank_row,code_row,comment_row,chars,word,chaniese
	
res = readfile(sys.argv[2])
if func == "-c" :
	print("字符数为：" ,res[4])
if func == "-l" :
    print("总行数为：" , res[0])
if func == "-w":
    print("单词数为:" ,res[5])
    print ("中文字数为：",res[6])
if func == "-a" :
    print("空行数为：" , res[1])
    print("代码行为：" , res[2])
    print ("注释行为：",res[3])
if func == "all" :
    print("总行数为：" , res[0])
    print("空行数为：" , res[1])
    print("代码行为：" , res[2])
    print ("注释行为：",res[3])
    print("字符数为：" ,res[4])
    print("单词数为:" ,res[5])
    print ("中文字数为：",res[6])
if func == "-s" :
    filelist = os.listdir(os.getcwd())
    for n in filelist :
        if os.path.isfile(n):
            if os.path.splitext(n)[1] == os.path.splitext(sys.argv[3])[1]:
                if func2 == "-c" :
                    print("字符数为：" ,res[4])
                if func2 == "-l" :
                    print("总行数为：" , res[0])
                if func2 == "-w":
                    print("单词数为:" ,res[5])
                    print ("中文字数为：",res[6])
                if func2 == "-a" :
                    print("空行数为：" , res[1])
                    print("代码行为：" , res[2])
                    print ("注释行为：",res[3])
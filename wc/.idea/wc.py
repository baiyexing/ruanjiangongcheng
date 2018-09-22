import sys
import os
if len(sys.argv ) < 3:
    print ("输入参数错误")
else :
        func = sys.argv[1]
        func2 = sys.argv[2]
        def readfile(name):
            list = os.listdir(os.getcwd())
            if name in list:
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
                        zs = line.split('//')
                        zs1 = line.split('/*')
                        if line.strip() == ''or len(line.strip()) == 1:
                            blank_row += 1
                        elif  len(zs[0]) <= 1 and zs[0] != '"'or len(zs1[0]) <= 1 and zs1 [0] != ' " ' :
                            comment_row += 1
                        else:
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
            else:
                print(name,"文件不存在")

try :
    if func!="-s" :
        res = readfile(sys.argv[2])
    if func == "-c" :
        print("字符数为：" ,res[4])
    if func == "-l" :
        print("总行数为：" , res[0])
    if func == "-w":
        print("单词数为:" ,res[5],"\n中文字数为：",res[6])
    if func == "-a" :
        print("空行数为：" , res[1],"\n代码行为：" , res[2],"\n注释行为：",res[3])
    if func == "all" :
        print("总行数为：" , res[0])
        print("空行数为：" , res[1])
        print("代码行为：" , res[2])
        print ("注释行为：",res[3])
        print("字符数为：" ,res[4])
        print("单词数为：" ,res[5])
        print ("中文字数为：",res[6])
    if func == "-s" :
        if func2 !="-w" and func2 !="-l" and func2 !="-a" and func2 !="-c" :
            print ("输入参数错误")
        filelist = os.listdir(os.getcwd())
        for n in filelist :
            if os.path.isfile(n):
                if os.path.splitext(n)[1] == os.path.splitext(sysif.argv[3])[1]:
                    res1 = readfile(n)
                    if func2 == "-c" :
                        print( "\n文件名：",n,"\n字符数为：" ,res1[4])
                    if func2 == "-l" :
                        print("\n文件名：",n,"\n总行数为：" , res1[0])
                    if func2 == "-w":
                        print("\n文件名：",n,"\n单词数为:" ,res1[5],"\n中文字数为：",res1[6])
                    if func2 == "-a" :
                        print("\n文件名：",n,"\n空行数为：" , res1[1],"\n代码行为：" , res1[2],"\n注释行为：",res1[3])
    if func !="-s"and func !="-c"and func !="-w"and func !="-l"and func !="-a":
        print("输入参数错误")
except BaseException :
    exit(1)
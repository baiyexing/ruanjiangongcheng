import random
import  math



class Question:
    expression_array = []#表达式列表
    expression = " "#表达式表示
    answer = 0         #答案
    answer_char = " "  #答案表示
    number_range = 10  #操作数范围
    probability = 0.5 #分数出现的概率
    count = 4
    def __init__(self,number_range,count,probability):

        self.number_range = number_range
        self.count = count
        self.probability = probability

        result = self.expression2(self.count)
        print(result)
        self.expression_array = result['expression_array']
        self.expression = result['expression']
        self.answer = result['answer']
        self.answer_char = str(self.fraction_char(result['answer']))
        print(self.answer_char)

    def fraction_char(self,figure_array):#获得分数的表示形式
        figure1 = figure_array[0]
        figure2 = figure_array[1]
        if figure2 == 1:
            return figure1
        elif(figure1>figure2):
            quotient = int (figure1/figure2)
            figure1 = figure1 - (quotient*figure2)
            return  str(quotient) +"'" + str(figure1) + "/" + str(figure2)
        else:
            return  str(figure1) + "/" + str(figure2)

    def random_fraction(self):#获得随机分数
        number_range = self.number_range
        while True:
            figure1 = self.getrandom(number_range)
            figure2 = self.getrandom(number_range)
            if (figure1 % figure2)== 0 or figure2 == 0:
                continue
            else :
                break
        return self.Simple_fraction(figure1,figure2)

    def getnumber(self) : # 获得随机运算数字
        number_range = self.number_range
        probability= self.probability

        probability *= 100
        probability = int(probability)

        result = { }
        if self.getrandom(100) <= probability:
            figure = self.random_fraction()
            result['figure'] = figure[0]/figure[1]
            result['figure_char'] =self.fraction_char(figure)
            result['figure_array'] =  [figure[0],figure[1]]
        else :
            figure = self.getrandom(number_range-1)
            result['figure'] = figure
            result['figure_char'] = str(figure)
            result['figure_array'] =  [figure,1]
        return result
    def operator_char(self,operator) :# 获取运算符号表示形式
        operatorArray = ['+','-','×','÷']
        return operatorArray[operator-1]

    def getrandom(self,range): # 获取一个随机数
        return random.randint(1,range)

    def Calculation(self,figure1,figure2,operate):#计算算式的结果
        if operate == 1:
            numerator = figure1[0]*figure2[1]+figure2[0]*figure1[1]
            denominator = figure1[1]*figure2[1]
        elif operate == 2:
            numerator = figure1[0]*figure2[1]-figure2[0]*figure1[1]
            denominator = figure1[1]*figure2[1]
            if numerator < 0:
                return [numerator,denominator]
        elif operate == 3:
            numerator = figure1[0]*figure2[0]
            denominator = figure1[1]*figure2[1]
        elif operate == 4 :
            numerator = figure1[0]*figure2[1]
            denominator = figure1[1]*figure2[0]
        result = self.Simple_fraction(numerator,denominator)
        return result

    def Simple_fraction(self,numerator,denominator):#化为最简分数
        numerator_factors = self.get_factors(numerator)
        denominator_factors = self.get_factors(denominator)

        if len(numerator_factors)==0 or len(denominator_factors)==0:
            return [numerator,denominator]
        else :
            flage = 0
            for factor in numerator_factors:
                if factor in denominator_factors:
                    flage = factor
            if flage != 0:
                numerator = int (numerator/flage)
                denominator = int (denominator/flage)
            return [numerator,denominator]

    def get_factors(self,figure):#获得数的因数列表
        list = []
        for factors in range(2,figure+1):
            if (figure % factors) == 0:
                list.append(factors)
        return list

    def expression2(self,count):
        if count == 1:
            figure = self.getnumber()
            return{
                'expression_array': figure['figure'],
                'expression':       figure['figure_char'],
                'answer':           figure['figure_array']
            }
        else :
            leftcount = self.getrandom(count -1)
            rightcount = count - leftcount

            left = self.expression2(leftcount)
            right = self.expression2(rightcount)

            operate = self.getrandom(4)


            if operate == 4 and right['answer'][0] == 0:
                 t = left
                 left = right
                 right = t
            answer = self.Calculation(left['answer'],right['answer'],operate)
            if answer[0] < 0:
                 t = left
                 left = right
                 right = t
                 answer = self.Calculation(left['answer'],right['answer'],operate)

            leftvalue = left['answer'][0]/left['answer'][1]
            rightvalue = right['answer'][0]/right['answer'][1]
            expression_array = [left['expression_array'],operate,right['expression_array']]
            if type(left['expression_array'])!=list and type(right['expression_array'])!=list: #两个子树都为值
                if (operate == 1 or operate == 3) and leftvalue < rightvalue:
                    expression_array = [right['expression_array'],operate,left['expression_array']]
            elif  type(left['expression_array'])==list and type(right['expression_array'])==list:# 两个子树都为树
                if operate == 1 or operate == 3:
                    if leftvalue == rightvalue and left['expression_array'][1] < right['expression_array'][1]:#树的值相等时，运算符优先级高的在左边
                        expression_array = [right['expression_array'],operate,left['expression_array']]
                    elif leftvalue < rightvalue :
                        expression_array = [right['expression_array'],operate,left['expression_array']]
                if operate in [3,4] :
                    if left['expression_array'][1] in [1,2]:
                        left['expression'] = '(' + left['expression'] + ')'
                    if right['expression_array'][1] in [1,2]:
                        right['expression'] = '(' + right['expression'] + ')'
            else:#一边的子树为树
                if operate == 1 or operate == 3:
                    if type(right['expression_array']) == list:
                        expression_array = [right['expression_array'],operate,left['expression_array']]
                if operate in [3,4] :
                    if type(left['expression_array']) == list and left['expression_array'][1] in [1,2] :
                        left['expression'] = '(' + left['expression'] + ')'
                    if type(right['expression_array']) == list and right['expression_array'][1] in[1,2]:
                        right['expression'] = '(' + right['expression'] + ')'
            expression = left['expression']+self.operator_char(operate)+right['expression']
            return {
                'expression_array':  expression_array,
                'expression':        expression,
                'answer':            answer
            }




n = 10
while n != 0:
    print(n)
    app = Question(10,3,0)
    n -= 1



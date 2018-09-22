import  random
def random_fraction():#获得随机分数
    number_range = 10
    while True:
        figure1 = getrandom(number_range)
        figure2 = getrandom(number_range)
        if (figure1 % figure2)== 0:
            continue
        else :
            break

    return Simple_fraction(figure1,figure2)


def Simple_fraction(numerator,denominator):#化为最简真分数
    numerator_factors = get_factors(numerator)
    denominator_factors = get_factors(denominator)

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

def get_factors(figure):#获得数的因数列表
    list = []
    for factors in range(2,figure+1):
        if (figure % factors) == 0:
            list.append(factors)
    return list

def getrandom(range): # 获取一个随机数
    return random.randint(1,range)

def fraction_char(figure_array):#获得分数的表示形式
    figure1 = figure_array[0]
    figure2 = figure_array[1]
    if figure2 == 1:
        return figure1
    if(figure1>figure2):
        quotient = int (figure1/figure2)
        figure1 = figure1 - (quotient*figure2)
        return  str(quotient) +"'" + str(figure1) + "/" + str(figure2)
    else:
        return  str(figure1) + "/" + str(figure2)


def getnumber() : # 获得随机运算数字
    number_range = 10
    probability= 0.5

    probability *= 100
    probability = int(probability)

    result = { }
    #if getrandom(100) <= probability:
    figure = random_fraction()
    result['figure'] = figure[0]/figure[1]
    result['figure_char'] =fraction_char(figure)
    result['figure_array'] =  [figure[0],figure[1]]
    # else :
    #     figure = getrandom(number_range-1)
    #     result['figure'] = figure
    #     result['figure_char'] = str(figure)
    #     result['figure_array'] =  [figure,1]
    return result

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


def expression2(count):
    if count == 1:
        figure = getnumber()
        dic={
            'expression_array': figure['figure']
        }
        return dic
    else :
        leftcount = getrandom(count -1)
        rightcount = count - leftcount

        left = expression2(leftcount)
        right = expression2(rightcount)
        operate = getrandom(4)
        expression_array = [left['expression_array'],operate,right['expression_array']]


        return {
            'expression_array':  expression_array
        }
while getrandom(10)!=0:
    print(getrandom(10))

    #print(expression2(3))
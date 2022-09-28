import sys
import math

def coef_isdigit(n):
    n = n.replace('-','')
    return n.replace('.','').isdigit()

def coef ( index, name_coef):
    try:

        coef_str = sys.argv[index]
        if ((index==1) and (coef_str=='0')):
            coef_str=1/0
        coef = float(coef_str)


    except:
        while(True):
            print(name_coef)
            str = input()
            if(coef_isdigit(str)):
                break
        coef=float(str)
        return coef
    # while (True):
    #     print(name_coef)
    #     coef_str = input()
    #     if (coef_isdigit(coef_str)):
    #         break
    # coef=float(coef_str)
    return coef
def counting(A,B,C):
    result = []

    D=B*B-4*A*C
    t1=((-B)+ math.sqrt(D)) / (2 * A)
    t2=((-B)+ math.sqrt(D)) / (2 * A)
    if (D==0):
        if t1>=0:
            x1=(-B)/(2*A)
            result.append(x1)
    if (D > 0):
            if t1>=0:
                x2 = -math.sqrt(t1)
                x3 = math.sqrt(t1)
                result.append(x2)
                result.append(x3)
            if t2 >= 0:
                x4 = -math.sqrt(t2)
                x5 = math.sqrt(t2)
                if (x4!=x2):
                    result.append(x4)
                if (x5!=x3):
                    result.append(x5)
    return result


def main():

    a = coef(1, "Введите коэффициент A:")
    b = coef(2, "Введите коэффициент B:")
    c = coef(3, "Введите коэффициент C:")

    result = counting(a,b,c)
    if len(result)==0:
        print("Нет корней!")
    if len(result)==1:
        print("Один корень:",result[0])
    if len(result) == 2:
        print("Два корня:", result[0], result[1])
    if len(result) == 4:
        print("Четыре корня:",result[0],result[1],result[2],result[3])



if __name__ == '__main__':
    main()


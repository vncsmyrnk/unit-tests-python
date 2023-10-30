def triangle(lenA, lenB, lenC):
    if(isinstance(lenA,int) and isinstance(lenB,int) and isinstance(lenC,int)):
        if(lenA>0 and lenB>0 and lenC>0):
            if lenA == lenB == lenC:
                return "Equilateral"
            elif lenA == lenB or lenB == lenC or lenC == lenA:
                return "Isoscalene"
            else:
                return "Scalene"
        else:
            return "Error, values must be >0"
    else:
        return "Not integer"


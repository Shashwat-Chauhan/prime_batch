def genPara(s , n: int, opening_count: int , closing_count:int):
    if (opening_count == n and closing_count == n):
        print(s)
        return

    if opening_count == closing_count:
        s += '('
        genPara(s , n , opening_count + 1, closing_count)

    
    else:
        if opening_count == n:
            s += ')'
            genPara(s , n , opening_count , closing_count + 1)
        else:
            genPara(s + '(' , n , opening_count + 1 , closing_count )
            genPara(s + ')' , n , opening_count , closing_count + 1)

n = 3
s = ""
genPara(s , n , 0 , 0)


        
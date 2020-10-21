def solution():
    num=10
    mult=[]
    for i in range(1,num):
        if i%3==0:
            mult.append(i)
        if i%5==0 and i%3!=0:
            mult.append(i)
    suma=sum(mult)
    print(mult)
    print(suma)
    return suma
            
if __name__ == "__main__":
   solution()      
def straight(list):
    straight=True
    
    for i in range(len(list)-1):
        if list[i]+1!=list[i+1]:
                straight=False
        
    if straight==True:
        print('Straight')
    else:
        print('Not straight')

if __name__=="__main__":
    list=[2,3,4,4,6]
    straight(list)
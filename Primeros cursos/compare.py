def duplicate_count(text):
    s=text.lower()
    n=len(s)

    r=0
    for i in range(0,n):

        for k in range(i+1,n):
            print(s[i] + '      '+ s[k])
            if s[i]==s[k]:
                
                r+=1
                print(str(r))


    return r
        
        
if __name__ == "__main__":
    duplicate_count('indivisibility')
    
     
print("Usage:")
print("    >>10 9", "ans: 9.5", sep="\n    ")
print("or")
print("    >>10", ">>9", "ans: 9.5", sep="\n    ")
print("-----")
while True:
    a=-1
    count=0
    suum=0
    while a!="":
        a=input(">>")
        if(a=="quit" or a=="exit" or a=="q"): exit()
        i=0
        while(i<len(a)):
            n=0
            nmb="0"
            while(i+n<len(a) and a[i+n].isdigit()):
                nmb+=a[i+n]
                n+=1
            suum+=int(nmb)
            count+=1
            if(n>0): i+=n
            else: i+=1
    count-=1
    if(count!=-1): print("ans: ", suum/count)
    print("-----")

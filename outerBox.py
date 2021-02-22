def inner(string, width):
	  return string + " " * (width - len(string))	
def longesti(li):
    longest=0
    for i in range(len(li)):
        if(len(str(li[i]))>len(str(li[longest]))):
            longest=i
    return longest
def outer(words):
    longest=longesti(words)
    w = len(str(words[longest]))
    print("*" * (w + 4))
    for i in words:
      print("* " + inner(i, w) + " *")
    print("*" * (w + 4))
ans="0"
li=[]
while(ans!="end"):
    ans=input(">>")
    if(ans!="end"): li.append(ans)
outer(li)

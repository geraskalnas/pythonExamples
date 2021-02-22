import time
import os


def secToText(d, diff=True):
    d=time.localtime(d)
    if (diff):
        return f"{d.tm_mday-1} dienu, {d.tm_hour-2} valandu, {d.tm_min} minuciu, {d.tm_sec} sekundziu"
    return f"{d.tm_year} metu, {d.tm_mon} menesiu, {d.tm_mday} dienu, {d.tm_hour} valandu, {d.tm_min} minuciu, {d.tm_sec} sekundziu"

def raport(d, su):
    print("Skirtumas DABAR:", secToText(d, True))
    print("Skirtumas is VISO:", secToText(su, True))

def saveStatus(filename, seconds):
    with open(filename, "a") as f:
        f.write(str(seconds)+"\n")

today = time.localtime()
filename = f"{today.tm_year}-{today.tm_mon}-{today.tm_mday}.txt"
status=""
su=0


if(input(filename+" [Y/n]: ")=="n"):
    filename = input("filename: ")


isPause = True
#print(diff(time.time(), time.mktime(today)))

if (os.path.isfile(filename)):
    with open(filename, "r") as f:
        for line in f:
            try:
                if(isPause):
                    l=float(line)
                else:
                    l1=l
                    l=float(line)
                    su+=l-l1
                isPause=not isPause
            except ValueError:
                continue
               
if(su>0):
    print("Imported from file")
    raport(0, su)
    print("NEW")

while(input("P")!="exit"):
    if(isPause):
        l=time.time()
        print("Screen-time ACTIVE", secToText(l, False))
    else:
        l1=l
        l=time.time()
        print("Screen-time STOPPED", secToText(l, False))
        #
        d=l-l1
        su+=d
        raport(d, su)
    saveStatus(filename, l)
    isPause=not isPause
    
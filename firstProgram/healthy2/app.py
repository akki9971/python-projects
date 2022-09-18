import time
from plyer import notification
from datetime import datetime

n1=0
n2=0
n3=0

a=18
b=27
c=12

x=6
z=12

def log(file,n):
    # datetime_str = "31OCT2020231032"
    x = datetime.now()
    date = x.strftime("%x")
    time = x.strftime("%X")
    name=(str(file)+".txt")

    f=open(name,"a")
    t=str(n)+". "+str(date)+"  "+str(time)+"\n"
    f.write(t)
    f.close()


def eye():
    notification.notify(
        title = 'Eye Exercise',
        message = 'Time to exercise your eyes',
        timeout = 2,
        # app_icon = "eye.ico"
    )
    global n1
    n1+=1
    log("eye",n1)
    

    x=6
    z=12

def exercise():
    notification.notify(
        title = 'Physical Exercise',
        message = 'Time for physical exercise',
        timeout = 2,
        # app_icon = "dumbbell.ico"
    )
    global n2
    n2+=1
    log("exercise",n2)
    
    x=6
    z=12

def water():
    notification.notify(
        title = 'Drink water',
        message = 'Time to drink some water',
        timeout = 2,
        # app_icon = "water-glass.ico"
    )
    global n3
    n3+=1
    log("water",n3)
    

    x=6
    z=12



while True:
    time.sleep(z)
    water()
    c+=c

    time.sleep(x)
    eye()
    a+=a

    time.sleep(15)
    exercise()
    b+=b
    
    continue

if a==b or c==a:
    x+=2
elif b==c:
    z+=2


# while True:
#     time.sleep(27)
#     exercise()
#     b+=b
#     break

# while True:
#     time.sleep(z)
#     water()
#     c+=c
#     break
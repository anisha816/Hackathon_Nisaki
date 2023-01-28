import mysql.connector as ms
#bangalore to manali/sikkim
m=ms.connect(host='localhost',user='root',passwd='mySQL',database='travel')

c=m.cursor()


budget=int(input("Enter a budget"))
nod=int(input("Enter number of days of stay"))
ppl=int(input("Enter number of people"))
place=input("Enter the destination")
op=input("Enter luxury or budget friendly")

c.execute('select name from hotels order by prices')
hl=c.fetchall()
c.execute('select prices from hotels order by prices')
hpp=c.fetchall()

if place=="manali" or place=="Manali":
    c.execute('select name from places order by tp')
    pl=c.fetchall()
elif place=="sikkim"or place=="Sikkim":
    c.execute('select name from placess order by tp')
    pl=c.fetchall()
if place=="manali"or place=="Manali":
    c.execute('select tp from places order by tp')
    tpp=c.fetchall()
elif place=="sikkim":
    c.execute('select tp from placess order by tp')
    tpp=c.fetchall()


if place=="manali" or place=="Manali":
        c.execute('select flightname from flights where destination="Manali" order by price')
        al=c.fetchall()
elif place=="sikkim" or place=="Sikkim":
        c.execute('select flightname from flights where destination="Sikkim" order by price')
        al=c.fetchall()

if place=="manali"or place=="Manali":
        c.execute('select price from flights where destination="Manali" order by price')
        fpp=c.fetchall()
elif place=="sikkim"or place=="Sikkim":
        c.execute('select price from flights where destination="Sikkim" order by price')
        fpp=c.fetchall()


if place=="manali"or place=="Manali":
        c.execute('select duration from places order by tp')
        time=c.fetchall()
elif place=="sikkim"or place=="Sikkim":
        c.execute('select duration from placess order by tp')
        time=c.fetchall()


def l():

    hours=nod*6 #maximum number of sightseeing hours per day is taken as 6
    t=0
    cost=0
    ap,hp,tp=7*budget/16,budget/2,budget/8  #assuming quarter of budget is used for air tickets, half for hotel and quarter for travel
    for i in range(len(fpp)-1,-1,-1):
        #flight charges per person
        f,=fpp[i]                       #tuple unpacking
        f_=f*ppl                        #total flight charges
        if f_<=ap:                      #checking if its in the budget
            flight=al[i]
            print(flight)               #if it is then it returns the flight name
            cost+=f_ 
            break
        else:
            continue
    if cost==0:
        print("Please find other means of travel")
    for i in range(len(hpp)-1,-1,-1):
        #room charge per room per night
        h,=hpp[i]
        h_=h*nod*int((ppl/2))
        if h_<=hp:
            print(hl[i])
            cost+=h_
            break
        else:
            continue

    for i in range(len(tpp)-1,-1,-1):
        #places to be visited in alloted time
        tll,=tpp[i]                
        while t<=hours:           #check if the places can be visited in time
            if tll<=ap:
                print(pl[i])
                cost+=tll
                tl,=time[i]
                t+=tl
                break
        else:
            continue
    
    
def b():

    hours=nod*6 #maximum number of sightseeing hours per day is taken as 6
    t=0
    cost=0
    ap,hp,tp=budget/4,budget/2,budget/4
    for i in range(0,len(fpp)):
        #flight charges per person
        f,=fpp[i]
        f_=f*ppl
        if f_<=ap:
            flight=al[i]
            print(flight)
            cost+=f_
            break
    if cost==0:
        print("Please find other means of travel")
    for i in range(0,len(fpp)):
        #room charge per room per night
        h,=hpp[i]
        h_=h*nod*int((ppl/2))
        if h_<=hp:
            print(hl[i])
            cost+=h_
            break        

    for i in range(0,len(fpp)):
        #places to be visited in alloted time
        tll,=tpp[i]
        while t<=hours:
            if tll<=ap:
                print(pl[i])
                cost+=tll
                tl,=time[i]
                t+=tl
                break
    
    
if op=='Luxury' or op=='luxury':
    l()

elif op=='Budget' or op=='budget':
    b()

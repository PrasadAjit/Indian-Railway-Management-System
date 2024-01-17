import pandas as pd
import time
import mysql.connector as sql
conn=sql.connect(host='Localhost',user='root',passwd='Prasad@2003',database='railway')
if conn.is_connected():
    print('')
    print('')
    print('***************------------>>>>>>>>>>>WELCOME TO,INDIAN RAILWAY MANAGEMENT SYSTEM <<<<<<<<<<<-----------****************')
    
def menu():
    print('')
    print('')
    print('1.Create Table Passenger')
    print('2.Add New Passenger Detail')
    print('3.Create Table Train Details')
    print('4.Add New in Train Details')
    print('5.Show All from Train Details')
    print('6.Show All from Passenger Table')
    print('7.Reservation of Tickets')
    print('8.Cancellation of Reservation')
    print('9.Exit from the System')
menu()


def create_passengers():
    c1=conn.cursor()
    c1.execute('Create table if not exists passengers(Pname varchar(20),age int,trainno varchar(20),destination varchar(20),amt int,status varchar(20))')
    print("Please Wait For Some Time..................")
    time.sleep(1)    
    print('Table passenger is created')

def add_passengers():
    c1=conn.cursor()
    L=[]
    Pname=input("Enter Name")
    L.append(Pname)
    age=int(input("Enter Age"))
    L.append(age)
    trainno=input("Enter the Train Number")
    L.append(trainno)
    destination=input("Enter the Destination")
    L.append(destination)
    amt=input("Enter the Amount")
    L.append(amt)
    status=input("Enter Status")
    L.append(status)
    pas=(Pname,age,trainno,destination,amt,status)
    sql="insert into passengers(Pname,age,trainno,destination,amt,status)values(%s,%s,%s,%s,%s,%s)"
    c1.execute(sql,pas)
    conn.commit()
    print("Record of Passenger Inserted")
    



def create_traindetail():
    c1=conn.cursor()
    c1.execute("create table if not exists trainsdetails(tname varchar(20),tnum int,source varchar(20),destination varchar(20),fare varchar(20),ac1 int,ac2 int,ac3 int)")
    print("Please Wait For Some Time..................")
    time.sleep(1)     
    print("Table Train Details Created")

def add_traindetail():
    c1=conn.cursor()
    tname=input("Enter Train Name")
    
    tnum=input("Enter the Train Number")
    
    source=input("Enter the Source")
    
    destination=input("Enter the Destination")
    
    fare=input("Enter the Fare")
    
    ac1=input("Enter Number of Seats for Ac1")
    
    ac2=input("Enter Number of Seats for Ac2")
    
    ac3=input("Enter Number of Seats for Ac3")
    f=(tname,tnum,source,destination,fare,ac1,ac2,ac3)
    sql="insert into traindetails(tname,tnum,source,destination,fare,ac1,ac2,ac3)values(%s,%s,%s,%s,%s,%s,%s,%s)"
    c1.execute(sql,f)
    conn.commit()
    print("Record Inserted in Trains Details")


def showtraindetails():
    print("***************************************************")
    sql='select * from traindetails'
    c1=conn.cursor()
    c1.execute(sql)
    d=c1.fetchall()
    for i in d:
        print("tname:",i[0])
        print("tnum:",i[1])
        print("source:",i[2])
        print("destination:",i[3])
        print("fare:",i[4])
        print("ac1:",i[5])
        print("ac2:",i[6])
        print("ac3:",i[7])
        print("***************************************************")



def showpassengers():
    print("***************************************************")
    sql='select * from passengers'
    c1=conn.cursor()
    c1.execute(sql)
    d=c1.fetchall()
    for i in d:
        print("Pname:",i[0])
        print("age:",i[1])
        print("trainno:",i[2])
        print("destination:",i[3])
        print("amt:",i[4])
        print("status:",i[5])
        print("***************************************************")



def ticketreservation():
    print("we have the following seat types for you:--")
    print()
    print("Tname is 1 for Goa express from New delhi:--")
    print()
    print("1.FIRST CLASS AC RS 6000 PER PERSON ")
    print("2.SECOND CLASS AC RS 5000 PER PERSON ")
    print("3.THIRD CLASS AC RS 4000 PER PERSON ")
    print("4.FOR SLEEPER RS 7000 PER PERSON ")
    print()
    time.sleep(2)
    print("Tname is 2 for Jmmu Express from new delhi")
    print()
    print("1.FIRST CLASS AC RS 10000 PER PERSON ")
    print("2.second CLASS AC RS 8000 PER PERSON ")
    print("3.third CLASS AC RS 6000 PER PERSON ")
    print("4.for sleeper AC RS 11000 PER PERSON ")
    print()
    time.sleep(2)
    print("Tname is 3 for Miraj Express from Londa Junction")
    print()
    print("1.FIRST CLASS AC RS 500 PER PERSON ")
    print("2.second CLASS AC RS 450 PER PERSON ")
    print("3.third CLASS AC RS 400 PER PERSON ")
    print("4.for sleeper AC RS 420 PER PERSON ")
    print()

    tname=(input("Enter Your Choice of Train Please->>>"))
    print(tname)
    if(tname==1):
        print("You Choicen First Train")
    x=int(input("Enter Your Choice of Ticket Please->>"))
    n=int(input("How Many Tickets You Need->>"))

    if(x==1):
        print("YOU HAVE CHOICEN FIRST CLASS AC TICKET")
        s=6000*n
    elif(x==2):
        print("YOU HAVE CHOICEN second CLASS AC TICKET")
        s=5000*n
    elif(x==3):
        print("YOU HAVE CHOICEN THIRD CLASS AC TICKET")
        s=4000*n
    elif(x==4):
        print("YOU HAVE CHOICEN SLEEPER  TICKET")
        s=7000*n
    else:
        print("INVALID OPTION")
        print("please choose a train")
    print("your total ticket price is =",s,"\n")
    if(tname==2):
        print("you choicen first train")
    if(x==1):
        print("YOU HAVE CHOICEN FIRST CLASS AC TICKET")
        s=10000*n
    elif(x==2):
        print("YOU HAVE CHOICEN second CLASS AC TICKET")
        s=8000*n
    elif(x==3):
        print("YOU HAVE CHOICEN third CLASS AC TICKET")
        s=6000*n
    elif(x==4):
        print("YOU HAVE CHOICEN sleeper TICKET")
        s=11000*n
    else:
        print("Invalid option")
        print("Please Choice a Train")
        
    print("Your Total Ticket Price is =",s,"\n")
    time.sleep(2)
    print("Your Ticket Is Reserved Succefully ")
    print("Thank You For Visiting")
    
def tck_cancellation():
    print('Please Wait For Some Time We Are Cancelling Your Ticket')
    time.sleep(2)
    print("Your Ticket Is Cancelled")
    
def hi():
    
    opt=''
    opt=int(input("Enter Your Choice:"))
    if opt==1:
        create_passengers()
        time.sleep(3)
        menu()
        hi()        
    elif opt==2:
        add_passengers()
        menu()
        hi()
    elif opt==3:
        create_traindetail()
        time.sleep(3)
        menu()
        hi()
    elif opt==4:
        add_traindetail()
        menu()
        hi()
    elif opt==5:
        print("PLEASE WAIT FOR SOME TIME ,WE ARE PETCHING TRAIN DETAILS !!!!")
        time.sleep(3)
        showtraindetails()
        menu()
        hi()
    elif opt==6:
        print("PLEASE WAIT FOR SOME TIME ,WE ARE PETCHING PASSENGERS DETAILS !!!!")
        time.sleep(3)
        showpassengers()
        menu()
        hi()
    elif opt==7:
        ticketreservation()
        menu()
        hi()
    elif opt==8:
        tck_cancellation()
        time.sleep(2)
        menu()
        hi()        
    elif opt==9:
        exit()
    else:
        print("Invalid Option")
        menu()
        hi()
    
hi()
time.sleep(5)
        
    
    
    
    
    
    
    
    
    

import mysql.connector as s
host=input("Enter host for mysql connection=   ")
user=input("Enter user for mysql connection=   ")
passwd=input("Enter password of your mysql=  ")
m=s.connect(host=host,database="khata_register",user=user,passwd=passwd)
if m.is_connected()==True:
    print("you are successfully connected to mysql")
else:
    print("Error in connecting to mysql database") 

print("\n")






def alldata():                #all data
    cursor=m.cursor()
    cursor.execute("select * from k")
    print(cursor.fetchall())



def passwd():                 #make password option......2......
    global passwd1
    passwd1=input("Enter new password :")
    passwd2=input("Confirm password:")
    if passwd1==passwd2:
        pass
    else:
        print("try again")
        passwd()
    print("you successfully created your password")

def seedata():                 #see data option......3.......
        print("\n")
        print("choose what you want to see......")
        print("""1.  Transactions left
2.  Transactions completed
3.  More than or equal .... money is left
4.  Last date is more than...
5.  last date is less than...
6.  Last date is...
7.  Sepecific person's data
8.  Transactions done on specified date
9.  Want to see whole data""")



#STARTING INTRO
print("ARMY PUBLIC SCHOOL \nNEW CANTT ALLAHABAD")
print("Computer Science project")
print("\n")
print("............................................................................................................................")
print("CREATER'S INTRO ")
print("NAME:Ankita")
print("class:XII\nSECTION:E")
print("Roll no.:5")
print("TOPIC:CREDIT MANAGEMENT")
print(".............................................................................................................................")
print("\n")
print("..............................................**KHATA REGISTER**.............................................................")
print("WELCOME TO KHATA REGISTER")
     




def functions():              #MAIN PROGRAM DEFINATION 
    print("\n")
    print("use following codes to proceed...")
    print("""1. Know about KHATA REGISTER
2. delete data
3. want to seek data
4. Do amendment in data
5. Add new person
6. Exit""")
    choice=int(input("Please enter the code number to proceed :    "))
   

    if choice==1:          #ABOUT KHATA REGISTER
        print("""Khata Register is here to make all your transaction records digital.It is easy to feach,
seek and store your daily transaction records though khata register.this is more safe
and secure from any manully created register.It can be used by any business man or for
household transaction related records""")
        functions()
        

    elif choice==2:        #DELETE DATA
        a=input("Enter column name :")
        b=input("Enter conditon(like>,<,=): ")
        c=input("Enter conditonal value: ")
        b="delete from k where {d}{e}'{f}'".format(d=a,e=b,f=c)
        cursor=m.cursor()
        cursor.execute(b)
        m.commit() 
        functions()
    
    
    elif choice==3:        #SEEK DATA
        cursor=m.cursor()
        seedata()
        kindofdata=int(input("ENTER code no. given above of your choice:  "))

        if kindofdata==1:      #transaction left
            print("Data of Customers whose money is left to get back...")
            cursor.execute("select * from k where status ='%s'"%("unpaid",))
            data=cursor.fetchall()
            for row in data:
                print(row)

        elif kindofdata==2:    #transaction completed
            print("Data of customers whose money is balanced")
            cursor.execute("select * from k where status ='%s'"%("paid",))
            data=cursor.fetchall()
            for row in data:
                print(row)
                
        elif kindofdata==3:    #More than.... money is left
            b=int(input("Enter money for more than which the customer left you want:  "))
            cursor.execute("select * from k where youllget >='%s'"%(b,))
            data=cursor.fetchall()
            for row in data:
                print(row)
        elif kindofdata==4:     #Last date is more than...
            b=input("Enter you want last date more than or equal(in the format YYYY-MM-DD) :  ")
            cursor.execute("select * from k where enddate >='%s'"%(b,))
            data=cursor.fetchall()
            for row in data:
                print(row)
                    
                 
        elif kindofdata==5:     # last date is less than...
            b=input("Enter you want last date less than (in the format YYYY-MM-DD) : ")
            cursor.execute("select * from k where enddate <='%s'"%(b,))
            data=cursor.fetchall()
            for row in data:
                print(row)
            
        elif kindofdata==6:     #Last date is...
            b=input("Enter you want last date is(in the format YYYY-MM-DD) : ")
            cursor.execute("select * from k where enddate ='%s'"%(b,))
            data=cursor.fetchall()
            for row in data:
                print(row)
            
        elif kindofdata==7:     # Sepecific person's data
            b=input("Enter name of the person: ")
            cursor.execute("select * from k where customer_name ='%s'"%(b,))
            data=cursor.fetchall()
            for row in data:
                print(row)
        elif kindofdata==8:     #Transactions done on specified date
            b=input("Enter date(in the format YYYY-MM-DD): ")
            cursor.execute("select * from k where date ='%s'"%(b,))
            data=cursor.fetchall()
            for row in data:
                print(row)

        elif kindofdata==9:     #Want to see whole data""")
            print("\n ")
            print("""The given data is of format
(CUSTOMER NAME , DATE OF TRANSACTION , CONTACT NO. OF CUSTOMER , YOU GAVE , YOU GOT , YOU'LL GET , LAST DATE FOR CUSTOMER , STATUS) """)
            print("\n") 
            alldata()
        functions()
    












    elif choice==4:        # AMENDMENT IN DATA
        a=input("Enter columun name to update: ")
        x=input("Enter old value: ")
        y=input("Enter new value: ")
        b="update k set {d}='{e}' where {d}='{f}'".format(d=a,e=y,f=x)
        cursor=m.cursor()
        cursor.execute(b)
        m.commit() 
        functions()
    
    elif choice==5:        #ADD NEW CUSTOMER
        name=input("Enter customer name: ")
        date=input("Enter date: ")
        conno=int(input("Enter contact no. : "))
        gave=int(input("Enter you gave : "))
        got=int(input("Enter you got: "))
        get=int(input("Enter you'll get: "))
        endate=input("Enter end date: ")
        status=input("Enter status: ")
        b="insert into k(customer_name,date,contactno,yougave,yougot,youllget,enddate,status) values ('{}','{}',{},{},{},{},'{}','{}')".format(name,date,conno,gave,got,get,endate,status)      
        cursor=m.cursor()
        cursor.execute(b)
        m.commit()
        functions()    
    elif choice==6:        # EXIT
        print("Press>>> 'Alt' plus 'F4'")

functions()
m.close()    


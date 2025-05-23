# Importing modules
from dotenv import load_dotenv
import os


load_dotenv()
import mysql.connector
import hashlib
import matplotlib.pyplot as plt

# Connecting to MYSQL
Con_obj = mysql.connector.connect(host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"), autocommit = True)

# Creating cursor object
cursor = Con_obj.cursor()

Key = ''

# Login page loop
while True :
    
    flag = 0                                                                
    print("\nLogin Page")                                   
    print("--------------------------------------------------------------------------------------------------------------")
    
    cursor.execute("Use Budget_Manager")
    
    cursor.execute("Select * from User_Details")
    
    data = cursor.fetchall()
    
    if data == [] :
        User = input("\nUsername: ")
        Password = input("Password: ")

        # Creating encrypted key
        x = bytes(Password, 'utf-8')    
        str = hashlib.sha256(x)
        KeyID = str.hexdigest()
        
        t = (User , Password , KeyID)
        sql = "Insert into User_Details values(%s,%s,%s)"
        
        cursor.execute(sql,t)

    elif flag == 1 :
        break

    else :
        
        print("\n1. Login\n2. Create new user")
        
        ch = int(input("-> "))
        if flag == 1 :
            break

        # Logging in
        elif ch == 1 :              
            
            flag = 0
            User = input("\n    Username - ")
            Password = input("    Password - ")
            
            cursor.execute("Select * from User_Details")
            data = cursor.fetchall()
            
            for i in data :
                if i[0] == User and i[1] == Password :
                    Key = i[2]
                    flag = 1
                    break
                
            else :
                if flag == 0 :
                    print("\nInvalid User or Password")
                    continue
                elif flag == 1 :
                    break
            break

        # Creating an account
        elif ch == 2:               
            
            User = input("\n    Username - ")
            Password = input("    Password - ")
            x = bytes(Password, "utf-8")
            
            str = hashlib.sha256(x)
            KeyID = str.hexdigest()
        
            t = (User , Password , KeyID)
            sql = "Insert into User_Details values(%s,%s,%s)"
        
            cursor.execute(sql,t)
                    

        else :
            print("\nInvalid input")

# Dashboard loop

while True :
    
    print("-------------------------------------------------------------------------------------------------------------")
    print("\nMenu")
    print("1. Income\n2. Expenses\n3. Investments\n4. Statistics\n5. Exit")
    
    ch = int(input("    Choice --> "))

    # Working with Income
    if ch == 1 :
        
        print("\t1. Display Incomes\n\t2. Input income stream\n\t3. Delete an income (Use M_ for monthly income or Y_ for yearly income)")
        choice = int(input("\tEnter choice--> "))

        # Displaying Incomes
        if choice == 1 :
            cursor.execute("Select Source, Value from Income where KeyID = %s",(Key,))
            data = cursor.fetchall()
            for i in data :
                print("\n\t\tSource:", i[0],"\n\t\tIncome:",i[1])

        # Taking Incomes
        elif choice == 2 :

            duration = int(input("\t\t\t1. Yearly\n\t\t\t2. Monthly\n\t\t\t3. One-Time\n\t\t\t\t--->"))
            
            if duration == 1 :
                
                source = input("\t\t\t\tEnter source - ")
                values = int(input("\t\t\t\tEnter value - "))
                source1 = "Y_" + source
                T1 = (source1 , values , Key)
                sql = "insert into Income values(%s,%s,%s)"
            
                cursor.execute(sql,T1)
                
            elif duration == 2 :
                source = input("\t\t\t\tEnter source - ")
                values = int(input("\t\t\t\tEnter value - "))
                source2 = "M_" + source
                T1 = (source2 , values , Key)
                sql = "insert into Income values(%s,%s,%s)"
            
                cursor.execute(sql,T1)

            elif duration == 3 :
                source = input("\t\t\t\tEnter source - ")
                values = int(input("\t\t\t\tEnter value - "))
                T1 = (source , values , Key)
                sql = "insert into Income values(%s,%s,%s)"
            
                cursor.execute(sql,T1)
                
            else :
                print("Invalid duration")

        # Deleting an Income
        elif choice == 3 :
            
            Del_source = input("\t\tEnter the source of income you would like to delete - ")
            cursor.execute("Delete from Income where Source = %s",(Del_source,))
            
        print("--------------------------------------------------------------------------------------------------------------")

    # Working with Expenses
    elif ch == 2 :                   
        

        print("\t1. Fixed Expenses\n\t2. Variable Expenses")
        choice = int(input("\tEnter choice --> "))

        # Taking Subscriptons
        if choice == 1 :    
            
            print("\t\t1. Display subscriptions\n\t\t2. Input a subscription\n\t\t3. Delete a subscription")
            C = int(input("\t\tEnter choice --> "))

            # Displaying fixed expenses
            if C == 1 :
                cursor.execute("Select Name, Price from Subscriptions where KeyID = %s",(Key,))
                data = cursor.fetchall()
                for i in data :
                     print("\n\t\t\tSubscription:", i[0],"\n\t\t\tExpense:",i[1])

            # Taking a subscription
            elif C == 2 :
                Name = input("\t\t\tEnter source - ")
                Price = int(input("\t\t\tEnter value - "))
            
                T2 = (Name , Price , Key)
                sql = "insert into Subscriptions values(%s,%s,%s)"
            
                cursor.execute(sql,T2)

            # Deleting an expense
            elif C == 3 :
                Del_source = input("\t\t\tEnter the subscription name you would like to delete - ")
                cursor.execute("Delete from Subscriptions where Name = %s",(Del_source,))

        # Taking variable expenses
        elif choice == 2 :
            print("\t\t1. Display Expenses\n\t\t2. Input an Expense\n\t\t3. Delete an Expense")
            C = int(input("\t\tEnter choice --> "))

            # Displaying expenses
            if C == 1 :
                cursor.execute("Select Name, Price from Variable_Expense where KeyID = %s",(Key,))
                data = cursor.fetchall()
                for i in data :
                    print("\n\t\t\tName:",i[0],"\n\t\t\tPrice:",i[1])

            # Taking an expense  
            elif C == 2 :
                Name = input("\t\t\tEnter source - ")
                Price = int(input("\t\t\tEnter value - "))
            
                T3 = (Name , Price , Key)
                sql = "insert into Variable_Expense values(%s,%s,%s)"
            
                cursor.execute(sql,T3)

            # Deleting an expense 
            elif C == 3 :
                Del_source = input("\t\t\tEnter the name of expense you would like to delete - ")
                cursor.execute("Delete from Variable_Expense where Name = %s",(Del_source,))
            
    
        print("--------------------------------------------------------------------------------------------------------------")

    # Working with Investments
    elif ch == 3 :                      
        
        print("\t1. Show portfolio\n\t2. Add investment\n\t3. Delete investment\n\t4. Returns Calculator")
        ch = int(input("\tEnter choice --> "))

        # Displaying investments
        if ch == 1 :
            
            cursor.execute("Select Investment, Invested_amount from Investments where KeyID = %s",(Key,))
            data = cursor.fetchall()
            for i in data :
                print("\n\t\tInvestment:",i[0],"\n\t\tInvested Amount:",i[1])

        # Adding a new investments      
        elif ch == 2 :
            
            Investment = input("\t\tEnter name of the investment - ")
            Price = int(input("\t\tEnter invested amount - "))
            
            T4 = (Investment , Price , Key)
            sql = "insert into Investments values(%s,%s,%s)"
            
            cursor.execute(sql,T4)

        # Deleting an investment
        elif ch == 3 :
            
            delete = input("\t\tEnter the investment name you want to delete -- ")
            cursor.execute("\t\tDelete from Investments where Investment = %s",(delete,))

        # Return calculator
        elif ch == 4 :
            
            Investment = input("\t\tEnter the Investment name -- ")
            Return_percentage = int(input("\t\tEnter return percentage -- "))
            
            cursor.execute("Select Investment, Invested_amount from Investments where KeyID = %s and Investment = %s",(Key,Investment))
            data = cursor.fetchall()
            
            for i in data :
                Return = i[1] + i[1] * ( Return_percentage/100 )
                print("\n\t\t\t -->",Return)
        print("--------------------------------------------------------------------------------------------------------------")

    # Statistics
    elif ch == 4 :
        
        print("\t\t1. Income\n\t\t2. Expense\n\t\t3. Invesments\n\t\t4. Savings\n\t\t5. Exit")
        Stats = int(input("\t\t\tChoice --> "))

        # Displaying Income statistics
        if Stats == 1 :
            Source = []
            Income = []
            
            print("\t\t\t\tEnter the status duration:\n\t\t\t\t1. Yearly\n\t\t\t\t2. Monthly")
            Duration = int(input("\t\t\t\t\tChoice --> "))

            D_Period = int(input("\t\t\t\t\t\tEnter the duration period --> "))
            
            if Duration == 1 :
                
                cursor.execute("Select Source, Value from Income where KeyID = %s",(Key,))
                data2 = cursor.fetchall()
                
                for i in data2 :

                    if i[0][0:2] == "Y_" :
                        Source.append(i[0])
                        Income.append(i[1] * D_Period)

                    elif i[0][0:2] == "M_" :
                        
                        Source.append(i[0])
                        Income.append((i[1]*12) * D_Period)

                    else :

                        Source.append(i[0])
                        Income.append(i[1])

            elif Duration == 2 :
                
                cursor.execute("Select Source, Value from Income where KeyID = %s",(Key,))
                data2 = cursor.fetchall()
                for i in data2 :

                    if i[0][0:2] == "Y_" :
                        Source.append(i[0])
                        Income.append((i[1]/12) * D_Period)

                    elif i[0][0:2] == "M_" :
                        
                        Source.append(i[0])
                        Income.append(i[1] * D_Period)

                    else :

                        Source.append(i[0])
                        Income.append(i[1])

        
            plt.style.use("ggplot")
            plt.title("Incomes")
            plt.pie(x = Income, labels = Source, autopct = "%.2f%%", shadow = True)
            plt.show()

        # Displaying Expense statistics   
        elif Stats == 2 :

            Source = []
            Expense = []

            print("\t\t\t\tEnter the status duration:\n\t\t\t\t1. Yearly\n\t\t\t\t2. Monthly")
            Duration = int(input("\t\t\t\t\tChoice --> "))

            D_Period = int(input("\t\t\t\t\t\tEnter the duration period --> "))

            if Duration == 1 :
                cursor.execute("Select Name, Price from Subscriptions where KeyID = %s",(Key,))
                data = cursor.fetchall()
                for i in data :
                    Source.append(i[0])
                    Expense.append((i[1]*12)* D_Period)
                      
                    
                cursor.execute("Select Name, Price from Variable_Expense where KeyID = %s",(Key,))
                data2 = cursor.fetchall()
                for i in data2 :
                    Source.append(i[0])
                    Expense.append(i[1])

            elif Duration == 2 :
                cursor.execute("Select Name, Price from Subscriptions where KeyID = %s",(Key,))
                data = cursor.fetchall()
                for i in data :
                    Source.append(i[0])
                    Expense.append(i[1]* D_Period)
                      
                    
                cursor.execute("Select Name, Price from Variable_Expense where KeyID = %s",(Key,))
                data2 = cursor.fetchall()
                for i in data2 :
                    Source.append(i[0])
                    Expense.append(i[1])

            plt.style.use("ggplot")
            plt.title("Expenses")
            plt.pie(x = Expense, labels = Source, autopct = "%.2f%%", shadow = True)
            plt.show()


        # Displaying investment statistics
        elif Stats == 3 :
            
            Investment = []
            Investment_amount = []
            
            cursor.execute("Select Investment, Invested_amount from Investments where KeyID = %s",(Key,))
            data = cursor.fetchall()
            for i in data :
                Investment.append(i[0])
                Investment_amount.append(i[1])
                
            plt.style.use("ggplot")
            plt.title("Investments")
            plt.pie(x = Investment_amount, labels = Investment, autopct = "%.2f%%", shadow = True)
            plt.show()

        # Calculating and Displaying savings 
        elif Stats == 4 :

            Name = []
            Value = []
            Income = []
            Expense = []
            Investment_amount = []
            
            print("\t\t\t\tEnter the status duration:\n\t\t\t\t1. Yearly\n\t\t\t\t2. Monthly")
            Duration = int(input("\t\t\t\t\tChoice --> "))

            D_Period = int(input("\t\t\t\t\t\tEnter the duration period --> "))
            
            if Duration == 1 :
                
                cursor.execute("Select Source, Value from Income where KeyID = %s",(Key,))
                data = cursor.fetchall()
                for i in data :

                    if i[0][0:2] == "Y_" :
                        
                        Income.append(i[1] * D_Period)

                    elif i[0][0:2] == "M_" :
                
                        Income.append((i[1]*12) * D_Period)

                cursor.execute("Select Name, Price from Subscriptions where KeyID = %s",(Key,))
                data = cursor.fetchall()
                for i in data :
                    
                    Expense.append((i[1]*12)* D_Period)
                      
                    
                cursor.execute("Select Name, Price from Variable_Expense where KeyID = %s",(Key,))
                data2 = cursor.fetchall()
                for i in data2 :
                    
                    Expense.append(i[1])

            elif Duration == 2 :
                
                cursor.execute("Select Source, Value from Income where KeyID = %s",(Key,))
                data = cursor.fetchall()
                for i in data :

                    if i[0][0:2] == "Y_" :
                        
                        Income.append((i[1]/12) * D_Period)

                    elif i[0][0:2] == "M_" :

                        Income.append(i[1] * D_Period)

                cursor.execute("Select Name, Price from Subscriptions where KeyID = %s",(Key,))
                data = cursor.fetchall()
                for i in data :
                    
                    Expense.append(i[1]* D_Period)
                      
                    
                cursor.execute("Select Name, Price from Variable_Expense where KeyID = %s",(Key,))
                data2 = cursor.fetchall()
                for i in data2 :
                    
                    Expense.append(i[1])

            
            cursor.execute("Select Investment, Invested_amount from Investments where KeyID = %s",(Key,))
            data = cursor.fetchall()
            for i in data :
                Investment_amount.append(i[1])

            Name.append("Incomes")
            Value.append(sum(Income))

            Name.append("Expenses")
            Value.append(sum(Expense))

            Name.append("Investments")
            Value.append(sum(Investment_amount))

            Name.append("Savings")
            Value.append(Value[0] + Value[2] - Value[1] )

            explode = (0,0,0,0.09)

            plt.style.use("ggplot")
            plt.title("Savings")
            plt.pie(x = Value, labels = Name, explode = explode, autopct = "%.2f%%", shadow = True, startangle = 60)
            plt.show()            
            print("--------------------------------------------------------------------------------------------------------------")
        
    elif ch == 5 :
        print("\nThank you for using this application!")
        print("--------------------------------------------------------------------------------------------------------------")        
        break

    else :
        print("Invalid input! \nRestart again!")
        print("\n--------------------------------------------------------------------------------------------------------------")
            

Con_obj.close()


            

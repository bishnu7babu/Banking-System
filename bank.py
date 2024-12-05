import csv as c
import random

class Bank_Details:

    def __init__(self,csv_ACCOUNT_NUMBER_NAME,csv_ACCOUNT_NUMBER_BALANCE,csv_ACCOUNT_NUMBER_PASS,csv_ACCOUNT_NUMBER_TPASS,csv_ACCOUNT_NUMBER_PHONE,csv_file_path,fields,row_index,column_index):
        self.csv_file = csv_file_path
        self.fields = fields
        self.csv_ACCOUNT_NUMBER_NAME = csv_ACCOUNT_NUMBER_NAME
        self.csv_ACCOUNT_NUMBER_BALANCE = csv_ACCOUNT_NUMBER_BALANCE
        self.csv_ACCOUNT_NUMBER_PASS = csv_ACCOUNT_NUMBER_PASS
        self.csv_ACCOUNT_NUMBER_TPASS = csv_ACCOUNT_NUMBER_TPASS
        self.csv_ACCOUNT_NUMBER_PHONE = csv_ACCOUNT_NUMBER_PHONE
        self.row_index = row_index
        self.column_index = column_index
        self.list_csv_data = []

    def create_account(self):
         self.C_name = input("Enter Your Name: ")
         self.C_Phone_Number = int(input("Enter Your Phone Number: "))
         self.C_New_Account_Number = self.create_New_Account_Number()
         self.C_Acc_Pass = int(input("Setup your 4 digit Account Password: "))
         self.C_Tran_Pass = int(input("Setup Your 4 digit Transaction Password: "))
         self.csv_writer_data()

    
    def find_CSV_INDEX(self): # It find the index number of csv file cell.
         with open(self.csv_file,'r') as file_index:
             csv_reader = c.reader(file_index)
             self.list_csv_data = list(csv_reader)
             for self.row_index,row in enumerate(self.list_csv_data):
                 if row:
                    for self.column_index, cell in enumerate(row):
                        try:
                            account = int(cell)
                            if account == self.account_Number:
                                # print(self.row_index,self.column_index)
                                return

                        except ValueError:
                            pass
    
    def change_Balance_Cell_Csv_Value(self):
         if self.row_index < len(self.list_csv_data) and self.column_index < len(self.list_csv_data[self.row_index]):
              new_Updated_Balance = int(input("Enter the Balance: "))
              self.column_index += 5
            #   print(self.column_index)
              self.list_csv_data[self.row_index][self.column_index] = new_Updated_Balance

              with open(self.csv_file,'w') as file:
                   file_writer = c.writer(file)
                   file_writer.writerows(self.list_csv_data)

    def change_Pass_Cell_Csv_Value(self):
         new_pass = int(input("Enter Your New Password: "))
         if self.row_index < len(self.list_csv_data) and self.column_index < len(self.list_csv_data[self.row_index]):
              self.column_index += 3
            #   print(self.column_index)
              self.list_csv_data[self.row_index][self.column_index] = new_pass

              with open(self.csv_file,'w') as file:
                   file_writer = c.writer(file)
                   file_writer.writerows(self.list_csv_data)

    def change_Tpass_Cell_Csv_Value(self):
         new_tpass = int(input("Enter Your New Transaction Password: "))
         if self.row_index < len(self.list_csv_data) and self.column_index < len(self.list_csv_data[self.row_index]):
              self.column_index += 4
            #   print(self.column_index)
              self.list_csv_data[self.row_index][self.column_index] = new_tpass

              with open(self.csv_file,'w') as file:
                   file_writer = c.writer(file)
                   file_writer.writerows(self.list_csv_data)

    def create_New_Account_Number(self):
         while True:
              self.new_account_number = int(''.join([str(random.randint(0,9)) for i in range(16)]))
              print(self.new_account_number)

              if self.new_account_number in self.csv_ACCOUNT_NUMBER_NAME:
                   continue
              else:
                   return self.new_account_number
              
    def compare_CSV_Column(self): # It Give You CSV file Value To a Dict file.
        #  self.csv_ACCOUNT_NUMBER_NAME = {}
        #  self.csv_ACCOUNT_NUMBER_BALANCE = {}
        #  self.csv_ACCOUNT_NUMBER_PASS = {}
        #  self.csv_ACCOUNT_NUMBER_TPASS = {}
        #  self.csv_ACCOUNT_NUMBER_PHONE = {}

         with open(self.csv_file,"r") as csv_file:
              csv_reader = c.DictReader(csv_file)
              for row in csv_reader:
                   account_number = int(row['account_Number'])
                #    print(int(self.csv_ACCOUNT_NUMBER_NAME))
                #    print(account_number)
                   self.csv_ACCOUNT_NUMBER_NAME[account_number] = ''.join(row['full_Name'])
                   self.csv_ACCOUNT_NUMBER_PASS[account_number] = int(''.join(row['account_Pass']))
                   self.csv_ACCOUNT_NUMBER_TPASS[account_number] = int(''.join(row['transaction_Pass']))
                   self.csv_ACCOUNT_NUMBER_BALANCE[account_number] = int(''.join(row['Balance']))
                   self.csv_ACCOUNT_NUMBER_PHONE[account_number] = int(''.join(row['Phone_Number']))
                   
            #   print(self.csv_ACCOUNT_NUMBER_NAME)
            #   print(self.csv_ACCOUNT_NUMBER_PASS)
            #   print(self.csv_ACCOUNT_NUMBER_TPASS)
            #   print(self.csv_ACCOUNT_NUMBER_BALANCE)
            #   print(self.csv_ACCOUNT_NUMBER_PHONE)
            
    def csv_writer_fields(self):
          with open(self.csv_file,"w",newline='') as csv_file:
               csv_writer = c.writer(csv_file)
               csv_writer.writerow(self.fields)
               return

    def csv_writer_data(self):
          with open(self.csv_file,'a',newline='') as csv_file:
               csv_writer = c.writer(csv_file)
               csv_writer.writerow([self.C_New_Account_Number,self.C_name,self.C_Phone_Number,self.C_Acc_Pass,self.C_Tran_Pass,0])
               print("Conguralation Your Account Is Created")
               print("Please Write Down Your Account Number on Paper.......")

    def manage_Account_Admin(self):
        print("------------------------------------------")
        print("Account Number: ",self.account_Number)
        print("Account Holder Name: ",self.csv_ACCOUNT_NUMBER_NAME[self.account_Number])
        print("Availabe Balance: ",self.csv_ACCOUNT_NUMBER_BALANCE[self.account_Number])
        print("------------------------------------------")

    def update_Csv_Balance(self): # This Will Change The Balance Of Csv File.
         with open(self.csv_file,'r') as file_index:
             csv_reader = c.reader(file_index)
             list_csv_data1 = list(csv_reader)
             for row_index1,row in enumerate(list_csv_data1):
                 if row:
                    for column_index1, cell in enumerate(row):
                        try:
                            account1 = int(cell)
                            if account1 == self.account_number2:
                                print(row_index1,column_index1)
                                # return
                                if row_index1 < len(list_csv_data1) and column_index1 < len(list_csv_data1[row_index1]):
                                    #   new_Updated_Balance = int(input("Enter the Balance: "))
                                    column_index1 += 5
                                    #   print(self.column_index)
                                    new_Updated_Balance = self.put_balance + self.csv_ACCOUNT_NUMBER_BALANCE[self.account_number2]
                                    print(new_Updated_Balance)
                                    list_csv_data1[row_index1][column_index1] = new_Updated_Balance

                                    with open(self.csv_file,'w') as file:
                                        file_writer = c.writer(file)
                                        file_writer.writerows(list_csv_data1)
                                        return

                        except ValueError:
                            pass

    def update_Csv_Balanace_2(self):                        
         with open(self.csv_file,'r') as file_index:
             csv_reader = c.reader(file_index)
             list_csv_data2 = list(csv_reader)
             for row_index2, row in enumerate(list_csv_data2):
                 if row:
                    for column_index2, cell in enumerate(row):
                        try:
                            account2 = int(cell)
                            if account2 == self.account_Number:
                                print(row_index2,column_index2)
                                # return
                                if row_index2 < len(list_csv_data2) and column_index2 < len(list_csv_data2[row_index2]):
                                    #   new_Updated_Balance = int(input("Enter the Balance: "))
                                    column_index2 += 5
                                    #   print(self.column_index)
                                    new_Updated_Balance2 =  self.csv_ACCOUNT_NUMBER_BALANCE[self.account_Number] - self.put_balance
                                    print(new_Updated_Balance2)
                                    list_csv_data2[row_index2][column_index2] = new_Updated_Balance2

                                    with open(self.csv_file,'w') as file:
                                        file_writer = c.writer(file)
                                        file_writer.writerows(list_csv_data2)
                                        return
                        except ValueError:
                            pass

    def manage_Transactions(self):
        self.put_balance = int(input("Enter the Balance: "))
        if self.put_balance <= self.csv_ACCOUNT_NUMBER_BALANCE[self.account_Number]:
            T_pass = int(input("Enter Your Transaction Pass: "))
            if T_pass == self.csv_ACCOUNT_NUMBER_TPASS[self.account_Number]:
                self.account_number2 = int(input("Enter 16 digits Account Number You want to Transfer: "))
                if self.account_number2 in self.csv_ACCOUNT_NUMBER_NAME:
                    self.update_Csv_Balance()
                    self.update_Csv_Balanace_2()
                    self.compare_CSV_Column()
                    print("Conguralation Your Transaction Is Sucessfull.")
                    print("Your Available balance =",self.csv_ACCOUNT_NUMBER_BALANCE[self.account_Number])
                    # print("Other Available balance =",self.balance[account_number2])
                else:
                    print("Invalid Account Number !!!")
                    for i in range(4,0,-1):
                         acc_Number2 = int(input(str(i)+". Enter 16 digits Account Number You want to Transfer: "))
                         if acc_Number2 in self.csv_ACCOUNT_NUMBER_NAME:
                              self.update_Csv_Balance()
                              self.update_Csv_Balanace_2()
                              self.compare_CSV_Column()
                              print("Conguralation Your Transaction Is Sucessfull.")
                              print("Your Available balance =",self.csv_ACCOUNT_NUMBER_BALANCE[self.account_Number])
                              break
            else:
                 print("Your Transaction Password is Wrong , Try again")
                 for i in range(4,0,-1):
                      nxt_T_Pass = int(input(str(i)+" Please Enter Your Password: "))
                      if nxt_T_Pass == self.csv_ACCOUNT_NUMBER_TPASS[self.account_Number]:
                            self.account_number2 = int(input("Enter 16 digits Account Number You want to Transfer: "))
                            if self.account_number2 in self.csv_ACCOUNT_NUMBER_NAME:
                                self.update_Csv_Balance()
                                self.update_Csv_Balanace_2()
                                self.compare_CSV_Column()
                                print("Conguralation Your Transaction Is Sucessfull.")
                                print("Your Available balance =",self.csv_ACCOUNT_NUMBER_BALANCE[self.account_Number])
                                # print("Other Available balance =",self.balance[account_number2])
                                break
        else:
            print("You Don't have enough Balance")       

    def balance_Inquary(self):
        print("Your Available balance = ",self.csv_ACCOUNT_NUMBER_BALANCE[self.account_Number])
        print("------------------------------------------")
        return self.inquary()

    def wrong_Password_Security(self):
        for i in range(4,0,-1):
            nxt_password = int(input("You Enter Wrong Password " + str(i) + " Times left: "))
            if nxt_password == self.password:
                return

    def check_Password(self):
        password = int(input("Enter your 4 digit Password: "))
        if password == self.password:
            self.check_Account_Number()
        else:
            self.wrong_Password_Security()

    def account_Security(self):
        print("Invalid Account Number !!!")
        for i in range(4,0,-1):
            self.account_Number = int(input(str(i)+" Please Enter Correct Account Number: "))  
            if self.account_Number in self.csv_ACCOUNT_NUMBER_NAME:
                for i in range(4,0,-1):
                    passwd = int(input("Enter your 4 Digits Password: "))
                    if passwd == self.csv_ACCOUNT_NUMBER_PASS[self.account_Number]:
                        print("------------------------------------------")
                        self.inquary()
                        break
                    break

    def check_Account_Number(self):
        if self.account_Number in self.csv_ACCOUNT_NUMBER_NAME:
            passw = int(input("Enter Your 4 Digits Passwords: "))
            if passw == self.csv_ACCOUNT_NUMBER_PASS[self.account_Number]:
                self.inquary()
            else:
                 print("Your Password Is Wrong!!!")
                 for i in range(4,0,-1):
                    ac_passwd = int(input(str(i)+". Enter Your Password: "))
                    if ac_passwd == self.csv_ACCOUNT_NUMBER_PASS[self.account_Number]:
                        self.inquary()
                        break    
        else:
            self.account_Security()

    def enter_Account_Number(self):
        self.account_Number = int(input("Please Enter Your 16 Digits Account Number: "))
        self.check_Account_Number()

    def update_Csv(self):
         print("------------------------------------------")
         print("Enter 1 For Update Your Balance")
         print("Enter 2 For Update Your Account Password")
         print("Enter 3 For Update Your Transactions Password")
         print("------------------------------------------")
         self.find_CSV_INDEX()
         update_inquary = int(input("Enter Your Quary: "))

         if update_inquary == 1:
              self.change_Balance_Cell_Csv_Value()

         elif update_inquary == 2:
              self.change_Pass_Cell_Csv_Value()

         elif update_inquary == 3:
              self.change_Tpass_Cell_Csv_Value()

         else:
              print("Invalid Operation")

    def inquary(self):
        print("------------------------------------------")
        print("Enter 1 For Balance Inquary")
        print("Enter 2 For Balance Transactions")
        print("Enter 3 For Account Details")
        print("Enter 4 For Update Your Account")
        print("------------------------------------------")
        inquary = int(input("User: "))
      
        if inquary == 1:
                self.balance_Inquary()
            
        elif inquary == 2:
                self.manage_Transactions()

        elif inquary == 3:
                self.manage_Account_Admin()

        elif inquary == 4:
             self.update_Csv()

        else:
             print("Invalide Inquary")

    def account_Log(self):
         print("Enter 1 For Create A Account")
         print("Enter 2 For Log in")
         Acc_Log = int(input("User: "))
         if Acc_Log == 1:
              self.create_account()
         
         elif Acc_Log == 2:
              self.enter_Account_Number()
         
         else:
              print("Invalid Operation")
         return Acc_Log
        
csv_ACCOUNT_NUMBER_NAME = {}
csv_ACCOUNT_NUMBER_BALANCE = {}
csv_ACCOUNT_NUMBER_PASS = {}
csv_ACCOUNT_NUMBER_TPASS = {}
csv_ACCOUNT_NUMBER_PHONE = {}

csv_file_path = "user_bank_details.csv"
fields = [
     "account_Number","full_Name",
     "account_Pass","transcation_Pass","Balance"
]

manage_Account_Admin_Password = 1234
# All_Account_Manage_Details = [account_Details,account_Balance,manage_Account_Admin_Password,account_Passwords,account_Transaction_Pass,csv_file_path,fields]
row_index = 0
column_index = 0
Bank = Bank_Details(csv_ACCOUNT_NUMBER_NAME,csv_ACCOUNT_NUMBER_BALANCE,csv_ACCOUNT_NUMBER_PASS,csv_ACCOUNT_NUMBER_TPASS,csv_ACCOUNT_NUMBER_PHONE,csv_file_path,fields,row_index,column_index)
Bank.compare_CSV_Column()
Acc_Log = Bank.account_Log()
if Acc_Log == 1:
     exit
else:
    Bank.find_CSV_INDEX()

# Bank.update_Balance()
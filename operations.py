# Importing
from dbconnections import *
from data_logs import *

# ===============================================[withdraw Class ]======================================================
class withdraw:
     def __init__(self, ID , PIN , b , NumberList, atmbc, userhist, userday, usertime):
        self.id = ID
        self.pin = PIN
        self.b = b
        self.NumberList = NumberList
        self.atmbc = atmbc  # atm balance
        self.userhist = userhist
        self.userday = userday
        self.usertime = usertime

     def gui_balance_check(self):

         check1st = date_logs(self.id, self.userhist, self.userday, self.usertime)
         first = check1st.first_operation_check()  # Check if its First Operation For User
         if first == 0:  # if user First Time Per Day
             st1 = 1
             value = self.NumberList[0] * 200 + self.NumberList[1] * 100 \
                     + self.NumberList[2] * 50 + self.NumberList[3] * 20 + self.NumberList[4] * 10

             self.b -= value  # suptract input cash from user
             insertbalance = DBOperation(self.id, self.pin)
             insertbalance.add_balance(self.b)  # add New Balance To user

             # ///////////////////////////////////////////////////////////////////////////////////
             # ///////////////////////////////////////////////////////////////////////////////////
             # //                 Insert Papers and Balance To ATM                            //
             AtmBalanceInsert = unATMFill(self.NumberList[0], self.NumberList[1],
                                        self.NumberList[2], self.NumberList[3], self.NumberList[4])
             AtmBalanceInsert.filling()
             # ///////////////////////////////////////////////////////////////////////////////////
             # ///////////////////////////////////////////////////////////////////////////////////

             # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
             # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

             opertaion = "withdraw - %s" % value  # Operation Row Content
             datalogs = date_logs(self.id, self.userhist, self.userday, self.usertime, opertaion, st1)
             datalogs.insert_operation(value, 0)  # Insert Values in Logs Table
             # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
             # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

         else:
             st1 = 0  # if Not First time Per Day
             value1 = self.NumberList[0] * 200 + self.NumberList[1] * 100 \
                     + self.NumberList[2] * 50 + self.NumberList[3] * 20 + self.NumberList[4] * 10


             self.b -= value1  # Suptract balance from user
             insertbalance = DBOperation(self.id, self.pin)
             insertbalance.add_balance(self.b)  # add New Balance To user

             # ///////////////////////////////////////////////////////////////////////////////////
             # ///////////////////////////////////////////////////////////////////////////////////
             # //                 Insert Papers and Balance To ATM                            //
             AtmBalanceInsert = unATMFill(self.NumberList[0], self.NumberList[1],
                                        self.NumberList[2], self.NumberList[3], self.NumberList[4])
             AtmBalanceInsert.filling()
             # ///////////////////////////////////////////////////////////////////////////////////
             # ///////////////////////////////////////////////////////////////////////////////////
             opertaion = "withdraw - %s" % value1  # Operation Content
             datalogs1 = date_logs(self.id, self.userhist, self.userday, self.usertime, opertaion, st1)
             totalwith1 = datalogs1.get_any_withdraw()  # Get Total Withdraw
             totaldep = datalogs1.get_any_totaldepposite()  # Get Total Deppsite
             inputingCash = value1 + totalwith1  # Total Withdraw Per Day
             datalogs1.insert_operation(inputingCash, totaldep)  # Insert Values in Logs

         return opertaion


# ===============================================[depposite Class ]=====================================================
class depposite:

    def __init__(self, ID, PIN, b, NumberList, atmbc,userhist, userday, usertime):
        self.id = ID
        self.pin = PIN
        self.b = b
        self.NumberList = NumberList
        self.atmbc = atmbc
        self.userhist = userhist
        self.userday = userday
        self.usertime = usertime


    def add_balance(self):

        # Calc Number of Papers
        numberofpapers = self.NumberList[0] + self.NumberList[1]\
                         + self.NumberList[2] + self.NumberList[3] + self.NumberList[4]

        if numberofpapers <= 30:
            # Value of Papers
            value = self.NumberList[0]*200 + self.NumberList[1]*100\
                    + self.NumberList[2]*50 + self.NumberList[3]*20 + self.NumberList[4]*10

            self.b += value  # + value to user
            InsertBalance = DBOperation(self.id, self.pin)
            InsertBalance.add_balance(self.b)  # Insert Value to User

            # ///////////////////////////////////////////////////////////////////////////////////
            # ///////////////////////////////////////////////////////////////////////////////////
            # //                 Insert Papers and Balance To ATM                            //
            AtmBalanceInsert = ATMFill(self.NumberList[0], self.NumberList[1],
                                       self.NumberList[2], self.NumberList[3], self.NumberList[4])
            AtmBalanceInsert.filling()
            # ///////////////////////////////////////////////////////////////////////////////////
            # ///////////////////////////////////////////////////////////////////////////////////

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            opertaion = "depposite + %s" % value  # Operation Row Content
            datalogs = date_logs(self.id, self.userhist, self.userday, self.usertime, opertaion)
            datalogs.insert_operation(0, value)  # insert values in logs
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            check = 1
        else:
            check = 0

        return check


# ===============================================[transfer Class ]=====================================================
class transfer:

    def __init__(self, ID, ID2, b, cash):
        self.id = ID  # user ID
        self.id2 = ID2  # user PIN
        self.b = b
        self.cash = cash

    def transfer_balance(self):
        if self.b >= self.cash:
            self.b -= self.cash
            InsertBalance = DBOperation(self.id)
            InsertBalance.add_balance(self.b)

            #Inster Balance To user 1
            get_user2_balance = DBOperation(self.id2)
            user2 = get_user2_balance.balance_check()

            user2 += self.cash
            # Insert Balance To user 2
            InsertBalance = DBOperation(self.id2)
            InsertBalance.add_balance(user2)

            check = 1
        else:
            check = 0
        return check


# ===============================================[Fill ATM ]=====================================================
class ATMFill:

    def __init__(self, x200, x100, x50, x20, x10):
        self.x200 = x200
        self.x100 = x100
        self.x50 = x50
        self.x20 = x20
        self.x10 = x10


    def filling(self):

        incash = DBOperation(1)
        g = incash.atm_full_check()  # Check Paper in ATM
        old200 = int(g[0][2]) + self.x200
        old100 = int(g[0][3]) + self.x100
        old50 = int(g[0][4]) + self.x50
        old20 = int(g[0][5]) + self.x20
        old10 = int(g[0][6]) + self.x10
        incash.atm_x200x100x50_update(old200, old100, old50, old20, old10)
        x = incash.atm_full_check()  # Check NewPaper in ATM
        new200 = int(x[0][2])
        new100 = int(x[0][3])
        new50 = int(x[0][4])
        new20 = int(x[0][5])
        new10 = int(x[0][6])
        sum_of_balance = 200*new200 + 100*new100 + 50*new50 + new20*20 + new10*10  # Get Value Of paper
        incash.atm_balance_update(sum_of_balance)  # insert Value

        return sum_of_balance
# ===============================================[unFill ATM ]=====================================================
class unATMFill:

    def __init__(self, x200, x100, x50, x20, x10):
        self.x200 = x200
        self.x100 = x100
        self.x50 = x50
        self.x20 = x20
        self.x10 = x10


    def filling(self):

        incash = DBOperation(1)
        g = incash.atm_full_check()  # Check Paper in ATM
        old200 = int(g[0][2]) - self.x200
        old100 = int(g[0][3]) - self.x100
        old50 = int(g[0][4]) - self.x50
        old20 = int(g[0][5]) - self.x20
        old10 = int(g[0][6]) - self.x10
        incash.atm_x200x100x50_update(old200, old100, old50, old20, old10)
        x = incash.atm_full_check()  # Check NewPaper in ATM
        new200 = int(x[0][2])
        new100 = int(x[0][3])
        new50 = int(x[0][4])
        new20 = int(x[0][5])
        new10 = int(x[0][6])
        sum_of_balance = 200*new200 + 100*new100 + 50*new50 + new20*20 + new10*10  # Get Value Of paper
        incash.atm_balance_update(sum_of_balance)  # insert Value

        return sum_of_balance

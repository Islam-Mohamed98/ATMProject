# Importing
from dbconnections import *
from data_logs import *


# ===============================================[UserCheck Class ]=====================================================
class UserCheck:

    def __init__(self, ID, userhist, userday, usertime):
        self.id = ID
        self.userhist = userhist
        self.userday = userday
        self.usertime = usertime

    def user_info_get(self):
        check1st = date_logs(self.id, self.userhist, self.userday, self.usertime)
        first = check1st.first_operation_check()  # Check if its First Operation For User
        if first == 0:
            st1 = 1
            totalwith = 0
            totaldep = 0
        else:
            st1 = 0
            checked = date_logs(self.id, self.userhist, self.userday, self.usertime, 0, st1)
            totalwith = checked.get_any_withdraw()  # Get Total Withdraw Last One
            totaldep = checked.get_any_totaldepposite()  # Get Total dep Last One

        result = [totalwith, totaldep, st1]
        return result


# ===============================================[withdraw Class ]======================================================
class WithDraw:

     def __init__(self, ID , PIN , b , NumberList, userhist, userday, usertime, st1, withdep):
        self.id = ID
        self.pin = PIN
        self.b = b
        self.NumberList = NumberList
        self.userhist = userhist
        self.userday = userday
        self.usertime = usertime
        self.value = self.NumberList[0] * 200 + self.NumberList[1] * 100 \
                + self.NumberList[2] * 50 + self.NumberList[3] * 20 + self.NumberList[4] * 10
        self.st1 = st1
        self.totalwith = withdep[0]
        self.totaldep = withdep[1]

     def gui_balance_check(self):

         insertbalance = DBOperation(self.id, self.pin)
         self.b -= self.value  # suptract input cash from user
         insertbalance.add_balance(self.b)  # add New Balance To user
         AtmBalanceInsert = UnATMFill(self.NumberList)
         AtmBalanceInsert.filling()
         opertaion = "withdraw - %s" % self.value  # Operation Row Content
         datalogs = date_logs(self.id, self.userhist, self.userday, self.usertime, opertaion, self.st1)
         datalogs.insert_operation(self.totalwith + self.value, self.totaldep, self.b)  # Insert Values in Logs Table

         return opertaion


# ===============================================[depposite Class ]=====================================================
class depposite:

    def __init__(self, ID, PIN, b, NumberList,userhist, userday, usertime, st1, withdep):
        self.id = ID
        self.pin = PIN
        self.b = b
        self.NumberList = NumberList
        self.userhist = userhist
        self.userday = userday
        self.usertime = usertime
        self.value = NumberList[0] * 200 + NumberList[1] * 100 \
                + NumberList[2] * 50 + NumberList[3] * 20 + NumberList[4] * 10
        self.numberofpapers = NumberList[0] + NumberList[1] \
                         + NumberList[2] + NumberList[3] + NumberList[4]
        self.st1 = st1
        self.totalwith = withdep[0]
        self.totaldep = withdep[1]

    def add_balance(self):

        if self.numberofpapers <= 30:
            self.b += self.value  # + value to user
            InsertBalance = DBOperation(self.id, self.pin)
            InsertBalance.add_balance(self.b)  # Insert Value to User
            AtmBalanceInsert = ATMFill(self.NumberList)
            AtmBalanceInsert.filling()
            opertaion = "depposite + %s" % self.value  # Operation Row Content
            datalogs = date_logs(self.id, self.userhist, self.userday, self.usertime, opertaion, self.st1)
            datalogs.insert_operation(self.totalwith, self.totaldep + self.value, self.b)  # Insert Values in Logs Table

            check = 1
        else:
            check = 0

        return check


# ===============================================[transfer Class ]=====================================================
class transfer:

    def __init__(self, ID, ID2, b, cash,userhist, userday, usertime, st1, withdep):
        self.id = ID  # user ID
        self.id2 = ID2  # user PIN
        self.b = b
        self.cash = cash
        self.userhist = userhist
        self.userday = userday
        self.usertime = usertime
        self.st1 = st1
        self.totalwith = withdep[0]
        self.totaldep = withdep[1]

    def transfer_balance(self):
        if self.b >= self.cash:
            self.b -= self.cash
            # insert balance to Trans maker
            opertaion = "Trans %s To ID + %s" % (self.cash, self.id2)  # Operation Row Content
            datalogs = date_logs(self.id, self.userhist, self.userday, self.usertime, opertaion, self.st1)
            datalogs.insert_operation(self.totalwith, self.totaldep, self.b)  # Insert Values in Logs Table
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # User 2
            get_user2_balance = DBOperation(self.id2)
            user2 = get_user2_balance.balance_check()
            user2 += self.cash
            # Insert Balance To user 2
            opertaion = "You Got %s From ID %s" % (self.cash, self.id)  # Operation Row Content
            check1st = date_logs(self.id2, self.userhist, self.userday, self.usertime)
            first = check1st.first_operation_check()  # Check if its First Operation For User
            if first == 0:
                st1 = 1
                totalwith2 = 0
                totaldep2 = 0
            else:
                st1 = 0
                checked = date_logs(self.id2, self.userhist, self.userday, self.usertime, 0, st1)
                totalwith2 = checked.get_any_withdraw()  # Get Total Withdraw Last One
                totaldep2 = checked.get_any_totaldepposite()  # Get Total dep Last One

            datalogs = date_logs(self.id2, self.userhist, self.userday, self.usertime, opertaion, self.st1)
            datalogs.insert_operation(totalwith2, totaldep2, user2)  # Insert Values in Logs Table

            check = 1
        else:
            check = 0
        return check


# ===============================================[Fill ATM ]=====================================================
class ATMFill:

    def __init__(self, numberlist):
        self.NumberList = numberlist

    def filling(self):

        incash = DBOperation(1)
        g = incash.atm_full_check()  # Check Paper in ATM
        old200 = int(g[0][2]) + self.NumberList[0]
        old100 = int(g[0][3]) + self.NumberList[1]
        old50 = int(g[0][4]) + self.NumberList[2]
        old20 = int(g[0][5]) + self.NumberList[3]
        old10 = int(g[0][6]) + self.NumberList[4]
        numberstoreplace = [old200, old100, old50, old20, old10]
        incash.atm_x200x100x50_update(numberstoreplace)
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
class UnATMFill:

    def __init__(self, numberlist):
        self.NumberList = numberlist

    def filling(self):

        incash = DBOperation(1)
        g = incash.atm_full_check()  # Check Paper in ATM
        old200 = int(g[0][2]) - self.NumberList[0]
        old100 = int(g[0][3]) - self.NumberList[1]
        old50 = int(g[0][4]) - self.NumberList[2]
        old20 = int(g[0][5]) - self.NumberList[3]
        old10 = int(g[0][6]) - self.NumberList[4]
        numberstoreplace = [old200, old100, old50, old20, old10]
        incash.atm_x200x100x50_update(numberstoreplace)
        x = incash.atm_full_check()  # Check NewPaper in ATM
        new200 = int(x[0][2])
        new100 = int(x[0][3])
        new50 = int(x[0][4])
        new20 = int(x[0][5])
        new10 = int(x[0][6])
        sum_of_balance = 200*new200 + 100*new100 + 50*new50 + new20*20 + new10*10  # Get Value Of paper
        incash.atm_balance_update(sum_of_balance)  # insert Value

        return sum_of_balance

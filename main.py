# Importing
import time
from time import gmtime, strftime
from operations import *
from data_logs import *


# =======================================[ User Info ]==================================================================
ID = 2222  # --------------/////------/////-----> Ramon Ramon
PIN = 0  # default value
ID2 = 0  # default value
userday = strftime("%d", gmtime())
usertime = strftime("%H:%M:%S")
userhist = time.asctime()

# =======================================[ Window1.. Check Login ]======================================================
option1 = 0
option2 = 3

print(time.asctime())

while option1 == 0 and option2 != 0:
    print "Enter ur PIN"
    PIN = int(input())  # --------------/////------/////-----> Ramon

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@               Admin Check                        @@@@@@
    if ID == 1 and PIN == 1:
        flag = 2
        break
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    UserLogin = DBOperation(ID, PIN)
    LoginCheck = UserLogin.login_check()  # Return 1 for Success Return 0 for Fail

    flag = 0  # Check if User Pass Login
    if LoginCheck == 1:
        print "Welcome To ATM"
        option1 = 1
        flag = 1

    # =========/Class DBOperation/========
    # ===      Get User Balance        ===
        UserBalance = DBOperation(ID, PIN)
        b = UserBalance.balance_check()
    # ====================================

    else:
        option2 -= 1
        print "Wrong PIN  %s Chance" % option2

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ========/User Info After Log In/========
object1 = DBOperation(ID)
atmbc = object1.atm_full_check()  # ATM Info
if ID != 1:
    totalinfo = UserCheck(ID, userhist, userday, usertime)
    withdep = totalinfo.user_info_get()  # Total WithDraw and Deppsite In Day
    totaldep = withdep[1]  # Total Deppsite In Day
    userbalance = object1.balance_check()  # User Balance
    allowedwithdraw = 5000 - withdep[0]  # Allowed WithDraw PerDay
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@                                 [ Admin Window ]                                                       @@@@@@@

if flag == 2:
    print "press 1 to Check ATM Balnce"
    print "press 2 to  depposite Balance To ATM"
    x = int(input())
    if x == 1:
        print "ATM Balance Is %s" % atmbc[0][1]
    if x == 2:
        print "Enter Cash 200"
        x200 = int(input())
        print "Enter Cash 100"
        x100 = int(input())
        print "Enter Cash 50"
        x50 = int(input())
        print "Enter Cash 20"
        x20 = int(input())
        print "Enter Cash 10"
        x10 = int(input())
        NumberList = [x200, x100, x50, x20, x10]
        # =========/Class ATMFill/====================
        # ===      Return ATM Balnce               ===
        AtmBalanceInsert = ATMFill(NumberList)
        existbalance = AtmBalanceInsert.filling()
        # =============================================

        print "ATM Balance Now is  %s" % existbalance

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# =======================================[ Windows2..Operations ]=======================================================

elif flag == 1:
    print "press 1 to Enter withdraw "
    print "press 2 to Enter depposite "
    print "press 3 to Enter CheckBalance "
    print "press 4 to Enter Transfer "
    print "press 5 to Check History "
    x = int(input())  # --------------/////------/////-----> Ramon (Button Return Number 1 to 4)


# ========================================[ Windows3..withdraw ]========================================================
    if x == 1:
        print "Max of 200 = %s / 100 = %s / 50 = %s / 20 = %s 10 " \
              "= %s" % (atmbc[0][2], atmbc[0][3], atmbc[0][4], atmbc[0][5], atmbc[0][6])

        print "Your Balance %s" % userbalance
        print "WithDraw Allowed %s" % allowedwithdraw  # if user balance >
        print "Enter Cash 200"
        x200 = int(input())
        print "Enter Cash 100"
        x100 = int(input())
        print "Enter Cash 50"
        x50 = int(input())
        print "Enter Cash 20"
        x20 = int(input())
        print "Enter Cash 10"
        x10 = int(input())

        NumberList = [x200, x100, x50, x20, x10]
        # ===========/Class withdraw/============
        # ===      Return 0 or 1              ===
        get_money = WithDraw(ID, PIN, b, NumberList, userhist, userday, usertime, withdep[2], withdep)
        check = get_money.gui_balance_check()
        # =======================================
        userbalance = object1.balance_check()
        print check  # Operation
        print "your balance now %s" % userbalance
        print time.asctime()
# ========================================[ Windows4..depposite ]=======================================================
    elif x == 2:
        print "Enter Cash 200"
        x200 = int(input())
        print "Enter Cash 100"
        x100 = int(input())
        print "Enter Cash 50"
        x50 = int(input())
        print "Enter Cash 20"
        x20 = int(input())
        print "Enter Cash 10"
        x10 = int(input())

        NumberList = [x200, x100, x50, x20, x10]

        # =============/class depposite/==============
    # ====      Add Balance                    ===
        get_money2 = depposite(ID, PIN, b, NumberList, userhist, userday, usertime, withdep[2], withdep)
        check = get_money2.add_balance()
    # ============================================
        if check == 1:
            print "Your Balance Now is %s" % get_money2.b
            print(time.asctime())
        elif check == 0:
            print " More Than 30 Paper (Error)"


# ========================================[ Windows5..CheckBalance ]====================================================
    elif x == 3:
        pass  # Fix Comments warning

    # =============/class CheckBalance/=================
    # ====          Print balance                    ===
        UserBalanceCheck = DBOperation(ID, PIN)
        balancedChecked = UserBalanceCheck.balance_check()
    # ==================================================
        print "Your Balance is %s" % balancedChecked
        print(time.asctime())


# ========================================[ Windows6..Transfer ]========================================================
    elif x == 4:
        print "Enter ID Which U want to Trans For"
        ID2 = int(input())  # --------------/////------/////-----> Ramon (ID Of Other User)

    # =============/class DBOperation/==========
    # ====          Return 0 or 1            ===
        IdCheck = DBOperation(ID2)
        Check = IdCheck.id_check()
    # ==========================================
        if Check == 1:
            print "Enter Cash"
            cash = int(input())  # --------------/////------/////-----> Ramon (Get Number From Button Or Input Label)

        # =============/class transfer/==================
        # ====          Return 0 or 1                 ===
            UserTrans = transfer(ID, ID2, b, cash, userhist, userday, usertime, withdep[2], withdep)
            check = UserTrans.transfer_balance()
        # ===============================================

            if check == 1:
                print "You Trans %s To ID = %s Your Balance Now is %s" % (UserTrans.cash, UserTrans.id2, UserTrans.b)
                print(time.asctime())
            else:
                print "You Dont Have Enought"
        else:
            print "Wrong ID"
# ========================================[ Windows7..History ]========================================================
    elif x == 5:
        datalogs = date_logs(ID)
        results = datalogs.get_history()
        # Print History
        print "-------------------------------------------------------------------------------------------------------"
        print "|      Date               |       Operation           |  Total widthdrow | TotalDeppsite    | Your Balance  |"
        print "-------------------------------------------------------------------------------------------------------"
        for result in results:

            print "|%s |  %s   |        %s      |       %s        |     %s       |"\
                  % (result[2], result[5], result[7], result[8], result[9])
            print "---------------------------------------------------------------------------------------------------"

else:
    print "You Dont Have More Chance"


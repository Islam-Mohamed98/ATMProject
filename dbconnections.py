#                                   ====================================
#                                   =         Documentation            =
#                                   ====================================
#
#                                         //////////////////////
#                                         //    Method Guide  //
#                                         //////////////////////
#
#   login_check()                   -----> Check if ID and PIN Exist (Return 0 or 1 )
#   balance_check()                 -----> Check balance (Return balance)
#   add_balance(balance)            -----> Add Balance to User
#   id_check()                      -----> Check if ID Exist (Return 0 or 1)
#   insert_user(balance)            -----> Insert user ID / PIN / Balance
#   atm_balance_update(balance)     -----> Add balance to ATM
#   atm_balance_check()             -----> Return ATM Balance

import MySQLdb

# =======================================[  Connect TO DataBase ]=======================================================
# MYSQL INFO
host_name = "127.0.0.1"
user_name = "user"
password = "123456"
db_name = "info"
table_name = "information"

# Open DataBase connection
db = MySQLdb.connect(host_name, user_name, password, db_name)

# prepare a cursor object using cursor() method
cursor = db.cursor()


class DBOperation:
    # __init__ build in function
    def __init__(self, card_id=0, card_pin=0):
        self.id = card_id  # user ID
        self.pin = card_pin  # user PIN

# ============================================[  Login Check Method  ]==================================================
    # Method To Check ID
    def login_check(self):
        # Count ID and PIN in DB
        sql = "SELECT COUNT(1) FROM %s WHERE ID = %s and PIN = %s" % (table_name, self.id, self.pin)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
        except:
            print "Error : Cant Fetch Data"
        # Change tuple To int
        check = int(results[0][0])
        # Check = 0 if ID is not Exist // Check = 1 if ID is Exist
        return check

# ============================================[  Balance Check Method  ]================================================
    # Method To ID Balance
    def balance_check(self):
        # Get ID balance
        sql = "SELECT balance FROM %s WHERE ID = %s" % (table_name, self.id)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
        except:
            print "Error : Cant Fetch Data"
        # Change tuple To int
        balance = int(results[0][0])
        # Return Balance Value
        return balance

# ============================================[ Update Balance Method ]=================================================
    # Method To Update User Balance
    def add_balance(self, balance):
        # Insert New Balance
        sql = "UPDATE %s  SET balance = %s WHERE ID = %s " % (table_name, balance, self.id)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

# ============================================[ ID Check Method ]=======================================================
    # This Method For Transfer
    # Method To Check ID
    def id_check(self):
        # Count ID in DB
        sql = "SELECT COUNT(1) FROM %s WHERE ID = %s" % (table_name, self.id)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
        except:
            print "Error : Cant Fetch Data"
        # Change tuple To int
        check = int(results[0][0])
        # Check = 0 if ID is not Exist // Check = 1 if ID is Exist
        return check

# ============================================[ Add Card Method ]=======================================================
    # Method To New Card
    def add_card(self, balance):
        # Insert New User
        sql = "INSERT INTO %s (ID, PIN ,balance ) VALUES (%s, %s, %s)" % (table_name, self.id, self.pin, balance)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

# ============================================[ ATM Info Check ]========================================================
    # Function To Check ATM Balance
    def atm_full_check(self):
        # Get ATM Info
        sql = "SELECT * FROM atm WHERE 1"
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
        except:
            print "Error : Cant Fetch Data"
        # Change tuple To int

        # Return Value of Balance
        return results

# ============================================[ ATM Balance Update ]====================================================
    # Function To Update ATM Balance
    def atm_balance_update(self, balance):
        # Update ATM Balance
        sql = " UPDATE ATM  SET balance = %s" % balance
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

# ============================================[ Update 200 / 100/ 50 values ]===========================================
    # Function To Update Update 200 / 100/ 50 values
    def atm_x200x100x50_update(self, numberstoreplace):

        # Update ATM Balance
        sql = "UPDATE `atm` SET `200` = '%s', `100` = '%s', `50` = '%s'" \
              ", `20` = '%s'" \
              ", `10` = '%s' WHERE `atm`.`id` = 1" \
              % (numberstoreplace[0], numberstoreplace[1], numberstoreplace[2], numberstoreplace[3], numberstoreplace[4])
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()


# =============================================@@@[Delete]@@@=========================================================
def delete_rows():
    # Get all ID in Table information
    sql = "SELECT ID FROM information WHERE 1"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results1 = cursor.fetchall()
    except:
        print "Error : Cant Fetch Data"

    # Operation For Every ID
    for result in results1:
        # Get Number OF Operations Of ID
        sql2 = "SELECT COUNT(1) FROM logs WHERE ID = %s" % result
        try:
            # Execute the SQL command
            cursor.execute(sql2)
            # Fetch all the rows in a list of lists.
            results2 = cursor.fetchall()
            # IF Number OF Operation > 5
            if int(results2[0][0]) > 5:
                number = int(results2[0][0]) - 5

                # Select Last Operations
                sql3 = "SELECT Num FROM logs  WHERE ID = %s ORDER BY Num ASC LIMIT %s " % (int(result[0]), number)
                cursor.execute(sql3)
                results3 = cursor.fetchall()
                for results in results3:
                    # remove Last Operations
                    sql4 = "DELETE FROM logs WHERE Num = %s " % int(results[0])
                    try:
                        cursor.execute(sql4)
                        db.commit()
                    except:
                        # Rollback in case there is any error
                        db.rollback()
        except:
            print "Error : Cant Fetch Data"


delete_rows()

# ======================================================================================================================
# Disconnect from server
# db.close()

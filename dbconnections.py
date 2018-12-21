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
    def __init__(self, id=0, pin=0):
        self.id = id  # user ID
        self.pin = pin  # user PIN

# ============================================[  Login Check Method  ]==================================================
    # Function To Check ID
    def login_check(self):
        # Count ID in DB
        sql = "SELECT COUNT(1) FROM %s WHERE ID = %s and PIN = %s" % (table_name, self.id, self.pin)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
        except:
            print "Error : Cant Fetch Data123"
        # Change tuple To int
        check = int(results[0][0])
        # Check = 0 if ID is not Exist // Check = 1 if ID is Exist
        return check

# ============================================[  Balance Check Method  ]================================================
    # Function To Check ID
    def balance_check(self):
        # Count ID in DB
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
        # Check = 0 if ID is not Exist // Check = 1 if ID is Exist
        return balance

# ============================================[ Update Method ]=========================================================
    # Function To Update User
    def add_balance(self, balance):
        # Insert New User
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
    # Function To Check ID
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

# ============================================[ Insert Method ]=========================================================
    # Function To Insert User
    def insert_user(self, balance):
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

# ============================================[ ATM Balance Check ]=====================================================
    # Function To Check ATM Balance
    def atm_full_check(self):
        # Get ATM Balance
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
    def atm_x200x100x50_update(self, x200, x100, x50, x20, x10):
        # Update ATM Balance
        sql = "UPDATE `atm` SET `200` = '%s', `100` = '%s', `50` = '%s', `20` = '%s', `10` = '%s' WHERE `atm`.`id` = 1" % (x200, x100, x50, x20, x10)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
            print "sucsee"
        except:
            # Rollback in case there is any error
            db.rollback()
            print"fail"

# ======================================================================================================================
# Disconnect from server
# db.close()

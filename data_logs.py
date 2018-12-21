from dbconnections import cursor, db


class date_logs:

    # __init__ build in function
    def __init__(self, id , date=0, day=0, time=0, operation=0, st1=0):
        self.id = id
        self.date = date
        self.day = day
        self.time = time
        self.operation = operation
        self.st1 = st1
# ============================================[  First operation Check  ]===============================================
    # Function To Check 1st
    def first_operation_check(self):


        sql = "SELECT COUNT(1) FROM logs WHERE 1st = 1 and Day1 = %s and ID = %s" % (self.day, self.id)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
        except:
            print "Error : Cant Fetch first_operation"
        # Change tuple To int
        check = int(results[0][0])
        # Check = 0 if ID is not Exist // Check = 1 if ID is Exist
        return check

# ============================================[  Get First Operatin time Check  ]=======================================
    # Function To Get Time
    def first_operation(self):
        # Count
        sql = "SELECT time1 FROM logs WHERE 1st = 1 and Day1 = %s and ID = %s" % (self.day, self.id)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
        except:
            print "Error : Cant Fetch Data123"
        # Change tuple To int
        check = str(results[0][0])
        # Check = 0 if ID is not Exist // Check = 1 if ID is Exist
        return check

# ============================================[  Insert Operation  ]====================================================
    # Function To Check 1st
    def insert_operation(self, totalwithdraw, totaldepposite):
        sql = "INSERT INTO logs (ID, Date1 ,Day1, time1, operation, 1st, totalwithdraw, totaldepposite) VALUES ('%s','%s" \
              "','%s','%s','%s', '%s', '%s', '%s')" % (self.id, self.date, self.day, self.time, self.operation, self.st1, totalwithdraw, totaldepposite)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
            print " succ"
        except:
            # Rollback in case there is any error
            print "error"
            db.rollback()

# ============================================[  Get  Any Row  ]========================================================
    # Function To Get Totalwithdraw Per Day
    def get_any_withdraw(self):
        # Count
        sql = "SELECT totalwithdraw FROM logs  WHERE Day1 = %s and ID = %s ORDER BY Num DESC" \
              " LIMIT 1" % (self.day, self.id)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
        except:
            print "Error : Cant Fetch Data1235"
        # Change tuple To int
        check = int(results[0][0])
        return check

# ============================================[  Get  Any Row  ]========================================================
    # Function To Get totaldepposite Per Day
    def get_any_totaldepposite(self):

        sql = "SELECT totaldepposite FROM logs  WHERE Day1 = %s and ID = %s ORDER BY Num DESC LIMIT 1" % (self.day, self.id)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
        except:
            print "Error : Cant Fetch Data1235"
        # Change tuple To int
        check = int(results[0][0])
        return check


# ============================================[  Get History ]========================================================
    #  History Return
    def get_history(self):

        sql = "SELECT * FROM logs  WHERE ID = %s ORDER BY Num ASC " % self.id
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
        except:
            print "Error : Cant Fetch Data1235"
        # Change tuple To
        return results
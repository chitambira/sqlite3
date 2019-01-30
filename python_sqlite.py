import sqlite3

#*********
#********* GLOBAL FUNCTION DEFINITIONS
#*********

def connect_to_db(dbase):
	""" create the connection to the SQLite database that is specified by dbase
	"""
	try:
		conxn = sqlite3.connect(dbase)
		return conxn
	except Exception as e:
		print(e)
	return None

def create_table(conxn, create_statement, insert_statement):
	""" create a table from the database using create_statement
	"""
	try:
		curs = conxn.cursor()
		curs.execute(create_statement)
		curs.execute(insert_statement)
		conxn.commit()
	except Exception as e:
		print(e)

def query_table(conxn, query_statement):
	""" query a table from the database using query_statement
	"""
	try:
		curs = conxn.cursor()
		curs.execute(query_statement)
		print(curs.fetchall())
	except Exception as e:
		print(e)

#*********
#********* MAIN
#*********

if __name__ == "__main__":

	database = "pythonsqlite.db"
	tablename = "records"
 
	create_statement = """CREATE TABLE IF NOT EXISTS %s (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        surname text,
                                        age integer,
					weight integer
                                    );""" % (tablename)

	insert_statement = """INSERT INTO %s (
					id,
					name,
					surname,
					age,
					weight)
				VALUES
					(1,"John","Doe",55,100
					),
					(4,"Robert","Bob",94,75
					),
					(2,"Sarah","Smith",30,65
					),
					(5,"Bill","Williams",75,72
					),
					(3,"Theresa","Miles",67,85);
				""" % (tablename)

	query_statement = "SELECT * FROM %s;" % (tablename)
 
	connection = connect_to_db(database)

	if connection is not None:
		#create table
		print("Creating table %s in database %s ..." % (tablename,database))
		create_table(connection, create_statement, insert_statement)

		#query table
		print("Querying table %s in database %s ..." % (tablename,database))
		query_table(connection, query_statement)

	else:
		print("Error! database connection failure.")

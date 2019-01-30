# sqlite3
This repo contains a simple python script to demonstrate connection to sqlite3 database.


The script "python_sqlite.py" is self-contained to make it easier to read. \
The __Main__ function sets the 4 parameters that are needed to create the sqlite database and query it. \
    &nbsp &nbsp * database = "pythonsqlite.db" #This specifies the name for the database, can be changed as required. \
    &nbsp &nbsp * create_statement = """SQL create table statement""" #This specifies the table name and the schema. \
    &nbsp;&nbsp * insert_statement = """SQL insert statement here""" #This specifies the records that are doing to be entered. \
    &nbsp;&nbsp * query_statement = """SQL db query statement here""" #This specifies the database query as needed. \
    
Please note this script has been made self contained for readability, otherwise in a real implementation, the following modifications will make it re-usable; \
    - Use getopt and sys to specify script arguments and options, \
    (e.g. pythonsqlite.py -m <mode> -d <database> -t <tablename> -s <sql_statement_file> -f <filename>)
    - For the above example; \
          <mode> would be [ create or query ]. \
          <sql_statement_file> would be a text file with the SQL statement(s). \
          <filename> could be a csv file that contains the records to be written. \
          <database> and <tablename> are self explanatory. \
    - A usage() function can be used to guide the users, together with help information.

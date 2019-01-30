# sqlite3
This repo contains a simple python script to demonstrate connection to sqlite3 database.


The script "__python_sqlite.py__" is self-contained to make it easier to read. \
The __Main__ function sets the 4 parameters that are needed to create the sqlite database and query it. \
    * *database* = "__pythonsqlite.db__" #This specifies the name for the database, can be changed as required. \
    * *create_statement* = """SQL create table statement""" #This specifies the table name and the schema. \
    * *insert_statement* = """SQL insert statement here""" #This specifies the records that are doing to be entered. \
    * *query_statement* = """SQL db query statement here""" #This specifies the database query as needed.
    
The script creates a table named *records* and inserts records of name, surname, age and weight for 5 people.
    
Please note this script has been made self contained for readability, otherwise in a real implementation, the following modifications will make it re-usable; \
    * Use getopt and sys to specify script arguments and options, \
    (e.g.
    ```bash
       python_sqlite.py -m <mode> -d <database> -t <tablename> -s <sql_statement_file> -f <filename>)
    ```
    ) \
    * For the above example; \
        + <*mode*> would be [ *create or query* ]. \
        + <*sql_statement_file*> would be a text file with the SQL statement(s). \
        + <*filename*> could be a csv file that contains the records to be written. \
        + <*database*> and <tablename> are self explanatory. \
    * A *usage()* function can be used to guide the users, together with help information.

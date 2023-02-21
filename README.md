# Template Database Project
Provides a quick way to setup sqlite database and flask. Uses jinja macros to render html. The project is meant to prioritise reusability and ease of adaptation to new data. 

# How to Run
### Dependencies
- Python
- Flask
- Sqlite3

`python3 server.py`

It is advised to use a Linux or MacOS machine for bash scripts.
# Database Creation
Running `import_tables.sh` will read the csv files at `Tables/` and create `import_test.db` file at project root directory.

`./import_tables.sh`

In the case that some columns of your data need to be removed:
- Place the original csv files at `Tables/full_backup/` directory.
- Modify `drop_unnecessary.sql` file by adding `DROP` statements for the columns to be removed. 
- Run `import_bulk.sh` script to populate the Tables directory with the distilled csv files.

# Adapting to Your Data
1. Replace example csv files in `Tables/` with your own csv files. 
- Check [Database Creation](#database-creation) section to generate Sqlite database.
2. Modify `models.py` to have successful object-table correspondence.
3. Modify `services/service.py` and `views.py` by adding class definitions for each table.
4. Modify `server.py` by using the `set_urls()` function for each table. 
5. Modify `templates/layout.html` to provide links to your table pages from the home page.


# Architecture
Sqlite3 is used as database.
## Service
SQL query generators reside in service.py which can be inherited by any table service class. Add, Update, Delete and Get methods of the parent class Service can be inherited by each table. They use objects in models to get information about columns. 
## Models
Tables' columns are stored in models.py as reference. It is used by services to generate queries. 
## Server
Url endpoints are declared in server.py. It is responsible to run the server. View functions are assigned to urls.
## Views
View functions are declared in views.py. It is responsible for connecting services with appropriate url's and template files which create html.
## Templates
Jinja templates are in templates/ directory. Jinja macro list_macro.html is responsible of serving appropriate html file depending on the context and data. 
## Tables
CSV files are stored in Tables/ to have common source of data at database creation.





from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, MetaData, ARRAY

connection_string = 'postgresql://user:pass@postgresql/mydatabase'

db = create_engine(connection_string)  
engine = db.connect() 
meta = MetaData(engine)
meta.reflect(bind=engine)

# list all tables
print('list all tables')
meta.tables

# create table
print('create table')
table = Table("queensolutions", 
                         meta,  
                         Column("solution_index", Integer, primary_key=True),
                         Column("number_queens", Integer, primary_key=True),
                         Column("solution", ARRAY(Integer)),
                         extend_existing=True)

table.create(engine)
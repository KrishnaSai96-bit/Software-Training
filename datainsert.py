from sqlalchemy import insert

from 
database import 
engine, SessionLocal

from 
sqlalchemy.sql 
import text



from 
csv import 
DictReader



db = 
SessionLocal()



with 
open("posts_data.csv", 
'r') as 
f:

    dict_reader = 
DictReader(f)

    entries = 
list(dict_reader)

    # print(entries)



# statement = insert(PostBase).values([{'title':title, 'content':content, 'salary':salary} for title, content, salary in rows])

for 
entry in 
entries:

    statement = 
text("INSERT INTO posts(title, content, user_id) VALUES(:title, :content, :user_id)")

    db.execute(statement,
entry)

    db.commit()
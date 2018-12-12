import sqlite3 as database
conn_data=database.connect('nav.db')
print('database is created')
cur=conn_data.cursor()

print(" 1) create table")
print(" 2) insert values into table")
print(" 3) view a table")
print(" 4) read one from table")
print(" 5) delete values from  table")
print(" 6) update values to the table")

option=int(input("enter u r option"))

if option==1:
    cur.execute("create table if not exists student(idno integer, name text,marks integer,average real)")
    print(" table created")
    conn_data.close()
if option==2:
    id=int(input("enter u r idno"))
    na=input("enter u r name")
    ma=int(input("enter u r marks"))
    avg=float(input("enter u r average"))
    cur.execute("insert into student values(?,?,?,?)",(id,na,ma,avg))
    conn_data.commit()
    print("insert all values ")
if option==3:
    cur.execute("select * from student")
    res=cur.fetchall()
    print(res)
if option==4:
    id =int(input("enter id no"))
    cur.execute("select * from student where  (?)",(id,))
    resl=cur.fetchone()
    print(resl)
    conn_data.commit()
    print("read one")
if option==5:
    id = int(input("enter id no"))
    cur.execute("delete from student where idno=?",(id,))
    conn_data.commit()
    print("delete values")
if option==6:
    id=int(input("enter to change id no"))
    name1=input("enter to change the name")
    cur.execute("update student set name=? where idno=?",(name1,id))
    conn_data.commit()
    print("update all")


print("thanks")
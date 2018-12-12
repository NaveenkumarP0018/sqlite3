import sqlite3 as navee
conn_data = navee.connect('sbi.db')
print('acccount is created')
cur = conn_data.cursor()

cur.execute("create  table  if not exists account(ac_no integer, ac_name text, balance real, pin integer)")
acno = int(input("enter account no:"))
nam = input("enter name :")
bal = int(input("enter balance:"))
pin = int(input("enter u r pin :"))
cur.execute("insert into account values (?,?,?,?)", (acno, nam, bal, pin))
conn_data.commit()

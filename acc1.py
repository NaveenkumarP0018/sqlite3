import sqlite3 as navee
conn_data = navee.connect('sbi.db')
cur = conn_data.cursor()

print("welcome to SBI ATM services ")
pin = int(input("please enter u r pin no:"))
a=cur.execute("select * from account  where pin=?", (pin,))
res = a.fetchone()
if res == None:
     print(" you entred invalid pin no")
else:
    wd_amt = int(input("please enter withdrawal_amount"))
    if wd_amt % 100 != 0:
        print("you entered invalid amount:")
    else:
        if wd_amt > 10000:
         print("withdraw amount is max 10000$rs only")
        else:
            if wd_amt > res[2]:
                print("amount is not avalable")

            else:
                curr_bal = res[2]-wd_amt
                cur.execute("update account set balance=? where pin=?", (curr_bal, pin,))
                conn_data.commit()
                print(curr_bal)
                print("your transcation is completed ")
                print("thanks for visiting")

print("please dont share ur bank details to any one")




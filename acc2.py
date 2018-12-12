import sqlite3 as navee
conn_data = navee.connect('sbi.db')
cur = conn_data.cursor()


print("welcome to SBI ATM services ")
pin = int(input("please enter u r pin no:"))
a=cur.execute("select * from account  where pin=?", (pin,))
res = a.fetchone()
if res == None:
     print(" you entred invalid pin no")
pin=int(input("enter u r account number"))
cur.execute("delete from account  where pin=?", (pin))

# else:
#     print("1) withdraw amount")
#     print("2) deposit amount")
#     print("3) change name")
#     option=int(input("enter your option:"))
#     if option > 4:
#         print("entered option is not valid")
#     elif option==1:
#         wd_amt = int(input("please enter withdrawal_amount"))
#         if wd_amt % 100 != 0:
#             print("you entered invalid amount:")
#         else:
#             if wd_amt > 10000:
#                 print("withdraw amount is max 10000$rs only")
#             else:
#                 if wd_amt > res[2]:
#                     print("amount is not avalable")
#                 else:
#                     curr_bal = res[2] - wd_amt
#                     cur.execute("update account set balance=? where pin=?", (curr_bal, pin,))
#                     conn_data.commit()
#                     print(curr_bal)
#     elif option == 2:
#         dp_amt=int(input("enter your deposit amount"))
#         if dp_amt % 50 !=0:
#             print("you entered amount is not valid")
#         else:
#             if dp_amt > 49000:
#                 print("your deposit amount is not valid")
#             else:
#                 dp_amt=res[2]+dp_amt
#                 cur.execute("update account set balance=? where pin=?", (dp_amt,pin))
#                 conn_data.commit()
#                 print(dp_amt)







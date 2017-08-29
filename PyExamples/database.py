import MySqldb
#open database connection
db=MySqldb.connect("localhost","testuser","test123","TESTDB")
cursor=db.cursor()
sql="Insert into Employee(first_name,\last_name,age,sex,inco
me)\values("%s","%s","%d","%d","%d")"%\("Ram","Khadka",45,"Male",34000)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
    db.close()    

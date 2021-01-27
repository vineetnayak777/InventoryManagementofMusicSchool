import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="7019252847", database="sadhu")
c = mydb.cursor()
c.execute("USE sadhu;")

c.execute("""
            ALTER TABLE Events drop foreign key events_ibfk_2;
            );
            """)
mydb.commit()
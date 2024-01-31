import sqlite3

connection = sqlite3.connect('University.db')
cursor = connection.cursor()

# cursor.execute("drop table UNIVERSITY;")
# sql_cmd='''CREATE TABLE UNIVERSITY(
#             NAME VARCHAR(15), 
#             MAIL VARCHAR(25) NOT NULL, 
#             USERNAME VARCHAR(35) PRIMARY KEY, 
#             PASSWORD VARCHAR(8) NOT NULL);'''

# cursor.execute("drop table STUDENT;")
# sql_cmd1='''CREATE TABLE STUDENT(
#             NAME VARCHAR(15), 
#             REGISTER_NUMBER INT PRIMARY KEY, 
#             YEAR VARCHAR(25) NOT NULL,
#             CLASSROOM_ID VARCHAR(20),
#             DEPARTMENT_ID INT,
#             SEMESTER INT NOT NULL,
#             FOREIGN KEY (CLASSROOM_ID) REFERENCES CLASSROOM (CLASSROOM_ID),
#             FOREIGN KEY (DEPARTMENT_ID) REFERENCES DEPARTMENT (DEPARTMENT_ID));'''

# cursor.execute("drop table CLASSROOM;")
# sql_cmd2='''CREATE TABLE CLASSROOM(
#             CLASSROOM_ID VARCHAR(20) PRIMARY KEY,
#             CLASSROOM_LABEL VARCHAR(20) NOT NULL,
#             CLASSROOM_CAPACITY INT NOT NULL, 
#             BENCH_COUNT INT NOT NULL,
#             BENCH_CAPACITY INT NOT  NULL,
#             CLASSROOM_NUMBER INT NOT NULL,
#             DEPARTMENT_ID INTEGER,
#             FOREIGN KEY (DEPARTMENT_ID) REFERENCES DEPARTMENT (DEPARTMENT_ID));'''

# cursor.execute("drop table DEPARTMENT;")
# sql_cmd3='''CREATE TABLE DEPARTMENT(
           
#             DEPARTMENT_NAME VARCHAR(80) NOT NULL, 
#             DEPARTMENT_ID INTEGER PRIMARY KEY,
#             CLASS_COUNT INTEGER NOT NULL);'''
# cursor.execute("drop table COURSE;")
# sql_cmd4='''CREATE TABLE COURSE (
#             COURSE_CODE VARCHAR(30) PRIMARY KEY ,
#             COURSE_TITLE VARCHAR(70),
#             DEPARTMENT_ID INT,
#             FOREIGN KEY (DEPARTMENT_ID) REFERENCES DEPARTMENT (DEPARTMENT_ID));'''

            

# cursor.execute(sql_cmd)
# print("LOGIN TABLE CREATED SUCCESSFULLY")
# cursor.execute(sql_cmd3)
# print("DEPARTMENT TABLE CREATED SUCCESSFULLY")
# cursor.execute(sql_cmd2)
# print("CLASSROOM TABLE CREATED SUCCESSFULLY")
# cursor.execute(sql_cmd1)
# print("STUDENTS TABLE CREATED SUCCESSFULLY")
# cursor.execute(sql_cmd4)
# print("COURSE TABLE CREATED SUCCESSFULLY")


# sql_cmd='''INSERT INTO UNIVERSITY VALUES(
#             'kayathri','kayathri@gmail.com',
#             'kayathri51','SSN');'''
# sql_cmd1='''INSERT INTO UNIVERSITY VALUES(
#             'kaviya','kaviya@gmail.com',
#             'kaviya22','SSN');'''
# sql_cmd2='''INSERT INTO UNIVERSITY VALUES(
#             'manasi','manasi@gmail.com',
#             'manasi52','SSN');'''

# cursor.execute(sql_cmd)
# cursor.execute(sql_cmd1)
# cursor.execute(sql_cmd2)
# print("login record added succesfully")

# sql_cmd6='''INSERT INTO DEPARTMENT VALUES('IT',5002,7);'''
# sql_cmd7='''INSERT INTO DEPARTMENT VALUES('CSE',5001,6);'''
# sql_cmd8='''INSERT INTO DEPARTMENT VALUES('ECE',5003,8);'''

# cursor.execute(sql_cmd6)
# cursor.execute(sql_cmd7)
# cursor.execute(sql_cmd8)
# print("department record added successfully")

# sql_cmd9='''INSERT INTO CLASSROOM VALUES('ITA','A',50,25,2,37,5002);'''
# sql_cmd10='''INSERT INTO CLASSROOM VALUES('ECEA','A',40,20,2,31,5003);'''
# sql_cmd11='''INSERT INTO CLASSROOM VALUES('CSEA','A',58,29,2,33,5001);'''

# cursor.execute(sql_cmd9)
# cursor.execute(sql_cmd10)
# cursor.execute(sql_cmd11)
# print("classroom data added successfully")


# sql_cmd3='''INSERT INTO STUDENT VALUES(
#             'manasi',3122215002052,'Third','ITA',5002,5);'''
# sql_cmd4='''INSERT INTO STUDENT VALUES(
#             'kaviyapriya',3122215003050,'Third','ECEA',5003,5);'''
# sql_cmd5='''INSERT INTO STUDENT VALUES(
#             'kayathri',3122215001051,'Third','CSEA',5001,5);'''
# cursor.execute(sql_cmd3)
# cursor.execute(sql_cmd4)
# cursor.execute(sql_cmd5)
# print("student data added successfully")

# sql_cmd12='''INSERT INTO COURSE VALUES('UIT2001','ARTIFICIAL INTELLIGENCE',5002);'''
# sql_cmd13='''INSERT INTO COURSE VALUES('UIT3001','EMBEDDED SYSTEMS',5003);'''
# sql_cmd14='''INSERT INTO COURSE VALUES('UIT4001','OPERATING SYSTEM',5001);'''
# cursor.execute(sql_cmd12)
# cursor.execute(sql_cmd13)
# cursor.execute(sql_cmd14)
# print("course data added successfully")  
# connection.commit()
sql_cmd3='''INSERT INTO STUDENT VALUES(
             'mythreya',3122215002064,'Third','ITA',5002,5);'''
sql_cmd4='''INSERT INTO STUDENT VALUES(
             'jovitha',3122215003042,'Third','ECEA',5003,5);'''
sql_cmd5='''INSERT INTO STUDENT VALUES(
            'merudhula',3122215002059,'Third','CSEA',5001,5)'''
sql_cmd6='''INSERT INTO STUDENT VALUES(
            'mathangi',3122215001059,'Third','ITA',5002,5)'''
sql_cmd7='''INSERT INTO STUDENT VALUES(
             'harini',3122215003033,'Third','ECEA',5003,5);'''
sql_cmd8='''INSERT INTO STUDENT VALUES(
            'harshini',3122215001038,'Third','CSEA',5001,5)'''
sql_cmd9='''INSERT INTO STUDENT VALUES(
            'hemasri',3122215001048,'Third','CSEA',5001,5)'''
sql_cmd10='''INSERT INTO STUDENT VALUES(
            'kaushik',3122215001047,'Third','CSEA',5001,5)'''
sql_cmd11='''INSERT INTO STUDENT VALUES(
            'kavin',3122215001049,'Third','CSEA',5001,5)'''
sql_cmd12='''INSERT INTO STUDENT VALUES(
            'karunagaran',3122215001046,'Third','CSEA',5001,5)'''
sql_cmd13='''INSERT INTO STUDENT VALUES(
            'lokesh',3122215001053,'Third','CSEA',5001,5)'''
sql_cmd14='''INSERT INTO STUDENT VALUES(
             'harish',3122215002032,'Third','ITA',5002,5);'''
sql_cmd15='''INSERT INTO STUDENT VALUES(
             'deepesh',3122215002023,'Third','ITA',5002,5);'''
sql_cmd16='''INSERT INTO STUDENT VALUES(
             'arunasri',3122215002015,'Third','ITA',5002,5);'''
sql_cmd17='''INSERT INTO STUDENT VALUES(
             'dhanushpriyan',3122215002025,'Third','ITA',5002,5);'''
sql_cmd18='''INSERT INTO STUDENT VALUES(
             'kaushika',3122215002029,'Third','ITA',5002,5);'''
sql_cmd19='''INSERT INTO STUDENT VALUES(
             'aashish',3122215003002,'Third','ECEA',5003,5);'''
sql_cmd20='''INSERT INTO STUDENT VALUES(
             'madhumitha',3122215003053,'Third','ECEA',5003,5);'''
sql_cmd21='''INSERT INTO STUDENT VALUES(
             'natarajan',3122215003066,'Third','ECEA',5003,5);'''
sql_cmd22='''INSERT INTO STUDENT VALUES(
             'naresh',3122215003065,'Third','ECEA',5003,5);'''
sql_cmd23='''INSERT INTO STUDENT VALUES(
             'nasrin',3122215003064,'Third','ECEA',5003,5);'''
cursor.execute(sql_cmd3)
cursor.execute(sql_cmd4)
cursor.execute(sql_cmd5)
cursor.execute(sql_cmd6)
cursor.execute(sql_cmd7)
cursor.execute(sql_cmd8)
cursor.execute(sql_cmd9)
cursor.execute(sql_cmd10)
cursor.execute(sql_cmd11)
cursor.execute(sql_cmd12)
cursor.execute(sql_cmd13)
cursor.execute(sql_cmd14)
cursor.execute(sql_cmd15)
cursor.execute(sql_cmd16)
cursor.execute(sql_cmd17)
cursor.execute(sql_cmd18)
cursor.execute(sql_cmd19)
cursor.execute(sql_cmd20)
cursor.execute(sql_cmd21)
cursor.execute(sql_cmd22)
cursor.execute(sql_cmd23)

connection.commit()


sql_cmd15='''SELECT * FROM UNIVERSITY;'''
sql_cmd16='''SELECT * FROM DEPARTMENT;'''
sql_cmd17='''SELECT NAME,REGISTER_NUMBER,BENCH_COUNT FROM STUDENT,CLASSROOM WHERE STUDENT.CLASSROOM_ID=CLASSROOM.CLASSROOM_ID;'''
sql_cmd18='''SELECT * FROM STUDENT;'''
sql_cmd19='''SELECT * FROM COURSE;'''
cursor.execute(sql_cmd15)
rows=cursor.fetchall()
print(rows)
cursor.execute(sql_cmd16)
rows=cursor.fetchall()
print(rows)
cursor.execute(sql_cmd17)
rows=cursor.fetchall()
print("HEREE",rows)
cursor.execute(sql_cmd18)
rows=cursor.fetchall()
print(rows)
cursor.execute(sql_cmd19)
rows=cursor.fetchall()
print(rows)

connection.commit()
connection.close()
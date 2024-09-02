import mys-ql.connector as my
connect = my.connect(host = 'localhost', user =' root ', passwd = 'mayank' , db =
'myschool')
cursor=connect.cursor()
#a='create database MySchool'
#cursor.execute (a)
#cursor.execute (‘create table student (NAME VARCHAR (50) NOT NULL, CLASS INT NOT NULL,
ADNO INT PRIMARY KEY, ADDRESS VARCHAR (50) NOT NULL, PHONE VARCHAR (50) NOT NULL)’)
#cursor.execute (‘create table teachers (NAME VARCHAR (50) NOT NULL, POST VARCHAR (30)
NOT NULL, SALARY VARCHAR (10) NOT NULL, ADDRESS VARCHAR (50) NOT NULL, PHONE VARCHAR (50)
NOT NULL, ACNO VARCHAR (10) PRIMARY KEY)’)
#cursor.execute (‘create table cattendence (DATE VARCHAR (30) NOT NULL, CLASS INT NOT
NULL, ABSENT VARCHAR (200) NOT NULL)’)
#cursor.execute (‘create table tattendence (DATE VARCHAR (30) NOT NULL, ABSENT VARCHAR
(200) NOT NULL)’)
#cursor.execute (‘create table fees (NAME VARCHAR (50) NOT NULL, CLASS INT NOT NULL, ADNO
INT PRIMARY KEY, MONTH VARCHAR (20) NOT NULL, FEE VARCHAR (30) NOT NULL, DATE VARCHAR
(30) NOT NULL, ISPAID VARCHAR (5) NOT NULL)’)
#cursor.execute (‘create table salary (NAME VARCHAR (30) NOT NULL, MONTH VARCHAR (20) NOT
NULL, PAID VARCHAR (30) NOT NULL, ACNO VARCHAR (10))’)
def ast():
 print('PLEASE ENTER DETAILS OF THE STUDENT FOR ADDMISSION')
 n=input("Student's name :")
 c=input("In which Class you want Addmission :")
 r=input('Enter assigned AddmissionNumber :')
 a=input('Give the Permanent Address :' )
 p=input('Give the Contact Number :')
 data=(n ,c ,r ,a ,p)
 sql = 'insert into Student values(%s,%s,%s,%s,%s)'
 c=connect.cursor()
 c.execute(sql ,data)
 connect.commit()
 print('DATA ENTERED SUCCSESSFULLY')
 print('-'*150)
 main()
def rst() :
 print('PLEASE ENTER DETAILS OF THE STUDENT FOR REMOVING')
 c=input('Class of Student :')
 r=input('Addmission Number of Student :')
 data = (c ,r)
 sql = 'delete from Student where CLASS =%s and ADNO =%s'
 c = connect.cursor()
 c.execute(sql ,data)
 connect.commit()
 print('DATA UPDATED')
 print('-'*150)
 main()

def addt() :
 print('PLEASE ENTER DETAILS OF TEACHER')
 n = input("Enter Teacher's name :")
 p = input('Enter Post :')
 s = input('Salary :')
 a = input('Address')
 ph = input('Contact Number :')
 ac = input('Account Number :')
 data = (n ,p ,s ,a ,ph ,ac)
 sql = 'insert into teachers values(%s,%s,%s,%s,%s,%s)'
 c = connect.cursor()
 c.execute(sql ,data)
 connect.commit()
 print('DATA ENTERED SUCCESSFULLY')
 print('-'*150)
 main()

def remt() :
 n= input('Teachers Name :')
 ac= input('Account Number :')
 data = (n ,ac)
 sql = 'delete from teachers where name =%s and acno =%s'
 c = connect.cursor()
 c.execute(sql ,data)
 connect.commit()
 print('DATA UPDATED')
 print('-'*150)
 main()

def abclass() :
 d = input('Date :')
 cl = input('Class :')
 ab = input('Names of Absent Students :')
 data = (d, cl, ab)
 sql = 'insert into cattendence values(%s,%s,%s)'
 c = connect.cursor()
 c.execute(sql ,data)
 connect.commit()
 print('DATA ENTERED SUCCESSFULLY')
 print('-'*150)
 main()

def abt() :
 d = input('Date :')
 ab = input('Names of Absent Teachers :')
 data = (d, ab)
 sql = 'insert into tattendence values(%s,%s)'
 c = connect.cursor()
 c.execute(sql ,data)
 connect.commit()
 print('DATA ENTERED SUCCESSFULLY')
 print('-'*150)
 main()

def subfee() :
 n = input("Student's name :")
 c = input("Class:")
 r = input('Enter assigned Addimision Number :')
 m = input('Month and Year :')
 f = input('Fees : ')
 d = input('Date :')
 i = input('IS FEE PAID :')
 data = (n ,c ,r ,m ,f ,d ,i)
 sql = 'insert into fees values(%s,%s,%s,%s,%s,%s,%s)'
 c = connect.cursor()
 c.execute(sql ,data)
 connect.commit()
 print('DATA ENTERED SUCCESSFULLY')
 print('-'*150)
 main()
def pays() :
 n = input('Teachers Name :')
 m = input('Month :')
 p = input('Is Salary Paid Y/N :')
 a = input('Account Number :')
 data = (n ,m ,p ,a)
 sql = 'insert into salary values(%s,%s,%s,%s)'
 c = connect.cursor()
 c.execute(sql ,data)
 connect.commit()
 print('DATA ENTERED SUCCESSFULLY')
 print('-'*150)
 main()

def dclass() :
 cl = input('Enter Class :')
 data = (cl,)
 #sql='select student.NAME ,student.ADNO ,student.CLASS ,student.ADDRESS
 ,student.PHONE ,fees.ISPAID where student.ADNO=fees.ADNO where class = %s'
 sql = 'select * from Student where class = %s'
 c = connect.cursor()
 c.execute(sql ,data)
 d = c.fetchall()
 for i in d:
 print('Name :' , i[0])
 print('Class :' , i[1])
 print('Addmission Number :' , i[2])
 print('Address :' , i[3])
 print('Contact Number' , i[4])
 print('>' ,"-"*161 ,'<')
 print('-'*165)
 main()

def dteacher():
 ad = input('Enter Addmission Number of Teacher :')
 data = (ad,)
 sql = 'select * from teachers where acno = %s'
 c = connect.cursor()
 c.execute(sql ,data)
 d=c.fetchall()
 for i in d:
 print('Name :' , i[0])
 print('Post :' , i[1])
 print('Salary :' , i[2])
 print('Address :' , i[3])
 print('Contact Number' , i[4])
 print('Account number' , i[5])
 print('>' ,"-"*161 ,'<')
 print('-'*165)
 main()


def exits() :
 print("\n\n\t\t\t\t\t Thanks for using SCHOOL MANAGEMENT SYSTEM...")
 print('~'*102)
 print("\t\t\t\t\t\t| Created By - Mayank Pathak |")
 print('<>'*51)

def main():
 print('\t\t\t\t\t\tSCHOOL MANAGEMENT')
 print('''\n\t\t\t\t\t\tSARAF PUBLIC SCHOOL''' )
 print('_'*167)
 print('\t\t\t\t [A]DD STUDENT',end='\t\t\t')
 print('[TA]DD TEACHER')
 print('\t\t\t\t [R]EMOVE STUDENT',end='\t\t')
 print('[TR]EMOVE TEACHER')
 print('\t\t\t\t [S]TUDENT ATTENDENCE',end='\t\t')
 print('[T]EACHER ATTENDENCE')
 print('\t\t\t\t [F]EE SUBMISSION',end='\t\t')
 print('[P]AY SALARY')
 print('\t\t\t\t [D]ISPLAY CLASS',end='\t\t\t')
 print('[TD]ISPLAY TEACHERS')
 print('\t\t\t\t\t\t\t''[E]XIT')
 print('_'*167)
 ch=input('Enter a task (given inside square bracket)')
 print('>' ,"-"*161 ,'<')
 if ch =='A':
 ast()
 elif ch =='TA':
 addt()
 elif ch =='R':
 rst()
 elif ch =='TR':
 remt()
 elif ch =='S':
 abclass()
 elif ch =='T':
 abt()
 elif ch =='F':
 subfee()
 elif ch =='P':
 pays()
 elif ch =='D':
 dclass()
 elif ch =='TD':
 dteacher()
 elif ch =='E':
 exits()

 else :
 print('WRONG CHOICE .......')
 print('GIVE A SUITABLE TASK...... ')
 main()

def password() :
 p=input('GIVE PASSWORD TO LOGIN :')
 if p == 'SPS123':
 main()
 else :
 print('WRONG PASSWORD')
 print('TRY AGAIN.....')
 password()
#PROGRAM STARTS HERE
password()




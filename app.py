import mysql.connector as mysql

mycon = mysql.connect(host="localhost", user="root", passwd="Ajay@154", database="university")

cursor = mycon.cursor()
# if mycon.is_connected():
#     print("successfull")


while True:
    print("\n\n\n\n************WELCOME TO THE UNIVERSITY************************\n\n")
    print("select  \n1.students \n2.lecturers \n3.subjects\n4.courses\n5.fees\n6.exit\n\n")
    select = int(input("select a option from above : "))

    if select == 1:
        print(
            "select  \n1.insert new student \n2.Delete a student \n3.update a student details\n4.display all students\n")
        select = int(input("select a number"))
        if select == 1:
            try:
                rollno = str(input("Enter student rollno :-"))
                name = str(input("Enter student name :-"))
                age = str(input("Enter student age :-"))
                sex = str(input("Enter sex(M/F) :-"))
                courseid = str(input("Enter courseid(CI000,cs01,EE08,MECH05) :-"))
                insert = f"insert into students values('{rollno}','{name}',{age},'{sex}','{courseid}')"
                cursor.execute(insert)
                mycon.commit()
            except:
                print("You have entered wrong details")
                continue

        if select == 2:
            try:
                rollno = str(input("Enter student rollno"))
                cursor.execute(f"delete from students where rollno='{rollno}'")
                mycon.commit()
            except:
                print("you have entered the wrong rollno")
                continue

        if select == 3:
            try:
                print("what do you wanna update??")
                update = str(input("enter (sex/name/courseid/age) :- "))
                updated = str(input("enter the detail to be updated :- "))
                rollno = str(input("Enter student rollno"))
                if update == 'age':
                    cursor.execute(f"update students set {update} = {updated} where rollno = '{rollno}'")
                    mycon.commit()

                cursor.execute(f"update students set {update} = '{updated}' where rollno = '{rollno}'")
                mycon.commit()
            except:
                print("you have entered details wrong")

        if select == 4:
            cursor.execute("select * from students")
            data = cursor.fetchall()
            for row in data:
                print(row)

    if select == 2:
        print(
            "select  \n1.insert new lecturer \n2.Delete a lecturer \n3.update a lecturer details\n4.display all lecturers\n")
        select = int(input("select a number :-"))

        if select == 1:
            try:
                Lid = str(input("Enter Lid :-"))
                name = str(input("Enter name :-"))
                subject = str(input("Enter subject :-"))
                age = int(input("Enter age :-"))
                sex = str(input("Enter sex(M/F) :-"))
                courseid = str(input("Enter courseid :-"))
                insert = f"insert into lecturers values('{Lid}', '{name}', '{subject}', {age}, '{sex}', '{courseid}')"
                cursor.execute(insert)
                mycon.commit()
            except:
                print("you have entered the wrong details")
        if select == 2:
            try:
                Lid = str(input("Enter lecturer Lid"))
                cursor.execute(f"delete from lecturers where Lid='{Lid}'")
                mycon.commit()
            except:
                print("you have entered the wrong rollno")
                continue

        if select == 3:
            try:
                print("what do you wanna update??")
                update = str(input("enter (subject/sex/name/courseid/age) :- "))
                updated = str(input("enter the detail to be updated :- "))
                Lid = str(input("Enter lecturer Lid :- "))
                if update == 'age':
                    cursor.execute(f"update lecturers set {update} = {updated} where Lid = '{Lid}'")
                    mycon.commit()

                cursor.execute(f"update lecturers set {update} = '{updated}' where Lid = '{Lid}'")
                mycon.commit()
            except:
                print("you have entered details wrong")

        if select == 4:
            cursor.execute("select * from lecturers")
            data = cursor.fetchall()
            for row in data:
                print(row)

    if select == 3:
        print(
            "select  \n1.insert new subject \n2.Delete a subject \n3.update a subject details\n4.display all subject\n")
        select = int(input("select a number :-"))
        if select == 1:
            try:
                subjectid = str(input("enter the subjectid :-"))
                subjectname = str(input("enter the subject name :-"))
                insert = f"insert into subjects values('{subjectid}','{subjectname}')"
                cursor.execute(insert)
                mycon.commit()

            except:
                print("you have entered the wrong details")

        if select == 2:
            try:
                subjectid = str(input("enter the subjectid"))
                cursor.execute(f"delete from subjects where subjectid = '{subjectid}'")
                mycon.commit()

            except:
                print("you have entered the wrong details")

        if select == 3:
            try:
                subjectid = str(input("enter thr subjectid"))
                update = str(input("enter the updated subjectname :-"))
                cursor.execute(f"update subjects set subjectname = '{update}' where subjectid = '{subjectid}'")
                mycon.commit()

            except:
                print("you have entered the wrong subject id")

        if select == 4:
            cursor.execute("select * from subjects")
            data = cursor.fetchall()
            for row in data:
                print(row)

    if select == 4:
        print(
            "select  \n1.insert new course \n2.Delete a course \n3.update a course details\n4.display all courses\n")
        select = int(input("select a number :-"))
        if select == 1:
            try:
                courseid = str(input("enter the courseid :-"))
                course = str(input("enter the course name :-"))
                feestructure = int(input("enter fee structure :-"))
                insert = f"insert into courses values('{courseid}','{course}',{feestructure})"
                cursor.execute(insert)
                mycon.commit()

            except:
                print("you have entered the wrong details")

        if select == 2:
            try:
                courseid = str(input("enter the courseid :"))
                cursor.execute(f"delete from courses where courseid ='{courseid}'")
                mycon.commit()
            except:
                print("invalid courseid!!!!!!!!!!!!")

        if select == 3:
            try:
                print("what do you wanna update??")
                update = str(input("enter (course/feestructure) :- "))
                updated = str(input("enter the detail to be updated :- "))
                Lid = str(input("Enter lecturer courseid :- "))

                cursor.execute(f"update courses set {update} = '{updated}' where courseid = '{Lid}'")
                mycon.commit()
            except:
                print("you have entered details wrong")

        if select == 4:
            cursor.execute("select * from courses")
            data = cursor.fetchall()
            for row in data:
                print(row)

    if select == 5:
        print(
            "select  \n1.insert new student \n2.Delete a student \n3.update a student details\n4.display all students\n")
        select = int(input("select a number"))
        if select == 1:
            try:
                rollno = str(input("Enter student rollno :-"))
                courseid = str(input("Enter courseid(CI000,cs01,EE08,MECH05) :-"))
                totalfees = int(input("enter total fees"))
                paid = int(input("enter the paid amount: "))
                balance = totalfees - paid
                insert = f"insert into fees values('{rollno}','{courseid}',{totalfees},{paid},{balance})"
                cursor.execute(insert)
                mycon.commit()
            except:
                print("You have entered wrong details")
                continue

        if select == 2:
            try:
                rollno = str(input("Enter student rollno :-"))
                cursor.execute(f"delete from fees where rollno='{rollno}'")
                mycon.commit()
            except:
                print("You have entered wrong details")
                continue

        if select == 3:
            try:
                rollno = str(input("Enter student rollno :-"))
                paid = int(input("enter paid amount :"))
                cursor.execute(f"select * from fees where rollno='{rollno}'")
                data = cursor.fetchone()
                totalfees = data[3]
                balance = totalfees - paid
                print(totalfees)
                print(balance)
                cursor.execute(f"update fees set paid={paid} where rollno='{rollno}'")
                mycon.commit()
                cursor.execute(f"update fees set balance={balance} where rollno='{rollno}'")
                mycon.commit()

            except:
                print("you have entered wrong details")

        if select == 4:
            cursor.execute("select * from fees")
            data = cursor.fetchall()
            for row in data:
                print(row)

    if select == 6:
        print("\n\n*************THANK YOU**********************")
        exit()

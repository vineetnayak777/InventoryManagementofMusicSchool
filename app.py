import mysql.connector

from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = b'Vineet'

mydb = mysql.connector.connect(host="localhost", user="root", passwd="7019252847", database="sadhu")
c = mydb.cursor()
c.execute("USE sadhu;")

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

#For Student Table
@app.route('/add_student')
def render_add_student_page():
    return render_template("add_student.html")

@app.route('/add_student_button', methods=['POST'])
def add_student_record():
    try:
        Name = request.form.get("Name")
        Reg_No = request.form.get("Reg_No")
        Level = request.form.get("Level")
        Contact = request.form.get("Contact")
        Date_Joined = request.form.get("Date_Joined")
        Fees_Id = request.form.get("Fees_Id")
        Age = request.form.get("Age")

        c.execute("""
                    INSERT INTO Students(Name, Reg_No, Level, Contact, Date_Joined, Fees_Id, Age) VALUES(%s,%s,%s,%s,%s,%s,%s)
                    """, (Name, Reg_No, Level, Contact, Date_Joined, Fees_Id, Age))
        mydb.commit()
        flash('Successfully Inserted Data into Student Table')
        return render_template("output.html", msg ="New Student added Successfully")
    except:
        mydb.rollback()
        return render_template("output.html", msg ="Failed to add new student, Check the table before inserting values...")

@app.route('/view_students')
def render_all_students():
    try:
        c.execute("""SELECT * FROM Students""")
        student_query=c.fetchall()

        return render_template("student_details.html", students=student_query)
    except:
        return render_template("output.html", msg ="Error in rendering student details")

@app.route('/delete_student_button', methods=['POST'])
def delete_student():
    try:
        Reg_No = request.form.get("Reg_No")

        c.execute("""
                DELETE FROM Students WHERE Reg_No = %s
                """,(Reg_No,))
        mydb.commit()
        return render_template("output.html", msg ="Student Record deleted successfully")
    except:
        mydb.rollback()
        return render_template("output.html", msg ="Error in deleting a student")

#For Level table
@app.route('/add_level')
def render_add_levels_page():
    return render_template("add_levels.html")

@app.route('/add_level_button', methods=['POST'])
def add_level_record():
    try:

        Level_id = request.form.get("Level_id")
        Name = request.form.get("Name")
        Actual_Name = request.form.get("Actual_Name")

        c.execute("""
                    INSERT INTO Levels(Level_id,Name, Actual_Name) VALUES(%s,%s,%s)
                    """, (Level_id,Name,Actual_Name,))
        mydb.commit()
        return render_template("output.html", msg ="Successfully added a Level data")
    except:
        mydb.rollback()
        return render_template("output.html", msg ="Error in adding level data")

@app.route('/view_levels')
def render_all_levels():
    try:
        c.execute("""SELECT * FROM Levels""")
        level_query=c.fetchall()

        return render_template("level_details.html", levels=level_query)
    except:
        return render_template("output.html", msg ="Error in rendering Level")

@app.route('/delete_level_button', methods=['POST'])
def delete_levels():
    try:
        Level_id = request.form.get("Level_id")

        c.execute("""
                DELETE FROM levels WHERE level_id=%s
                """,(Level_id,))
        mydb.commit()
        return render_template("output.html", msg ="Level deleted successfully")
    except:
        mydb.rollback()
        return render_template("output.html", msg ="Error in level deletion operation")  
    

#For Raag
@app.route('/add_ragas')
def render_add_ragas_page():
    return render_template("add_ragas.html")


@app.route('/add_ragas_button', methods=['POST'])
def add_ragas_record():
    try:
        Raga_Name = request.form.get("Raga_Name")
        Aaroh = request.form.get("Aaroh")
        Avaroh = request.form.get("Avaroh")

        c.execute("""
                    INSERT INTO Ragas(Raga_Name, Aaroh, Avaroh) VALUES(%s,%s,%s)
                    """, (Raga_Name, Aaroh, Avaroh))
        mydb.commit()
        return render_template("output.html", msg ="Successfully added a raga")
    except:
        mydb.rollback()
        return render_template("output.html", msg ="Failed to add a raga, Check the value of table before inserting again!")


@app.route('/view_ragas')
def render_all_ragas():
    try:

        c.execute("""SELECT * FROM Ragas""")
        Ragas_query = c.fetchall()
        return render_template("ragas_detail.html", ragas=Ragas_query)
    except:
        return render_template("output.html", msg ="Error in rendering Raga Details")

@app.route('/delete_raga_button', methods=['POST'])
def delete_raga():
    try:
        Raga_Name = request.form.get("Raga_Name")
        c.execute("""
                DELETE FROM Ragas WHERE Raga_Name = %s
                """,(Raga_Name,))
        mydb.commit()
        return render_template("output.html", msg ="Raga Deleted Successfully")
    except:
        mydb.rollback()
        return render_template("output.html", msg ="Error in deleting a Raga")

#For Examination
@app.route('/add_exam')
def render_add_exam_page():
    return render_template("add_examination_details.html")


@app.route('/add_exam_button', methods=['POST'])
def add_exam_record():
    try:
        E_S_No = request.form.get("E_S_No")
        Student_Reg_No = request.form.get("Student_Reg_No")
        Status = request.form.get("Status")
        Date_of_Examination = request.form.get("Date_of_Examination")

        c.execute("""
                    INSERT INTO Examination(E_S_No,Student_Reg_No, Status, Date_of_Examination) VALUES(%s,%s,%s,%s)
                    """, (E_S_No, Student_Reg_No, Status, Date_of_Examination))
        mydb.commit()
        return render_template("output.html", msg ="Exam data added successfully")
    except:
        mydb.rollback()
        return render_template("output.html", msg ="Error in adding Exam details")

@app.route('/view_exams')
def render_all_exam():
    try:

        c.execute("""SELECT * FROM Examination""")
        exam_query = c.fetchall()

        return render_template("exam_details.html", exams=exam_query)
    except:
        return render_template("output.html", msg ="Error in rendering Examination Details")

@app.route('/delete_exam_button', methods=['POST'])
def delete_exams():
    try:
        E_S_No = request.form.get("E_S_No")

        c.execute("""
                DELETE FROM Examination WHERE E_S_No = %s
                """,(E_S_No,))
        mydb.commit()
        return render_template("output.html", msg ="Examination data deleted successfully")
    except:
        mydb.rollback()
        return render_template("output.html", msg ="Error in deletion of Examination data")

@app.route('/update_exam_button', methods=['POST'])
def update_exams():
    try:
        E_S_No = request.form.get("E_S_No")
        Student_Reg_No = request.form.get("Student_Reg_No")
        Status = request.form.get("Status")

        c.execute("""
                Update Examination set Status = %s, Student_Reg_No = %s WHERE E_S_No = %s
                """,(Status, Student_Reg_No, E_S_No,))
        mydb.commit()
        return render_template("output.html", msg ="Status updated successfully")
    except:
        mydb.rollback()
        return render_template("output.html", msg ="Error in Updating Examination Status")

#For events
@app.route('/add_events')
def render_add_event_page():
    return render_template("add_event_details.html")


@app.route('/add_event_button', methods=['POST'])
def add_event_record():
    try:
        S_No = request.form.get("S_No")
        Agency_Id = request.form.get("Agency_Id")
        Student_Reg_No = request.form.get("Student_Reg_No")
        Place = request.form.get("Place")
        Date_of_Event = request.form.get("Date_of_Event")

        c.execute("""
                    INSERT INTO Events(S_No,Agency_Id, Student_Reg_No, Place, Date_of_Event) VALUES(%s,%s,%s,%s,%s)
                    """, (S_No, Agency_Id, Student_Reg_No, Place, Date_of_Event))
        mydb.commit()
        return render_template("output.html", msg ="Successfully added a Event Details")
    except:
        mydb.rollback()
        return render_template("output.html", msg ="Failed to insert Event Details")

@app.route('/view_events')
def render_all_events():
    try:

        c.execute("""SELECT * FROM Events""")
        event_query = c.fetchall()

        return render_template("event_details.html", events=event_query)
    except:
        return render_template("output.html", msg ="Error in rendering Events")

@app.route('/delete_event_button', methods=['POST'])
def delete_events():
    try:
        S_No = request.form.get("S_No")
        c.execute("""
                DELETE FROM Events WHERE S_No = %s
                """,(S_No,))
        mydb.commit()
        return render_template("output.html", msg ="Event deleted successfully")
    except:
        mydb.rollback()
        return render_template("output.html", msg ="Error in deletion of an Event")

#For Level_Ragas table
@app.route('/add_level_raga')
def render_add_level_raga_page():
    return render_template("add_level_raga.html")


@app.route('/add_level_raga_button', methods=['POST'])
def add_level_raga_record():
    try:
        Level_id = request.form.get("Level_id")
        Raga_name = request.form.get("Raga_name")

        c.execute("""
                    INSERT INTO Level_Ragas(Level_id, Raga_name) VALUES(%s,%s)
                    """, (Level_id, Raga_name,))
        mydb.commit()
        return render_template("output.html", msg ="Successfully added a level_raga")
    except:
        mydb.rollback()
        return render_template("output.html", msg ="Failed to insert level_raga")


@app.route('/view_level_raga')
def render_all_level_raga():
    try:
        c.execute("""SELECT * FROM Level_Ragas""")
        level_raga_query = c.fetchall()
        return render_template("level_raga_details.html", level_ragas=level_raga_query)
    except:
        return render_template("output.html", msg ="Error in rendering level_raga data")

@app.route('/delete_level_raga_button', methods=['POST'])
def delete_level_raga():
    try:
        Level_id = request.form.get("Level_id")
        Raga_name = request.form.get("Raga_name")
        c.execute("""
                DELETE FROM level_ragas WHERE level_id=%s and Raga_name = %s
                """,(Level_id, Raga_name))
        mydb.commit()
        return render_template("output.html", msg ="Level_Raga deleted successfully")
    except:
        mydb.rollback()
        return render_template("output.html", msg ="Error in deleting Level_Raga")

#For Agencies table
@app.route('/add_agency')
def render_agency_page():
    return render_template("add_agency_details.html")

@app.route('/add_agency_button', methods=['POST'])
def add_agency_record():
    try:

        Agency_id = request.form.get("Agency_id")
        Agency_name = request.form.get("Agency_name")
        Agency_Place = request.form.get("Agency_Place")

        c.execute("""
                    INSERT INTO Agencies(Agency_id, Agency_name, Agency_Place) VALUES(%s,%s,%s)
                    """, (Agency_id, Agency_name, Agency_Place))
        mydb.commit()
        return render_template("output.html", msg ="Successfully added an Agency")
    except:
        mydb.rollback()
        return render_template("output.html", msg ="Error in deleting Agency detail")

@app.route('/view_agencies')
def render_all_agencies():
    try:
        c.execute("""SELECT * FROM Agencies""")
        Agencies_query = c.fetchall()

        return render_template("agency_details.html", agencies=Agencies_query)
    except:
        return render_template("output.html", msg ="Error Rendering the Agency Table")

@app.route('/delete_agency_button', methods=['POST'])
def delete_agency():
    try:
        Agency_id = request.form.get("Agency_id")
        c.execute("""
                DELETE FROM Agencies WHERE Agency_id = %s
                """,(Agency_id,))
        mydb.commit()
        return render_template("output.html", msg ="Agency deleted successfully")
    except:
        mydb.rollback()
        return render_template("output.html", msg ="Error in deleting Agent")

#For Fees Payment
@app.route('/add_fees_payment')
def render_add_fees_payment_page():
    return render_template("add_fees_payment.html")

@app.route('/add_fees_payment_button', methods=['POST'])
def add_fees_payment_record():
    try:
        S_No = request.form.get("S_No")
        Student_Reg_No = request.form.get("Student_Reg_No")
        Date_of_Payment = request.form.get("Date_of_Payment")
        Amount = request.form.get("Amount")

        c.execute("""
                    INSERT INTO Fees_Payment(S_No, Student_Reg_No, Date_of_Payment, Amount) VALUES(%s,%s,%s,%s)
                    """, (S_No, Student_Reg_No, Date_of_Payment, Amount,))
        mydb.commit()
        return render_template("output.html", msg = "Fees Payment added Successfully")
    except:
        return render_template("output.html", msg = "Failed to insert Fees Payment Details")

@app.route('/view_fees_payment')
def render_all_fees_payment():

    c.execute("""SELECT * FROM Fees_Payment""")
    fees_query = c.fetchall()
    return render_template("fees_payment_details.html", fees=fees_query)

@app.route('/delete_fees_payment_button', methods=['POST'])
def delete_fees_payment():
    try:

        S_No = request.form.get("S_No")

        c.execute("""
                DELETE FROM Fees_Payment WHERE S_No=%s
                """,(S_No,))
        mydb.commit()
        return render_template("output.html", msg = "Fees Payment Data Deleted Successfully")
    except:
        mydb.rollback()
        return render_template("output.html", msg = "Error in Deletion Operation")

#For Fees
@app.route('/add_fees')
def render_add_fees_page():
    return render_template("add_fees.html")

@app.route('/add_fees_button', methods=['POST'])
def add_fees_record():
    try:
        Fees_id = request.form.get("Fees_id")
        Monthly_Fees = request.form.get("Monthly_Fees")
        Admission_Fees = request.form.get("Admission_Fees")

        c.execute("""
                    INSERT INTO Fees(Fees_id, Monthly_Fees, Admission_Fees) VALUES(%s,%s,%s)
                    """, (Fees_id, Monthly_Fees, Admission_Fees,))
        mydb.commit()
        return render_template("output.html", msg = "Fees Data added Successfully")
    except:
        mydb.rollback()
        return render_template("output.html", msg = "Failed to add Fees details")

@app.route('/view_fees')
def render_all_fees():

    c.execute("""SELECT * FROM Fees""")
    Fees_query = c.fetchall()
    return render_template("fees_detail.html", fees=Fees_query)

@app.route('/update_fees_button', methods=['POST'])
def update_fees():
    try:
        Fees_Id = request.form.get("Fees_Id")
        Monthly_Fees = request.form.get("Monthly_Fees")
        Admission_Fees = request.form.get("Admission_Fees")

        c.execute("""
                Update Fees set Monthly_Fees = %s, Admission_Fees = %s where Fees_id = %s
                """,(Monthly_Fees,Admission_Fees,Fees_Id,))
        mydb.commit()
        return render_template("output.html", msg = "Fees Data Updated Successfully")
    except:
        mydb.rollback()
        return render_template("output.html", msg = "Error in Data Updation")

@app.route('/delete_fees_button', methods=['POST'])
def delete_fees():
    try:
        Fees_id = request.form.get("Fees_id")

        c.execute("""
                DELETE FROM Fees WHERE Fees_id=%s
                """,(Fees_id,))
        mydb.commit()
        return render_template("output.html", msg = "Fees Data Deleted Successfully")
    except:
        mydb.rollback()
        return render_template("output.html", msg = "Error in Fees Deletion Operation")

@app.route('/retrieve_student_fees_button', methods=['POST'])
def retrieve_fees():

    Student_Reg_No = request.form.get("Student_Reg_No")

    c.execute("""
            CALL Fees_History(%s);
            """,(Student_Reg_No,))
    retrieve_query = c.fetchall()

    return render_template("retrieve_fees_detail.html", retrieve_querys=retrieve_query)

@app.route('/view_student_association_years')
def view_student_association():

    c.execute("select * from student_association;")
    view_association = c.fetchall()
    return render_template("view_student_association.html", view_associations = view_association)

@app.route('/view_student_events_details')
def view_student_event():

    c.execute("select * from student_event_detail;")
    view_student_event_query = c.fetchall()
    return render_template("view_student_events.html", view_student_events = view_student_event_query)

@app.route('/add_data')
def render_add_data_page():
    return render_template("add_data.html")

@app.route('/view_data')
def render_view_data_page():
    return render_template("view_data.html")

@app.route('/misc_data')
def render_view_misc_data_page():
    return render_template("misc_data.html")

@app.route('/retrieve_raga_from_lr_button', methods=['POST'])
def retrieve_raga_details_level_raga():

    Level_id = request.form.get("Level_id")

    c.execute("""
            CALL extract_raag_details(%s);
            """,(Level_id,))
    retrieve_raga_from_lr = c.fetchall()

    return render_template("retrieve_raga_from_lr_detail.html", retrieve_raga_from_lr_querys=retrieve_raga_from_lr)

if __name__ == "__main__":
    app.run(debug=True)
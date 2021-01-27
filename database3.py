import mysql.connector

def init_db():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="7019252847", database="sadhu")
    c = mydb.cursor()
    c.execute("USE sadhu;")

    c.execute("""
                CREATE TABLE Levels(
                    Level_id int primary key,
                    Name varchar(15),
                    Actual_Name varchar(20)
                );
                """)
    mydb.commit()

    c.execute("""
            CREATE TABLE Fees(
                Fees_id int primary key,
                Monthly_Fees int,
                Admission_Fees int
            );
            """)
    mydb.commit()

    c.execute("""
                CREATE TABLE Students(
                    Name varchar(50),
                    Reg_No char(8) PRIMARY KEY check(Reg_No like '__HIN___'),
                    Level int,
                    Contact bigint,
                    Date_Joined DATE,
                    Fees_id int,
                    Age int,
                    Foreign key(Level) references Levels(Level_id),
                    Foreign key(Fees_id) references Fees(Fees_id)
                );
                """)
    mydb.commit()


    c.execute("""
                CREATE TABLE Ragas(
                    Raga_Name varchar(15) primary key,
                    Aaroh varchar(60),
                    Avaroh varchar(60)
                );
                """)
    mydb.commit()

    c.execute("""
                CREATE TABLE Examination(
                    E_S_No int Primary Key,
                    Student_Reg_No char(8),
                    Status char(10),
                    Date_of_Examination Date,
                    Foreign Key(Student_Reg_No) references Students(Reg_No) on delete cascade
                );
                """)

    mydb.commit()

    c.execute("""
                CREATE Table Agencies(
                    Agency_Id int primary key,
                    Agency_name varchar(20),
                    Agency_Place varchar(20)
                );
                """)

    mydb.commit()

    c.execute("""
                CREATE TABLE Events(
                    S_No int primary key,
                    Agency_Id int,
                    Student_Reg_No char(8),
                    Place varchar(30),
                    Date_of_Event Date,
                    Foreign Key(Student_Reg_No) references Students(Reg_No) on delete cascade,
                    Foreign Key(Agency_Id) references Agencies(Agency_Id) on delete set null
                );
                """)

    mydb.commit()

    c.execute("""
                CREATE TABLE Level_Ragas(
                    Level_id int,
                    Raga_name varchar(15),
                    Primary key(Level_id, Raga_name),
                    Foreign key(Level_id) references Levels(Level_id) on delete cascade,
                    Foreign key(Raga_name) references Ragas(Raga_name) on delete cascade
                );
                """)
    mydb.commit()

    c.execute("""
                CREATE TABLE Fees_Payment(
                    S_No int primary key,
                    Student_Reg_No char(8),
                    Date_of_Payment Date,
                    Amount int,
                    Foreign Key (Student_Reg_No) references Students(Reg_No) on delete cascade
                );
                """)
    mydb.commit()
    #Triggerer
    c.execute("""
                CREATE DEFINER = CURRENT_USER TRIGGER `sadhu`.`examination_AFTER_UPDATE` AFTER UPDATE ON `examination` FOR EACH ROW
                BEGIN
                    IF (new.status = "Passed") THEN
                        UPDATE Students Set Level = Level+1 where Reg_No = (select Student_Reg_No from Examination where Student_Reg_No = new.Student_Reg_No);
                    END IF;
                END
            """)
    mydb.commit()
    #Stored Procedure   
    c.execute("""
                CREATE DEFINER=`root`@`localhost` PROCEDURE `Fees_History`(IN Stud_Reg_No Char(8))
                BEGIN
                    Select Student_Reg_No, sum(Amount) from Fees_Payment where Student_Reg_No = Stud_Reg_No;
                END;
            """)
    mydb.commit()

    c.execute("""
                CREATE FUNCTION `no_of_years` (date1 date)
                RETURNS INTEGER DETERMINISTIC
                BEGIN
                    declare date2 date;
                    Select current_date()into date2;
                RETURN year(date2)-year(date1);
                END;
        """)
    mydb.commit()

    c.execute("""
                CREATE 
                    ALGORITHM = UNDEFINED 
                    DEFINER = `root`@`localhost` 
                    SQL SECURITY DEFINER
                VIEW `sadhu`.`student_association` AS
                    SELECT 
                        `sadhu`.`students`.`Name` AS `Name`,
                        NO_OF_YEARS(`sadhu`.`students`.`Date_Joined`) AS `no_of_years(Date_Joined)`
                    FROM
                        `sadhu`.`students`
                    ORDER BY `sadhu`.`students`.`Reg_No`;
        """)
    mydb.commit()
    c.execute("""
                CREATE
                    ALGORITHM = UNDEFINED 
                    DEFINER = `root`@`localhost` 
                    SQL SECURITY DEFINER
                VIEW `sadhu`.`student_event_detail` AS
                    SELECT 
                        `sadhu`.`students`.`Name` AS `name`,
                        `sadhu`.`students`.`Reg_No` AS `Reg_No`,
                        `sadhu`.`events`.`Date_of_Event` AS `date_of_event`
                    FROM
                        (`sadhu`.`students`
                        JOIN `sadhu`.`events`)
                    WHERE
                        (`sadhu`.`students`.`Reg_No` = `sadhu`.`events`.`Student_Reg_No`)
                    GROUP BY `sadhu`.`students`.`Reg_No`;
            """)
    mydb.commit()
    c.execute("""
            CREATE PROCEDURE `extract_raag_details` (IN Lev_Id int)
            BEGIN
                SELECT Avaroh, Avaroh from ragas, level_ragas  where Raga_Name in (select Raga_Name from level_ragas where level_id = Lev_Id);
            END
        """)
    mydb.commit()
init_db()
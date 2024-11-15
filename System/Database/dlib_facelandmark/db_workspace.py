import sqlite3
import time

basepath = "D:\\OneDrive - Asia Pacific University\\Degree Year 3\\Sem 2\\Final Year Project\\Deepfake Detection System\\Database\\"
database_name = "deepfake_system_db"

connection = sqlite3.connect(basepath + database_name)

cursor = connection.cursor()

# Create user table
create_statement_user = """
                        CREATE TABLE IF NOT EXISTS user (
                            email TEXT PRIMARY KEY,
                            password TEXT,
                            full_name TEXT
                        );
                        """
# Create OTP table
create_otp_table = """
                    CREATE TABLE IF NOT EXISTS otp_records (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        email TEXT NOT NULL,            
                        otp TEXT NOT NULL,             
                        expiry_time DATETIME NOT NULL,
                        FOREIGN KEY(email) REFERENCES user(email)             
                    );
                    """
# Create detection table
create_detection_table = """
                    CREATE TABLE IF NOT EXISTS detection (
                        detection_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        upload_date DATETIME NOT NULL,            
                        upload_time DATETIME NOT NULL,             
                        completion_time DATETIME NOT NULL,
                        source TEXT NOT NULL,             
                        user_id TEXT NOT NULL,
                        FOREIGN KEY(user_id) REFERENCES user(email)          
                    );
                    """

create_video_table = """
                    CREATE TABLE IF NOT EXISTS video (
                        video_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        file_path TEXT NOT NULL,            
                        file_name TEXT NOT NULL,             
                        status TEXT NOT NULL,
                        result TEXT NOT NULL,             
                        ai_frame BLOB NULL,
                        detection_id INTEGER NOT NULL,
                        FOREIGN KEY(detection_id) REFERENCES detection(detection_id)          
                    );
                    """

create_notification_table = """
                        CREATE TABLE IF NOT EXISTS notification (
                            notification_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            content TEXT NOT NULL,
                            created_date DATETIME NOT NULL,            
                            created_time DATETIME NOT NULL, 
                            user_id TEXT NOT NULL,
                            FOREIGN KEY(user_id) REFERENCES user(email) 
                        )
                        """

query = f"""
            SELECT t1.upload_date, t1.upload_time, t1.completion_time, t1.source, t2.total_video, CAST(COALESCE(t2.num_deepfake, 0)) AS STRING AS num_deepfake , t1.detection_id FROM 
            (SELECT upload_date, upload_time, completion_time, source,  detection_id 
                from detection WHERE user_id = 'tp060575@mail.apu.edu.my') t1
            INNER JOIN
            (SELECT detection_id, CAST(COUNT(detection_id) AS text) AS total_video, SUM(CASE WHEN result = 'Fake' THEN 1 ELSE 0 END) AS num_deepfake FROM video GROUP BY detection_id) t2
            ON t1.detection_id = t2.detection_id
            ORDER BY t1.detection_id DESC
        """


# cursor.execute(create_video_table)
# cursor.execute("INSERT INTO user VALUES ('test12', 'test123', 'ImTest')")
# cursor.execute("INSERT INTO otp_records (email, otp, expiry_time) VALUES ('test12', 'test123', 'ImTest')")

# cursor.execute("SELECT d.user_id, v.result  from detection d INNER JOIN video v on d.detection_id = v.detection_id", ())

# cursor.execute("""SELECT d.upload_date, d.upload_time, d.completion_time, d.source, d.detection_id, v.result 
#                     from detection d INNER JOIN video v ON d.detection_id = v.detection_id 
#                     WHERE d.user_id = 'test' ORDER BY d.upload_date DESC, d.upload_time DESC""")
query = """SELECT total, total_fake, CONCAT(ROUND(((total - total_fake) / CAST(total as FLOAT))*100,2),'%'), CONCAT(ROUND((total_fake / CAST(total as FLOAT))*100,2),'%') FROM
            (SELECT COUNT(*) AS total, SUM(CASE WHEN result = 'Fake' THEN 1 ELSE 0 END) AS total_fake from video v 
            INNER JOIN detection d ON v.detection_id = d.detection_id 
            WHERE d.user_id = 'tp060575@mail.apu.edu.my' AND d.source = '') """

query = """SELECT source, count(source) as total from video v 
            INNER JOIN detection d ON v.detection_id = d.detection_id 
            WHERE d.user_id = 'tp060575@mail.apu.edu.my'
            GROUP BY source
            ORDER BY total DESC
            LIMIT 2"""

query = """SELECT month, ROUND((SUM(CASE WHEN result = 'Fake' THEN 1 ELSE 0 END)/CAST(COUNT(month) as FLOAT))*100,2) FROM
            (SELECT CASE strftime('%m', d.upload_date)
                    WHEN '01' THEN 'Jan'
                    WHEN '02' THEN 'Feb'
                    WHEN '03' THEN 'Mar'
                    WHEN '04' THEN 'Apr'
                    WHEN '05' THEN 'May'
                    WHEN '06' THEN 'Jun'
                    WHEN '07' THEN 'Jul'
                    WHEN '08' THEN 'Aug'
                    WHEN '09' THEN 'Sep'
                    WHEN '10' THEN 'Oct'
                    WHEN '11' THEN 'Nov'
                    WHEN '12' THEN 'Dec'
                END AS month, v.result
                FROM detection d INNER JOIN video v ON d.detection_id = v.detection_id ) t
                GROUP BY month"""

query = f"""SELECT source, count(source) as total from video v 
                    INNER JOIN detection d ON v.detection_id = d.detection_id 
                    WHERE d.user_id = 'tp060575@mail.apu.edu.my' AND result = 'Fake'
                    GROUP BY source
                    ORDER BY total DESC
                    LIMIT 5
                    """
query = "UPDATE DETECTION SET upload_date = '2024-06-01' WHERE detection_id = 18"
# DELETE FROM DETECTION WHERE detection_id = 27
# cursor.execute("SELECT * FROM DETECTION ORDER BY detection_id")
cursor.execute(query)

result = cursor.fetchall()

# for source in result:
#     print(source[0])


print((result))
connection.commit()

connection.close()

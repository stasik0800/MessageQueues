# MessageQueues

Using :
Python – 2.7 
modules  - pika , json , sqlite3 , dicttoxml , pandas

Python fiels description :
send.py = send request to rabbit . Please provide values db_path and data_format inside the script. 
Receive.py = receive request from send.py.
db.py = connections to sqlite db.
format.py = methods returning format type.
questions.py = hold queries related  to questions.
Main.py = main program. 

Steps to run:
1) run send.py with supplied parameters.
2) run reveive.py.


 
  :כל קובץ מכיל מספר שאלה 
:שאלות פירוט
לכל שיר נמצא את מחבר/מלחין שלו ואת סוג שלו  - q1

 מצא רשימת לקוחות הכוללת שם , טלפון, אימייך , כתובת משורשרת , וכמה רכישות עשה.- q2  

כמה דומנים שונים של איימיל יש בכל מדינה  - q3
נלקחו לקוחות ומעסיקים*

לכל מדינה כמה דיסקים נמכרו - q4

לכל מדינה מה הדיסק הכי נמכר ומה מכירות ממנו . - q5
דיסק = אלבום

   מה הדיסק הכי נמכר בארה’’ב החל משנת 2011- q6
דיסק = אלבום

 רשימת לקוחות שחסר בהזמנה שלהם 2 שדות או יותר- q7 
התייחסות רק לטבלת לקוחות


MessageQueues

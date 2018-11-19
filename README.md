# MessageQueues

Using :
1) Ubuntu 16.04
2) rabbitmq:3-management  running through docker 
3) Python – 2.7 
4) modules  - pika (v 0.12 ), json , sqlite3 , dicttoxml (v 1.7.4) , pandas ( v 0.23.4)

Python fiels description :
1) send.py = send request to rabbit . Please provide values db_path and data_format inside the script
2) Receive.py = receive request from sendpy.
3) db.py = connections to sqlite db.
4) format.py = methods returning format type.
5) questions.py = hold queries related  to questions.
6) Main.py = main program. 


Steps to run:
1) first run send.py with supplied parameters.
2) second run reveive.py for getting result.

Output:
1) for each question (q1...7) will create file xml,csv,json

 
 
  :כל קובץ מכיל מספר שאלה 

:שאלות פירוט והנחות

לכל שיר נמצא את מחבר/מלחין שלו ואת סוג שלו  - q1

 מצא רשימת לקוחות הכוללת שם , טלפון, אימייל , כתובת משורשרת , וכמה רכישות עשה.- q2  

כמה דומנים שונים של איימיל יש בכל מדינה  - q3

נלקחו לקוחות ומעסיקים*

לכל מדינה כמה דיסקים נמכרו - q4

לכל מדינה מה הדיסק הכי נמכר ומה מכירות ממנו  - q5

דיסק = אלבום

   מה הדיסק הכי נמכר בארה’’ב החל משנת 2011- q6
   
דיסק = אלבום

 רשימת לקוחות שחסר בהזמנה שלהם 2 שדות או יותר- q7
 
התייחסות רק לטבלת לקוחות



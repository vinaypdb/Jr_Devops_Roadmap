import shutil
import smtplib

THRESHOLD = 80  # percent

total, used, free = shutil.disk_usage("/")

percent_used = (used / total) * 100

if percent_used > THRESHOLD:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login("vinaypedapuri@gmail.com", "yourpassword")
        message = f"Subject: Disk Alert\n\nDisk usage is {percent_used:.2f}%"
        server.sendmail("youremail@gmail.com", "admin@example.com", message)

import smtplib
import datetime as dt

# SMTP - Simple Mail Transfer Protocol
# I'm creating a new connection, basically a way to be able to connect to the email provider's SMTP email server

my_email = "mirela.manta23@gmail.com"  # testing email
password = "obqklcpwktzjrepz"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    # the line above will make the connection secure
    # TLS stands for Transport Layer Security
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="tibi.zepter@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)
print(year)   # type = int
print(now)   # type = datetime object


date_of_birth = dt.datetime(year=1999, month=11, day=18, hour=4)
print(date_of_birth)
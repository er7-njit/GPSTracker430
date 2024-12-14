import time
from datetime import datetime
import pytz
import board
import busio
import adafruit_gps
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import serial

# Serial connection for GPS module
uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=10)

# Create a GPS module instance
gps = adafruit_gps.GPS(uart, debug=False)

# GPS initialization commands
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
gps.send_command(b"PMTK220,1000")

# Timezone setup
eastern = pytz.timezone('US/Eastern')

# Email configuration
EMAIL_SENDER = "rj65@njit.edu"
EMAIL_PASSWORD = "tdqq jdqy plop avdu"
EMAIL_RECEIVER = "rj65@njit.edu"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

# Function to send an email with GPS data
def send_email(latitude, longitude, timestamp, speed_kmh=None):
    # Create the email content
    message = MIMEMultipart()
    message["From"] = EMAIL_SENDER
    message["To"] = EMAIL_RECEIVER
    message["Subject"] = "GPS Location Fix"

    # Email body
    email_content = f"""
    GPS Location Fix:
    Timestamp (Eastern Time): {timestamp}
    Latitude: {latitude:.6f} degrees
    Longitude: {longitude:.6f} degrees
    Speed: {speed_kmh if speed_kmh else 'N/A'} km/h
    """
    message.attach(MIMEText(email_content, "plain"))

    # Secure SSL context
    context = ssl.create_default_context()

    # Sending the email
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, message.as_string())

    print("Email sent successfully!")

# Main loop
last_print = time.monotonic()
email_sent = False

while True:
    gps.update()
    current = time.monotonic()

    if current - last_print >= 1.0:
        last_print = current
        if not gps.has_fix:
            print("Waiting for fix...")
            continue

        # Get UTC time and convert it to Eastern Time
        utc_time = gps.timestamp_utc
        if utc_time is not None:
            utc_datetime = datetime(utc_time.tm_year, utc_time.tm_mon, utc_time.tm_mday,
                                    utc_time.tm_hour, utc_time.tm_min, utc_time.tm_sec, tzinfo=pytz.UTC)
            eastern_time = utc_datetime.astimezone(eastern)
            formatted_time = eastern_time.strftime("%m/%d/%Y %I:%M:%S %p")

            # Print GPS information
            print("=" * 40)
            print(f"Timestamp (Eastern Time): {formatted_time}")
            print(f"Latitude: {gps.latitude:.6f} degrees")
            print(f"Longitude: {gps.longitude:.6f} degrees")
            if gps.speed_kmh is not None:
                print(f"Speed: {gps.speed_kmh} km/h")

            # Send email only once when we get the first fix
            if not email_sent:
                send_email(gps.latitude, gps.longitude, formatted_time, gps.speed_kmh)
                email_sent = True  # Prevent multiple emails

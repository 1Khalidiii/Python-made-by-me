import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import smtplib
from email.mime.text import MIMEText

# Set up the GPIO pin for the PIR sensor
pir_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_pin, GPIO.IN)

# Set up the GPIO pins for the lights
lights_pin = 17
GPIO.setup(lights_pin, GPIO.OUT)

# Set up the GPIO pins for the HVAC system
hvac_pin = 27
GPIO.setup(hvac_pin, GPIO.OUT)

# Set up the DHT11 temperature and humidity sensor
dht_pin = 22
dht_sensor = Adafruit_DHT.DHT11

# Set up the SMTP server details for sending email notifications
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "your_email@gmail.com"
smtp_password = "your_email_password"
smtp_sender = "your_email@gmail.com"
smtp_recipient = "recipient_email@gmail.com"

# Define a function to turn the lights on
def turn_lights_on():
    print("Lights on!")
    GPIO.output(lights_pin, GPIO.HIGH)

# Define a function to turn the lights off
def turn_lights_off():
    print("Lights off!")
    GPIO.output(lights_pin, GPIO.LOW)

# Define a function to turn the HVAC system on
def turn_hvac_on():
    print("HVAC on!")
    GPIO.output(hvac_pin, GPIO.HIGH)

# Define a function to turn the HVAC system off
def turn_hvac_off():
    print("HVAC off!")
    GPIO.output(hvac_pin, GPIO.LOW)

# Define a function to read the temperature and humidity from the sensor
def read_temperature_and_humidity():
    humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, dht_pin)
    if humidity is not None and temperature is not None:
        return temperature, humidity
    else:
        return None, None

# Define a function to send an email notification
def send_email_notification(subject, message):
    try:
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.ehlo()
        smtp_connection.starttls()
        smtp_connection.login(smtp_username, smtp_password)
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = smtp_sender
        msg['To'] = smtp_recipient
        smtp_connection.sendmail(smtp_sender, [smtp_recipient], msg.as_string())
        smtp_connection.quit()
        print("Email notification sent!")
    except Exception as e:
        print("Error sending email notification: {}".format(str(e)))

# Set up an event listener for the PIR sensor
GPIO.add_event_detect(pir_pin, GPIO.BOTH)

# Initialize the occupancy status to "not occupied"
occupied = False

# Initialize the temperature and humidity setpoints
temperature_setpoint = 20.0
humidity_setpoint = 50.0

# Initialize the security system status to "disarmed"
security_armed = False

# Define a function to arm or disarm the security system
def toggle_security_system():
    global security_armed
    security_armed = not security_armed
    if security_armed:
        print("Security system armed!")
    else:
        print("Security system disarmed!")

# Initialize the notification system status to "disabled"
notification_enabled = False

# Define a function to enable or disable email notifications
def toggle_notification_system():
    global notification_enabled
    notification_enabled = not notification_enabled
    if notification_enabled:
        print("Email notifications enabled!")
    else:
        print("Email notifications disabled!")

# Loop forever
while True:
    try:
        # Check for motion detection events
        if GPIO.event_detected(pir_pin):
            if GPIO.input(pir_pin) == GPIO.HIGH:
                # Motion detected, room is occupied
                if not occupied:
                    turn_lights_on()
                    turn_hvac_on()
                    occupied = True
                    if notification_enabled:
                        subject = "Occupancy Alert"
                        message = "The room is occupied."
                        send_email_notification(subject, message)
            else:
                # No motion detected, room is not occupied
                if occupied:
                    turn_lights_off()
                    turn_hvac_off()
                    occupied = False
                    if notification_enabled:
                        subject = "Occupancy Alert"
                        message = "The room is not occupied."
                        send_email_notification(subject, message)
        
        # Read the current temperature and humidity from the sensor
        temperature, humidity = read_temperature_and_humidity()
        
        # Check if the temperature is above or below the setpoint, and adjust the HVAC system accordingly
        if temperature is not None and temperature < temperature_setpoint:
            turn_hvac_on()
        elif temperature is not None and temperature >= temperature_setpoint:
            turn_hvac_off()
        
        # Check if the humidity is above or below the setpoint, and adjust the HVAC system accordingly
        if humidity is not None and humidity < humidity_setpoint:
            turn_hvac_on()
        elif humidity is not None and humidity >= humidity_setpoint:
            turn_hvac_off()
        
        # Check if the security system is armed, and if so, send an email notification if motion is detected
        if security_armed and GPIO.input(pir_pin) == GPIO.HIGH:
            subject = "Security Alert"
            message = "Motion detected in the room!"
            send_email_notification(subject, message)
        
        # Wait for a short period of time before checking again
        time.sleep(0.1)
    
    except KeyboardInterrupt:
        # Clean up the GPIO pins and exit the program if the user presses Ctrl-C
        GPIO.cleanup()
        exit()
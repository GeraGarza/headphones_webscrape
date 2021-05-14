import os  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import creds

chrome_options = Options()  
chrome_options.add_argument("--headless") 
driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),   chrome_options=chrome_options)  



def get_headphones():
    driver.get("https://electronics.sony.com/audio/headphones/headband/p/wh1000xm4-w")
    coming_soon_ele = driver.find_elements_by_xpath("//*[contains(text(), 'Coming Soon')]")
    return "They're out now!" if len(coming_soon_ele)>0 else ""


def emailnew(content):
    if content == "":
        return
    
    sender_email = "geragarzadev@gmail.com"
    receiver_email = "josegarzadev@gmail.com"
    password = creds.password
    message = MIMEMultipart("alternative")
    message["Subject"] = "Headphones time"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = """\
    New stuff in today!"""
    html = content #.to_html(index=False)
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

emailnew(get_headphones())

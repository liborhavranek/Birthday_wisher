import pandas
from datetime import datetime
import random
import smtplib

now = datetime.now()

day = now.day
month = now.month

birth_day = (month, day)


birth_day_data = pandas.read_csv("birthdays.csv")
birth_day_dictionary = birth_day_data.to_dict()


new_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birth_day_data.iterrows()}

if (month, day) in new_dict:
	birth_day_person = new_dict[birth_day]
	file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
	with open(file_path) as letter_file:
		contents = letter_file.read()
		contents = contents.replace("[NAME]", birth_day_person["name"])

	my_email = "liborhavranek91@gmail.com"
	password = "******************"

	with smtplib.SMTP("smtp.gmail.com", 587) as connection:
		connection.starttls()
		connection.login(user=my_email, password=password)
		connection.sendmail(from_addr=my_email, to_addrs=birth_day_person["email"],
		                    msg=f"Subject: Happy Birthday {contents}")
		connection.close()

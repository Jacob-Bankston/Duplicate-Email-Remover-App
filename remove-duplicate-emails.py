#HARD MODE: Create a script to make an a list of emails and output it into the email.txt file, then sort those emails into the sorted_emails.txt file

import random
import string

random_letters = list(string.ascii_lowercase)
random_email_tags = ["@yahoo.com", "@gmail.com", "@sbcglobal.net", "@msn.com", "@ymail.com", "@hotmail.com"]
random_emails = []
new_email_string = ""

def random_email_name():
    email_name = ""
    for i in range(random.randint(5, 10)):
        email_name = email_name + random.choice(random_letters)
    return email_name

for i in range(100):
    random_emails.append(f"{random_email_name()}@{random.choice(random_email_tags)}")

for i in range(60):
    if random.randint(0, 3) == 0:
        new_email_string = new_email_string + " "
    if random.randint(0, 3) == 1:
        new_email_string = new_email_string + "\n"
    new_email_string = f"{new_email_string}{random.choice(random_emails)},"

with open("emails.txt", "w") as email_object:
    email_object.write(new_email_string)


# NORMAL ASSIGNMENT - Remove duplicate emails and sort them into a clean txt document

sorted_emails = "sorted_emails.txt"
new_email_string = ""
new_email_array = []
output_email_string = ""
random_letters = "abcdefghijklmnopqrstuvwxyz"
random_email_tags = ["@yahoo.com", "@gmail.com", "@sbcglobal.net", "@msn.com", "@ymail.com", "@hotmail.com"]

with open("emails.txt") as email_list:
    email_string = email_list.read()

email_string = email_string.replace(' ', '')            #implemented instead of a concatenation loop with a new string
email_string = email_string.replace('\n', '')

# for index in range(len(email_string)):
#     if email_string[index] != " " and email_string[index] != "\n":
#         new_email_string += email_string[index]

email_array = email_string.split(",")

for index in range(len(email_array)):
    if email_array[index] not in new_email_array:
        new_email_array.append(email_array[index])

new_email_array.sort()

for email in new_email_array:
    output_email_string += f'{email}\n'

with open(sorted_emails, "w") as new_email_list:
    new_email_list.write(output_email_string)
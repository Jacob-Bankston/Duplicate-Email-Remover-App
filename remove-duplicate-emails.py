## Try to do the hard mode

## Try to implement the same code with a replace function

raw_emails = "emails.txt"
sorted_emails = "sorted_emails.txt"
new_email_string = ""
new_email_array = []
output_email_string = ""

with open(raw_emails) as email_list:
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
    output_email_string += f'{email}, \n'

with open(sorted_emails, "w") as new_email_list:
    new_email_list.write(output_email_string)
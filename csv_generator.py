import csv

logins = [["folder", "favorite", "type", "name", "notes", "fields",
          "reprompt", "login_uri", "login_username", "login_password", "login_totp"]]

data = []

# Enter user and password:
user_prefix = "x"
password = "scotland1"
domain = "poop.com"
name = input("Enter name:")


def generate_entry(day, month):
    return ["Coffee", None, "login", "Gails", f"Date: {day:02d}/{month:02d}", f"Date: {day:02d}/{month:02d}",
            None,  None, f"{user_prefix}{day:02d}{month:02d}", password, None]


thirty_day_months = [4, 6, 9, 11]

for month in range(1, 13):
    if month == 2:
        for day in range(1, 29):
            logins.append(generate_entry(day, month))
            data.append([name,
                        f"{user_prefix}{day:02d}{month:02d}@{email_domain}", day, month, 2002, password])
    elif month in thirty_day_months:
        for day in range(1, 31):
            logins.append(generate_entry(day, month))
            data.append([name,
                        f"{user_prefix}{day:02d}{month:02d}@{email_domain}", day, month, 2002, password])
    else:
        for day in range(1, 32):
            logins.append(generate_entry(day, month))
            data.append([name,
                        f"{user_prefix}{day:02d}{month:02d}@{email_domain}", day, month, 2002, password])


with open("logins.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(logins)

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

import csv

logins = [["folder", "favorite", "type", "name", "notes", "fields",
          "reprompt", "login_uri", "login_username", "login_password", "login_totp"]]

data = []


def generate_entry(day, month):
    return ["Coffee", None, "login", "Gails", f"Date: {day:02d}/{month:02d}", f"Date: {day:02d}/{month:02d}",
            None,  None, f"avigz{day:02d}{month:02d}", "coldpassword", None]


current_day = 11
month = 9
days_in_future = 14
for day in range(current_day, current_day + days_in_future + 1):
    logins.append(generate_entry(day, month))
    data.append([f"avigz{day:02d}{month:02d}",
                 f"avigz{day:02d}{month:02d}@coldmail.com", day, month, 2002, "coldpassword"])


with open("logins_current.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(logins)

with open("data_current.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

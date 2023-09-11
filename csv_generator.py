import csv

logins = [["folder", "favorite", "type", "name", "notes", "fields",
          "reprompt", "login_uri", "login_username", "login_password", "login_totp"]]

data = []


def generate_entry(day, month):
    return ["Coffee", None, "login", "Gails", f"Date: {day:02d}/{month:02d}", f"Date: {day:02d}/{month:02d}",
            None,  None, f"willp{day:02d}{month:02d}", "scotland1", None]


thirty_day_months = [4, 6, 9, 11]

for month in range(1, 13):
    if month == 2:
        for day in range(1, 29):
            logins.append(generate_entry(day, month))
            data.append([f"willp{day:02d}{month:02d}",
                        f"willp{day:02d}{month:02d}@coldmail.com", day, month, 2002, "scotland1"])
    elif month in thirty_day_months:
        for day in range(1, 31):
            logins.append(generate_entry(day, month))
            data.append([f"willp{day:02d}{month:02d}",
                        f"willp{day:02d}{month:02d}@coldmail.com", day, month, 2002, "scotland1"])
    else:
        for day in range(1, 32):
            logins.append(generate_entry(day, month))
            data.append([f"willp{day:02d}{month:02d}",
                        f"willp{day:02d}{month:02d}@coldmail.com", day, month, 2002, "scotland1"])


with open("logins.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(logins)

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

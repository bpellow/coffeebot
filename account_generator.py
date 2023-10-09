import csv
from datetime import date, timedelta


class AccountGenerator():
    def __init__(self, name, email_prefix, email_domain, password, duration):
        self.name = name
        self.email_prefix = email_prefix
        self.email_domain = email_domain
        self.password = password
        self.birthyear = 2002
        self.dates = self.get_dates(int(duration))

    def get_dates(self, duration):
        current = date.today()
        date_tuples = []
        for day in range(1, duration + 1):
            target = current + timedelta(days=day)
            day_month_tuple = (target.day, target.month)
            date_tuples.append(day_month_tuple)
        return date_tuples

    def generate_accounts(self):
        accounts = []
        for day, month in self.dates:
            accounts.append(
                [self.name, f"{self.email_prefix}{day:02d}{month:02d}@{self.email_domain}", day, month, self.birthyear, self.password])
        return accounts

    def store_details(self):
        details = [["folder", "favorite", "type", "name", "notes", "fields",
                    "reprompt", "login_uri", "login_username", "login_password", "login_totp"]]
        for day, month in self.dates:
            details.append(["Coffee", None, "login", "Gail's Bakery", f"Date: {day:02d}/{month:02d}", None,
                            None,  None, f"{self.email_prefix}{day:02d}{month:02d}@{self.email_domain}", self.password, None])
        with open("gails_logins.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(details)

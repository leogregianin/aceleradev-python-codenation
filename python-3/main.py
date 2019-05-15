import numpy as np
import datetime


class ManagerDates:
    def date_is_valid(self, date):
        try:
            datetime.datetime.strptime(date, "%d/%m/%Y")
        except ValueError:
            return False
        return True

    def date_weekday(self, date):
        return date.strftime("%A")

    def convert_string_to_date(self, date_str):
        formats = ["%d/%m/%Y", "%d-%m-%Y", "%d%m%Y"]
        date = False
        for date_format in formats:
            try:
                date = datetime.datetime.strptime(date_str, date_format)
            except ValueError:
                continue
        return date

    def get_all_dates(self, month, year):
        date = np.datetime64(f"{year}-{month}", dtype="datetime64[D]")
        return np.arange(date, date + np.timedelta64(1, "M"), dtype="datetime64[D]")

    def count_days_mounth(self, month, year):
        days_of_month = self.get_all_dates(month, year)
        workdays = np.is_busday(np.array(days_of_month).astype("datetime64[D]"))
        return np.count_nonzero(workdays)

    def get_first_monday(self, year):
        date = np.busday_offset(
            f"{year}-05", 0, roll="forward", holidays=[f"{year}-05-01"], weekmask="Mon"
        )
        return date.tolist().strftime("%d/%m/%Y")

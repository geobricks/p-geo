import datetime


def day_of_the_year_to_date(day, year):
    """
    Convert a day of an year to a date
    @param day: day of the year
    @type string i.e. "020" or "20"
    @param year: year of reference
    @type string or int i.e. "2014" or 2014
    @return: the date of the day/year i.e. "2012-01-20"
    """
    first_of_year = datetime.datetime(int(year), 1, 1).replace(month=1, day=1)
    ordinal = first_of_year.toordinal() - 1 + int(day)
    return datetime.date.fromordinal(ordinal)


def day_of_the_year_to_dekad(day, year):
    """
    Convert a day of an year to a date
    @param day: day of the year
    @type string i.e. "020" or "20"
    @param year: year of reference
    @type string or int i.e. "2014" or 2014
    @return: the dekad code i.e. "08-1" (month-dekad)
    """
    d = day_of_the_year_to_date(day, year)
    if d.day in range(1, 11):
        return create_dekad_code(d.month, 1)
    elif d.day in range(11, 21):
        return create_dekad_code(d.month, 2)
    elif d.day in range(21, 32):
        return create_dekad_code(d.month, 3)


def create_dekad_code(month, dekad):
    c = '0' if month < 10 else ''
    return c + str(month) + '-' + str(dekad)


# print range(1,11)
# print range(11,21)
# print range(21,32)
# print day_of_the_year_to_dekad("256", 2013)
# print day_of_the_year_to_dekad("30", 2013)
# print day_of_the_year_to_dekad(30, 2013)
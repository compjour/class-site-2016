from fetch import read_data
from csv import DictReader

def parse_data():
    """
    Returns a list of dictionaries from the raw text
    based on what fetch.read_data() returns
    """
    txt = read_data()
    lines = txt.splitlines()
    return list(DictReader(lines))


def get_birthday_rows_by_month_day(mth_day):
    """
    Calls parse_data to get a list of dicts

    Expects mth_day to be a string in this format:

        MM-DD, e.g. "05-12", (May 12)

    Returns a list of dicts that includes:

    - dicts with 'in_office' == '1' (legislators still in office)
    - dicts with the month and day components of 'birthdate'
        equal to the mth_day string
    """
    newrows = []
    original_rows = parse_data()
    for row in original_rows:
        if row['in_office'] == '1':
            rbdate = row['birthdate'][5:]
            if rbdate == mth_day:
                newrows.append(row)
    # all done
    return newrows



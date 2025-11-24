import jdatetime


def current_shamsi_year():
    return jdatetime.date.today().year


def current_shamsi_month():
    return jdatetime.date.today().month


def current_shamsi_day_of_month():
    return jdatetime.date.today().day


def current_shamsi_day_of_week():
    """
    Returns day of week according to DAYS_OF_WEEK (Saturday=1 ... Friday=7)
    jdatetime.date.weekday(): Monday=0 ... Sunday=6
    Adjust mapping so Saturday=1.
    """
    weekday = jdatetime.date.today().weekday()  # Mon=0 ... Sun=6
    # Map to Saturday=1 ... Friday=7
    return (weekday % 7) + 1

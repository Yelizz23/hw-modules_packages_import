from application.db.people import get_employees as ge
from application.salary import calculate_salary as cs
from datetime import datetime


if __name__ == '__main__':
    print(datetime.now())
    print()
    ge()
    print()
    cs()

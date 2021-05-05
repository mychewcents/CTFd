#!/usr/bin/env python
import argparse
import csv

from CTFd import create_app
from CTFd.models import Users


def main(args):
    app = create_app()

    with args.file, app.app_context():
        students = csv.DictReader(args.file.readlines(), delimiter=',')

        count = 0
        for student in students:
            print("Importing account for student: {fullname} ({email}) with password {password}".format(
                **student))
            team = Users(
                name=student['fullname'], email=student['email'], password=student['password'])
            team.verified = True
            app.db.session.add(team)
            count += 1

        app.db.session.commit()
        print("Done importing for all {count} student accounts.".format(
            count=count))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Import into CTFd database.')
    parser.add_argument('--file', required=True, type=argparse.FileType('r+'),
                        help='Input CSV file containing name, matriculation number, username, email and password columns.')
    args = parser.parse_args()
    main(args)

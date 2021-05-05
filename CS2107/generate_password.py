#!/usr/bin/env python
import argparse
import csv
import string
import random


def generate_password(length=10):
    return ''.join([random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length)])


def main(args):
    students = csv.DictReader(args.file.readlines(), delimiter=',')
    args.file.seek(0)
    writer = csv.DictWriter(args.file, fieldnames=students.fieldnames)
    writer.writeheader()

    count = 0
    for student in students:
        student['password'] = generate_password(args.length)
        # print("Created account for student: {fullname} ({email}) with password {password}".format(**student))
        count += 1
        writer.writerow(student)

    print("Done generating passwords for all {count} students.".format(
        count=count))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Read students info from CSV and append random password.')
    parser.add_argument('--length', default='10', type=int,
                        help="Specifies the desired password length")
    parser.add_argument('--file', required=True, type=argparse.FileType('r+'),
                        help='Input CSV file containing name, matriculation number, username, email and password columns.')
    args = parser.parse_args()

    with args.file:
        main(args)

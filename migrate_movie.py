import csv
import os
from contextlib import closing
from io import StringIO


os.environ['DJANGO_SETTINGS_MODULE'] = 'nozbe.settings'

import django
django.setup()

from django.db import connection


def insert_to_db():
    file = open('./title.basics.tsv', 'r')
    reader = csv.DictReader(file, dialect='excel-tab')
    stream = StringIO()
    writer = csv.writer(stream, delimiter='\t')
    counter = 1
    for row in reader:
        id = int(row['tconst'].lstrip('t'))
        if counter != id:
            for i in range(counter, id):
                writer.writerow([i, None, None, False] + [None] * 4)
            counter = id
        name = row['originalTitle']
        type_title = row['titleType']
        is_adult = row['isAdult']
        try:
            is_adult_bin = int(is_adult)
        except ValueError:
            is_adult_bin = 0
        is_adult = False
        if is_adult_bin:
            is_adult = True
        start_year = row['startYear']
        end_year = row['endYear']
        run_time = row['runtimeMinutes']
        genres = row['genres']
        writer.writerow([id, name, type_title, is_adult, start_year, end_year, run_time, genres])
        counter += 1
        print(row)

    stream.seek(0)
    with closing(connection.cursor()) as cursor:
        cursor.copy_from(
            file=stream,
            table='imdb_movie',
            sep='\t',
            columns=('id', 'name', 'type_title', 'is_adult',
                     'start_year', 'end_year', 'run_time', 'genres'),)


if __name__ == '__main__':
    insert_to_db()
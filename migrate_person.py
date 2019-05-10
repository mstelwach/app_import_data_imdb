import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'nozbe.settings'
import django
django.setup()

from django.db import connection
from io import StringIO
from contextlib import closing
import csv
import unidecode as unidecode


def insert_to_db():
    file = open('./name.basics.tsv', 'r')
    reader = csv.DictReader(file, dialect='excel-tab')
    stream = StringIO()
    writer = csv.writer(stream, delimiter='\t')

    for row in reader:
        id = int(row['nconst'].lstrip('nm'))
        full_name = row['primaryName'].split()
        username = unidecode.unidecode(''.join(full_name)).lower()
        first_name = full_name[0]
        last_name = full_name[-1]
        birth_year = row['birthYear']
        death_year = row['deathYear']
        profession = row['primaryProfession']
        writer.writerow([id, username, first_name, last_name, birth_year, death_year, profession])
        print(row)

    stream.seek(0)
    with closing(connection.cursor()) as cursor:
        cursor.copy_from(
            file=stream,
            table='imdb_actor',
            sep='\t',
            columns=('id', 'username', 'first_name', 'last_name', 'birth_year',
                     'death_year', 'profession'),)


if __name__ == '__main__':
    insert_to_db()

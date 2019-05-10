import os


os.environ['DJANGO_SETTINGS_MODULE'] = 'nozbe.settings'
import django
django.setup()

from django.db import connection
import csv
from io import StringIO
from contextlib import closing


def insert_to_db():

    file = open('./name.basics.tsv', 'r')
    reader = csv.DictReader(file, dialect='excel-tab')
    stream = StringIO()
    writer = csv.writer(stream, delimiter='\t')
    for row in reader:
        actor_id = int(row['nconst'].lstrip('nm'))
        titles = [int(title.lstrip('t')) for title in row['knownForTitles'].split(',') if 't' in title]
        if titles:
            for movie_id in titles:
                print(titles)
                writer.writerow([str(actor_id), str(movie_id)])

    stream.seek(0)
    with closing(connection.cursor()) as cursor:
        cursor.copy_from(
            file=stream,
            table='imdb_moviecast',
            sep='\t',
            columns=('actor_id', 'movie_id'), )


if __name__ == '__main__':
    insert_to_db()

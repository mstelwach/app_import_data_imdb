echo
echo "Witaj!"
echo
echo "Ten skrypt pozwoli na skonfigurowanie aplikacji pred jej pierwszym uruchomieniem."
echo "Baza danych zostanie odpowiednio skonfigurowana, nastąpi zapis rekordów"
echo "W tym czasie na ekranie pojawi się wiele komunikatów"
echo "ABY INSTALACJA POWIODŁA SIĘ MUSISZ MIEĆ DOSTĘP DO INTERNETU"
read -n1 -r -p "Naciśnij dowolny klawisz, by kontynuować."

echo
echo "Tworzy bazę danych PostgreSQL..."

sudo su -postgres 
psql -c 'create database nozbe_db'

echo "Tworzę nowe środowisko"
virtualenv -p python3 venv

echo "Instaluję niezbędne narzędzia do uruchomienia aplikacji" 
source ./venv/bin/activate
pip3 install -r requirements.txt


echo "Baza została utworzona"
echo "Pierwsza migracja tabeli do bazy danych"
python manage.py makemigrations
python manage.py migrate

echo "Zapis filmów  do bazy, proszę o chwilę cierpliwości ;)"
python migrate_movie.py

echo "Teraz czas na aktorów!!"
python migrate_person.py

echo "Ostatni krok! Posiadamy filmy i aktorów, czas na obsadę."
python migrate_moviecast.py

echo "Super, czas na uruchomienie aplikacji!"
python manage.py runserver

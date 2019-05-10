# Nozbe-imdb


It is an application that retrieves the contents of name.basics.tsv and title.basics.tsv and imports into the database PostgreSQL. The application uses the REST-API.

## Tasks!
  - Retrieves a list - in alphabetical order - of all movie titles with an indicated startYear value, along with associated persons (a mechanism with pagination of results).
  - As above, but with the option of listing movies with the indicated genre.
  - Return videos that people are associated with search results (that is, as a parameter we pass a phrase - for example with the name on the basis of which we are looking for people and for each of them we return a list of movie titles).

### Help in the implementation of the task

* [Django] - http://docs.python-guide.org/en/latest/writing/style/
* [Django-Rest-Framework] - http://www.django-rest-framework.org/tutorial/quickstart/
* [PostgreSQL] - https://www.postgresql.org/docs/

### Installation
The installation is done by running the script. Before running the script, you must have PostgreSQL database installed and the downloaded IMDB movie database in the form of a tsv file in the application folder.

##### Database movies links
https://www.dropbox.com/s/xaidig3yw2viyym/name.basics.tsv.gz?dl=0
https://www.dropbox.com/s/3do9bu0awq048uh/title.basics.tsv.gz?dl=0

To use the script you must:
 1. Open the terminal and then enter the following command:
 2. Go to the directory with the downloaded files by typing:
```sh
$ sh install.sh
```
#### That's all!


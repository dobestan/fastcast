# target: help - Display callable targets
help:
	@egrep "^# target:" [Mm]akefile


# target: clean - Clean all ".pyc" files
clean:
	find . -name "*.pyc" -exec rm -rf {} \;


# target: migrate - Migrate all django applications considering app dependencies
migrate:
	python fastcast/manage.py makemigrations users contents
	python fastcast/manage.py migrate


# target: clean_migration - folders in all django apps
clean_migrations:
	ls fastcast/ | grep -v -e 'manage.py' | xargs -I{} rm -rf fastcast/{}/migrations/

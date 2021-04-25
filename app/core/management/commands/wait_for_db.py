import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django Commants to pause execution database is available"""
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database to establish connection...!')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write(
                    'Database Unavailable, trying again after 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database Available!'))

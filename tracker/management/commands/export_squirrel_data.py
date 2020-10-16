from django.core.management.base import BaseCommand, CommandError
from tracker.models import Squirrel
import csv
import datetime

class Command(BaseCommand):
    help = 'Export data'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_file')

    def handle(self, *args, **options):
        file_ = options['squirrel_file']
        
        with open(file_, 'w') as csvfile:
            writer = csv.writer(csvfile)
            fields = Squirrel._meta.fields

            for i in Squirrel.objects.all():
                writer.writerow(getattr(i, field.name) for field in fields)
            csvfile.close()
        

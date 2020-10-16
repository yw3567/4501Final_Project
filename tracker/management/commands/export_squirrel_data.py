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
        meta = Squirrel._meta
        field_name = [field.name for field in meta.fields]
        with open(file_, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(field_name)
            for i in Squirrel.objects.all():
                writer.writerow(getattr(i, field) for field in field_name)
        

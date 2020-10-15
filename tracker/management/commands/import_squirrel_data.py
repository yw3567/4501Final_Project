from django.core.management.base import BaseCommand
from sightings.models import Sight
import csv
import datetime

class Command(BaseCommand):
    help = 'Get csv file of squirrel data'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_file', help='file containing squirrel details')

    def handle(self, *args, **options):
        file_ = options['squirrel_file']
        with open(options['squirrel_file']) as csvfile:
            reader = csv.DictReader(csvfile)
            for i in reader:


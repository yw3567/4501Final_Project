from django.core.management.base import BaseCommand
from tracker.models import Squirrel
import csv
import datetime

class Command(BaseCommand):
    help = 'Get csv file of squirrel data'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_file', help='file containing squirrel details')

    def handle(self, *args, **options):
        file_ = options['squirrel_file']
        with open(file_) as csvfile:
            reader = csv.DictReader(csvfile)
            for i in reader:
                read_table = Squirrel(
                Longitude = i['X'],
                Latitude = i['Y'],
                Unique_Squirrel_ID = i['Unique Squirrel ID'],
                Shift = i['Shift'],
                Date = datetime.date(int(i['Date'][4:8]), int(i['Date'][0:2]), int(i['Date'][2:4])),
                Age = i['Age'],
                Primary_Fur_Color = i['Primary Fur Color'],
                Location = i['Location'],
                Specific_Location = i['Specific Location'],
                Running = i['Running'],
                Chasing = i['Chasing'],
                Climbing = i['Climbing'],
                Eating = i['Eating'],
                Foraging = i['Foraging'],
                Other_Activities = i['Other Activities'],
                Kuks = i['Kuks'],
                Quaas = i['Quaas'],
                Moans = i['Moans'],
                Tail_flags = i['Tail flags'],
                Tail_twitches = i['Tail twitches'],
                Approaches = i['Approaches'],
                Indifferent = i['Indifferent'],
                Runs_from = i['Runs from'],
                )

            read_table.save()



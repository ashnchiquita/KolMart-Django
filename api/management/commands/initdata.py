from django.core.management import BaseCommand, call_command
from api.models import User

class Command(BaseCommand):
    help = "DEV COMMAND: Seed database user"

    def handle(self, *args, **options):
        call_command('loaddata','initial_data')

        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

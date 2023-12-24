from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from django.contrib.auth import get_user_model
from django.core.management import call_command
User = get_user_model()

class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            self.makemigrations_for_all_apps()
            self.migrate_for_all_apps()
            self.create_super_user()
        except Exception as e:
            raise CommandError(e)
    
    def makemigrations_for_all_apps(self):
        for app in settings.LOCAL_APPS:
            try:
                call_command('makemigrations', app)
            except Exception as e:
                raise CommandError(e)
        self.stdout.write(self.style.SUCCESS('Successfully created makemigrations for all apps'))
    
    def migrate_for_all_apps(self):
        for app in settings.LOCAL_APPS:
            try:
                call_command('migrate', app)
            except Exception as e:
                raise CommandError(e)
        self.stdout.write(self.style.SUCCESS('Successfully created migrations for all apps'))

    def create_super_user(self):
        User.objects.create_superuser(
            username = "admin",
            email = "admin@yopmail.com",
            password = "Admin@123",
        )
        self.stdout.write(self.style.SUCCESS('Successfully created super user'))

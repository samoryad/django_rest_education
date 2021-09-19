from django.core.management import BaseCommand
from userapp.models import ToDoUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        ToDoUser.objects.create(first_name='Ashot', email="Ashot@gb.ru",
                                last_name='Potikyan')
        ToDoUser.objects.create_superuser(
            'django', "django@gb.ru", 'geekbrains')

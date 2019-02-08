
from datetime import date, timedelta

from django.core import management

from social.models import UserProfile, UserPost


class Command(management.base.BaseCommand):
    help = "Populate the database"

    MIN_USER_COUNT = 10

    def add_arguments(self, parser):
        parser.add_argument('-e', '--extra-users',
                            dest='extra_users',
                            default=0,
                            type=int,
                            help='Number of extra users to be populated')

    def _create_userposts(self, user_profile, count):
        for i in range(count):
            text = f"I'm repeated {count} / {i}," * (i + 1)
            extra_fields = dict(
                likes=i,
                privacy=1 + i % 2,
                date_posted=date.today()-timedelta(i),
            )
            UserPost.objects.create_userpost(user_profile, text,
                                             **extra_fields)

    def _create_userprofiles(self, users_count):
        for user_number in range(1, users_count + 1):
            username = f'user_{user_number}'
            email = f'user_{user_number}@connect.com'
            password = f'password{user_number}'
            extra_fields = dict(
                first_name='UserFirst',
                last_name=f'{username}second',
                website=f'localhost/profile/{username}',
                phone_number=f'+91{user_number}'.ljust(13, '0'),
                bio=f'This is a simple bio of {username}'
            )
            user = UserProfile.objects.create_user(username, email=email,
                                                   password=password, **extra_fields)
            # Creating as many posts as user number
            self._create_userposts(user, user_number)

    def _create_superuser(self):
        username = 'super_user'
        email = f'super_user@connect.com'
        password = f'password'
        extra_fields = dict(
            first_name='Super',
            last_name='User',
            website=f'localhost/profile/super_user',
            phone_number='+91'.ljust(13, '9'),
            bio='This is a simple bio of Super user'
        )
        UserProfile.objects.create_superuser(username, email=email,
                                             password=password, **extra_fields)

    def handle(self, *args, **options):
        # Clear the database before populating
        management.call_command('flush', verbosity=1, interactive=False)

        users_count = options['extra_users']
        if users_count > 1000:
            users_count = 0
        self._create_userprofiles(self.MIN_USER_COUNT + users_count)

        self._create_superuser()

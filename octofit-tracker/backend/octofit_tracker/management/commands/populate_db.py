from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = "Populate the database with test data"

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Populate users
        user1 = User.objects.create(email="john.doe@example.com", name="John Doe")
        user2 = User.objects.create(email="jane.smith@example.com", name="Jane Smith")

        # Populate teams
        team1 = Team.objects.create(name="Team Alpha", members=[user1.id, user2.id])

        # Populate activities
        Activity.objects.create(user=user1, type="Running", duration=30)
        Activity.objects.create(user=user2, type="Cycling", duration=45)

        # Populate leaderboard
        Leaderboard.objects.create(team=team1, score=100)

        # Populate workouts
        Workout.objects.create(name="Morning Run", description="A 5km run to start the day.")
        Workout.objects.create(name="Evening Yoga", description="A relaxing yoga session.")

        self.stdout.write(self.style.SUCCESS("Database populated with test data."))

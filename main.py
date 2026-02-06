import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    global QuerySet1
    list_of_genres = ["Western", "Action", "Dramma"]
    list_of_actors = ["George Klooney", "Kianu Reaves",
                      "Scarlett Keegan", "Will Smith",
                      "Jaden Smith", "Scarlett Johansson"]
    for genre in list_of_genres:
        Genre.objects.create(name=genre)
    for actor in list_of_actors:
        actor_split = actor.split(" ")
        Actor.objects.create(first_name=actor_split[0],
                             last_name=actor_split[1])

    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")
    Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).update(first_name="George", last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(
        name="Action"
    ).delete()
    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    QuerySet1 = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
    return QuerySet1

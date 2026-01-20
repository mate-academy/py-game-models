import pytest
from django.db import models
from django.db.models import EmailField
from main import main
from db.models import Race, Skill, Player, Guild


@pytest.fixture(scope="session")
def populate_db(django_db_setup, django_db_blocker):
    """Fixtura, która raz wypełnia bazę danymi z main.py."""
    with django_db_blocker.unblock():
        main()


@pytest.mark.django_db
def test_guilds(populate_db):
    assert list(Guild.objects.values_list("name", "description")) == [
        ("archers", None),
        ("mags", "A community of the elf mags"),
        ("blacksmiths", "A community of the blacksmiths"),
    ]


@pytest.mark.django_db
def test_skills(populate_db):
    assert list(Skill.objects.values_list("name", "bonus")) == [
        (
            "Teleportation",
            "The ability to move so fast they look like they're teleporting. "
            "Could be considered to technically be Teleportation.",
        ),
        (
            "Reality Warping",
            "The ability to Warp Reality. Make the impossible become possible "
            "but can't warp anything containing the structure that holds "
            "everything together (Which are many creatures.)",
        ),
    ]


@pytest.mark.django_db
def test_races(populate_db):
    assert list(Race.objects.values_list("name", "description")) == [
        ("elf", "The magic race"),
        ("human", "Human race"),
    ]
    related_field = (
        Skill._meta.get_field("race").remote_field.related_name or "skill_set"
    )

    assert list(
        getattr(Race.objects.get(name="elf"), related_field).values_list("name")
    ) == [
        ("Teleportation",),
        ("Reality Warping",),
    ]

    assert (
        list(
            getattr(Race.objects.get(name="human"), related_field).values_list(
                "name", "bonus"
            )
        )
        == []
    )


@pytest.mark.django_db
def test_players(populate_db):
    assert list(
        Player.objects.values_list(
            "nickname", "email", "bio", "race__name", "guild__name"
        )
    ) == [
        ("john", "john@gmail.com", "Hello, I'm John, elf ranger", "elf", "archers"),
        ("max", "max@gmail.com", "Hello, I'm Max, elf mag", "elf", "mags"),
        ("arthur", "arthur@gmail.com", "Arthur, elf mag", "elf", "mags"),
        ("andrew", "andrew@gmail.com", "Hello, I'm Andrew", "human", "blacksmiths"),
        ("nick", "nick@gmail.com", "Hello, I'm Nick", "human", None),
    ]


@pytest.mark.django_db
def test_email_field():
    assert isinstance(Player._meta.get_field("email"), EmailField)


@pytest.mark.django_db
def test_guild_on_delete():
    assert Player._meta.get_field("guild").remote_field.on_delete == models.SET_NULL

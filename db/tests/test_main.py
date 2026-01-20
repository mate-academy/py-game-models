import pytest
from db.models import Race, Skill, Guild, Player

@pytest.mark.django_db
def test_race_str() -> None:
    race = Race.objects.create(name="Elf")
    assert str(race) == "Elf"

@pytest.mark.django_db
def test_skill_str() -> None:
    race = Race.objects.create(name="Elf")
    skill = Skill.objects.create(name="Archery", race=race)
    assert str(skill) == "Archery"

@pytest.mark.django_db
def test_guild_str() -> None:
    guild = Guild.objects.create(name="Warriors")
    assert str(guild) == "Warriors"

@pytest.mark.django_db
def test_player_str() -> None:
    race = Race.objects.create(name="Human")
    guild = Guild.objects.create(name="Warriors")
    player = Player.objects.create(
        nickname="John",
        email="john@example.com",
        race=race,
        guild=guild,
        bio="A brave warrior",
    )
    assert str(player) == "John"

import pytest

from app.main import main, Race, Skill, Player, Guild


@pytest.mark.django_db
def test_guilds():
    main()
    assert list(Guild.objects.values_list("name", "description")) == [
        ("archers", None),
        ("mags", "A community of the elf mags"),
        ("blacksmiths", "A community of the blacksmiths"),
    ]


@pytest.mark.django_db
def test_skills():
    main()
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
def test_races():
    main()
    assert list(Race.objects.values_list("name", "description")) == [
        ("elf", "The magic race"),
        ("human", "Human race"),
    ]
    assert list(
        Race.objects.get(name="elf").skill_set.values_list("name", "bonus")
    ) == [
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
    assert list(
        Race.objects.get(name="human").skill_set.values_list("name", "bonus")
    ) == []


@pytest.mark.django_db
def test_players():
    main()
    assert list(Player.objects.values_list("nickname", "email", "bio")) == [
        ("john", "john@gmail.com", "Hello, I'm John, elf ranger"),
        ("max", "max@gmail.com", "Hello, I'm Max, elf mag"),
        ("arthur", "arthur@gmail.com", "Arthur, elf mag"),
        ("andrew", "andrew@gmail.com", "Hello, I'm Andrew"),
        ("nick", "nick@gmail.com", "Hello, I'm Nick"),
    ]

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    elf_race = Race.objects.create(
        name="elf",
        description="The magic race"
    )

    human_race = Race.objects.create(
        name="human",
        description="Human race"
    )

    Skill.objects.create(
        name="Teleportation",
        bonus="The ability to move so fast they look like they're "
              "teleporting. Could be considered to technically be "
              "Teleportation.",  # Made to fix flake8 "line too long" warning
        race=elf_race
    )

    Skill.objects.create(
        name="Reality Warping",
        bonus="The ability to Warp Reality. "
              "Make the impossible become possible but can't warp "
              "anything containing the structure that holds everything "
              "together (Which are many creatures.)",
              # Made to fix flake8 "line too long" warning
        race=elf_race
    )

    archers_guild = Guild.objects.create(
        name="archers"
    )

    mags_guild = Guild.objects.create(
        name="mags",
        description="A community of the elf mags"
    )

    blacksmiths_guild = Guild.objects.create(
        name="blacksmiths",
        description="A community of the blacksmiths"
    )

    Player.objects.create(
        nickname="john",
        email="john@gmail.com",
        bio="Hello, I'm John, elf ranger",
        race=elf_race,
        guild=archers_guild
    )

    Player.objects.create(
        nickname="max",
        email="max@gmail.com",
        bio="Hello, I'm Max, elf mag",
        race=elf_race,
        guild=mags_guild
    )

    Player.objects.create(
        nickname="arthur",
        email="arthur@gmail.com",
        bio="Arthur, elf mag",
        race=elf_race,
        guild=mags_guild
    )

    Player.objects.create(
        nickname="andrew",
        email="andrew@gmail.com",
        bio="Hello, I'm Andrew",
        race=human_race,
        guild=blacksmiths_guild
    )

    Player.objects.create(
        nickname="nick",
        email="nick@gmail.com",
        bio="Hello, I'm Nick",
        race=human_race
    )


if __name__ == "__main__":
    main()

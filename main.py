import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    # Races
    elf_race = Race.objects.get_or_create(
        name="elf",
        description="The magic race"
    )[0]

    human_race = Race.objects.get_or_create(
        name="human",
        description="Human race"
    )[0]

    # Guilds
    archers_guild = Guild.objects.get_or_create(
        name="archers",
    )[0]

    mags_guild = Guild.objects.get_or_create(
        name="mags",
        description="A community of the elf mags"
    )[0]

    blacksmiths_guild = Guild.objects.get_or_create(
        name="blacksmiths",
        description="A community of the blacksmiths"
    )[0]

    # Skills
    teleportation_skill = Skill.objects.get_or_create(
        name="Teleportation",
        bonus="The ability to move so fast they look like they're teleporting."
              " Could be considered to technically be Teleportation.",
        race=elf_race
    )[0]

    reality_warping_skill = Skill.objects.get_or_create(
        name="Reality Warping",
        bonus="The ability to Warp Reality. "
              "Make the impossible become possible but can't "
              "warp anything containing the structure "
              "that holds everything together (Which are many creatures.)",
        race=elf_race
    )[0]

    # Players
    john_player = Player.objects.get_or_create(
        nickname="john",
        email="john@gmail.com",
        bio="Hello, I'm John, elf ranger",
        race=elf_race,
        guild=archers_guild
    )[0]

    max_player = Player.objects.get_or_create(
        nickname="max",
        email="max@gmail.com",
        bio="Hello, I'm Max, elf mag",
        race=elf_race,
        guild=mags_guild
    )[0]

    arthur_player = Player.objects.get_or_create(
        nickname="arthur",
        email="arthur@gmail.com",
        bio="Arthur, elf mag",
        race=elf_race,
        guild=mags_guild
    )[0]

    andrew_player = Player.objects.get_or_create(
        nickname="andrew",
        email="andrew@gmail.com",
        bio="Hello, I'm Andrew",
        race=human_race,
        guild=blacksmiths_guild
    )[0]

    nick_player = Player.objects.get_or_create(
        nickname="nick",
        email="nick@gmail.com",
        bio="Hello, I'm Nick",
        race=human_race
    )[0]

    # PRINT
    print(
        "Races:", elf_race, human_race,
        "Guilds:", blacksmiths_guild, archers_guild, mags_guild,
        "Skills:", teleportation_skill, reality_warping_skill,
        "Players:", john_player, max_player, arthur_player,
        andrew_player, nick_player,
        sep="\n"
    )


if __name__ == "__main__":
    main()

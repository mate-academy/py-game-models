import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def wipe() -> None:  # TODO: delete
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Guild.objects.all().delete()
    Player.objects.all().delete()


def main() -> None:
    try:
        Race.objects.create(
            name="Orc",
            description="Zug zug"
        )
        Race.objects.create(
            name="Dwarf",
            description="Oi gimme ale"
        )
    except Exception as e:
        print(f"C error {e}")
    try:
        Skill.objects.create(
            name="SMORc",
            bonus="+10% attack power",
            race_id=9
        )
        Skill.objects.create(
            name="Drunk blacksmith",
            bonus="+5% chance to forge an item",
            race_id=10
        )
    except Exception as e:
        print(f"C error {e}")

    try:
        Guild.objects.create(
            name="FOR THE HORDE",
            description="YES"
        )
        Guild.objects.create(
            name="FOR THE ALE",
            description="..hic"
        )
    except Exception as e:
        print(f"C error {e}")

    try:
        Player.objects.create(
            nickname="Player",
            email="letmein@gmail.com",
            bio="18hr uptime",
            race_id=9,
            guild_id=7
        )
    except Exception as e:
        print(f"C error {e}")


if __name__ == "__main__":
    # wipe()
    main()

import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def get_or_create_race(name: str) -> Race:
    try:
        race = Race.objects.get(name=name)
    except Race.DoesNotExist:
        race = Race.objects.create(name=name)
        race.save()
    return race


def get_or_create_guild(name: str) -> Guild:
    try:
        guild = Guild.objects.get(name=name)
    except Guild.DoesNotExist:
        guild = Guild.objects.create(name=name)
        guild.save()
    return guild


def main() -> None:
    players_data = json.load(open("players.json", "r"))

    elf_race = Race.objects.create(name="elf", description="The magic race")
    Skill.objects.create(
        name="Teleportation",
        bonus="The ability to move so fast they look like they're "
              "teleporting. Could be considered to technically be "
              "Teleportation.",
        race_id=elf_race.id)
    Skill.objects.create(
        name="Reality warping",
        bonus="The ability to Warp Reality. Make the impossible become"
              " possible but can't warp anything containing the structure"
              " that holds everything together (Which are many creatures.)",
        race_id=elf_race.id)

    for player_key in players_data.keys():
        player = players_data[player_key]
        Player.objects.create(nickname=player_key,
                              email=player["email"],
                              bio=player["bio"],
                              race=get_or_create_race(player["race"]),
                              guild=get_or_create_guild(player["guild"]))


if __name__ == "__main__":
    main()

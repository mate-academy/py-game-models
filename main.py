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


def get_or_create_guild(guild: dict) -> Guild:
    try:
        guild = Guild.objects.get(name=guild["name"])
    except Guild.DoesNotExist:
        guild = Guild.objects.create(name=guild["name"])
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
        race=elf_race)
    Skill.objects.create(
        name="Reality warping",
        bonus="The ability to Warp Reality. Make the impossible become"
              " possible but can't warp anything containing the structure"
              " that holds everything together (Which are many creatures.)",
        race=elf_race)

    for player_key in players_data.keys():
        player = players_data[player_key]
        Player.objects.create(nickname=player_key,
                              email=player["email"],
                              bio=player["bio"],
                              race=get_or_create_race(player["race"])
                              )
        if player["guild"] is not None:
            guild = get_or_create_guild(player["guild"])
            Player.objects.filter(guild=guild.guild_id).update(guild=guild)

if __name__ == "__main__":
    main()

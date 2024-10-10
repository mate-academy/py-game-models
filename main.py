# import init_django_orm  # noqa: F401
# import json
# from db.models import Race, Skill, Player, Guild
#
#
# def main() -> None:
#     with open("players.json") as file:
#         data = json.load(file)
#
#     for player in data:
#         race_name = data[player]["race"]["name"]
#         race_description = data[player]["race"]["description"]
#         Race.objects.get_or_create(name=race_name,
#                                    description=race_description)
#
#         for skill in data[player]["race"]["skills"]:
#             skill_name = skill["name"]
#             skill_bonus = skill["bonus"]
#             Skill.objects.get_or_create(name=skill_name,
#                                         bonus=skill_bonus,
#                                         race=Race.objects.get(name=race_name))
#
#         guild_data = data[player].get("guild")
#         player_guild = None
#         if guild_data:
#             guild_name = guild_data["name"]
#             guild_description = guild_data["description"]
#             player_guild, created = Guild.objects.get_or_create(
#                 name=guild_name,
#                 description=guild_description
#             )
#
#         player_name = player
#         player_email = data[player]["email"]
#         player_bio = data[player]["bio"]
#         player_race = Race.objects.get(name=race_name)
#         Player.objects.get_or_create(nickname=player_name,
#                                      email=player_email,
#                                      bio=player_bio,
#                                      race=player_race,
#                                      guild=player_guild)
#
#
# if __name__ == "__main__":
#     main()

import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    races = []
    skills = []
    guilds = []
    players = []

    for player in data:
        race_name = data[player]["race"]["name"]
        race_description = data[player]["race"]["description"]
        race, created = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description}
        )
        if created:
            races.append(race)

        for skill in data[player]["race"]["skills"]:
            skill_name = skill["name"]
            skill_bonus = skill["bonus"]
            skill_instance, created = Skill.objects.get_or_create(
                name=skill_name,
                defaults={"bonus": skill_bonus, "race": race})
            if created:
                skills.append(skill_instance)

        guild_data = data[player].get("guild")
        player_guild = None
        if guild_data:
            guild_name = guild_data["name"]
            guild_description = guild_data["description"]
            guild, created = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description}
            )
            if created:
                guilds.append(guild)
            player_guild = guild

        player_name = player
        player_email = data[player]["email"]
        player_bio = data[player]["bio"]
        player_race = Race.objects.get(name=race_name)
        player_instance, created = Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_email,
                "bio": player_bio,
                "race": player_race,
                "guild": player_guild
            }
        )
        if created:
            players.append(player_instance)

    Race.objects.bulk_create(races, ignore_conflicts=True)
    Skill.objects.bulk_create(skills, ignore_conflicts=True)
    Guild.objects.bulk_create(guilds, ignore_conflicts=True)
    Player.objects.bulk_create(players, ignore_conflicts=True)


if __name__ == "__main__":
    main()

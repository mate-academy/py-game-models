import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with (open("players.json", "r") as file):
        players = json.load(file)
    for player in players:
        # player's characteristics
        characteristics = players[player]
        email = characteristics.get("email")
        bio = characteristics.get("bio")
        race = characteristics.get("race")
        guild = characteristics.get("guild")
        race_skills_list = None
        race_obj = None
        # race's characteristics
        if race:
            race_name = race.get("name")
            race_description = race.get("description")
            race_skills_list = race.get("skills")
            race_obj, _ = Race.objects.get_or_create(
                name=race_name,
                defaults={"description": race_description})
        # race's skills
        if race_skills_list:
            for skill in race_skills_list:
                skill_name = skill.get("name")
                skill_bonus = skill.get("bonus")
                skill_obj, _ = Skill.objects.get_or_create(
                    name=skill_name,
                    race=race_obj,
                    defaults={"bonus": skill_bonus})
        guild_obj = None
        # guild characteristics
        if guild:
            guild_name = guild.get("name")
            guild_description = guild.get("description")
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description":
                          guild_description})
        Player.objects.get_or_create(nickname=player,
                                     defaults={"email": email,
                                               "bio": bio,
                                               "race": race_obj,
                                               "guild": guild_obj})


if __name__ == "__main__":
    main()

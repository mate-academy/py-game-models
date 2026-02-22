import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:  # noqa: C901
    with open("players.json", "r") as data:
        data_dict = json.load(data)
    race_array = []
    skills_array = []
    guild_array = []

    for players_races in data_dict.values():
        for race_key, race_value in players_races.items():
            race_dict = {}
            if race_key == "race":
                race_dict["name"] = race_value.get("name")
                race_dict["description"] = (
                    race_value.get("description"))
                if race_dict not in race_array:
                    race_array.append(race_dict)

    for race in race_array:
        Race.objects.create(
            name=race["name"],
            description=race["description"]
        )

    for players in data_dict.values():
        for key, value in players.items():
            if key == "guild" and value is not None:
                guild_dict = {}
                guild_dict["name"] = value.get("name")
                guild_dict["description"] = (
                    value.get("description"))
                if guild_dict not in guild_array:
                    guild_array.append(guild_dict)

    for guild in guild_array:
        Guild.objects.get_or_create(
            name=guild["name"],
            description=guild["description"]
        )

    for players in data_dict.values():
        for skills_key, skills_value in players.items():
            if skills_key == "race":
                race_name = skills_value.get("name")
                race_id = Race.objects.get(name=race_name).id
                for key, value in skills_value.items():
                    if key == "skills" and value is not None:
                        for skill in value:
                            if value is not None:
                                skills_dict = {}
                                skills_dict["name"] = skill.get("name")
                                skills_dict["bonus"] = skill.get("bonus")
                                skills_dict["race_id"] = int(race_id)
                                if (skills_dict not in skills_array
                                        and skills_dict is not None):
                                    skills_array.append(skills_dict)

    for skill in skills_array:
        if skill is not None:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race_id=skill.get("race_id")
            )

    for player_key, player_value in data_dict.items():
        nickname = player_key
        email = player_value.get("email")
        bio = player_value.get("bio")
        race = player_value.get("race")
        guild = player_value.get("guild")
        guild_to_create = None
        if player_value.get("race") is not None:
            name = race.get("name")
            race_to_create = Race.objects.get(name=name)
        else:
            race_to_create = None
        if player_value.get("guild") is not None:
            name = guild.get("name")
            guild_to_create = Guild.objects.get(name=name)
        else:
            guild_to_create = None
        Player.objects.get_or_create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race_to_create,
            guild=guild_to_create
        )


if __name__ == "__main__":
    main()

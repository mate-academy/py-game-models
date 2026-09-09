import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_data = json.load(file)
    for player in players_data:
        p_data: dict[str, dict] = players_data[player]
        race_dict: dict[str, list] = p_data.get("race")
        race, created = Race.objects.get_or_create(
            name=race_dict["name"],
            description=race_dict["description"]
        )
        skill_list: list[dict] = race_dict.get("skills")
        for skill in skill_list:
            name, bonus = skill.values()
            Skill.objects.get_or_create(
                name=name,
                bonus=bonus,
                race=race
            )
        guild_dict: dict = p_data.get("guild")
        if guild_dict:
            name, descript = guild_dict.values()
            guild, created = Guild.objects.get_or_create(
                name=name,
                description=descript
            )
        Player.objects.create(
            nickname=player,
            email=p_data.get("email"),
            bio=p_data.get("bio"),
            race=race,
            guild=None if not guild_dict else guild
        )


if __name__ == "__main__":
    main()

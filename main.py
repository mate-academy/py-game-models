import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)
    # for player in data:
    for player_name, player_data in players.items():
        race_data = player_data.get("race")
        if race_data:
            race, created = Race.objects.get_or_create(
                name=race_data.get("name"),
                defaults={"description": race_data.get("description")}
            )
        skills_data = player_data["race"].get("skills")
        for skill in skills_data:
            if skill:
                skill_, created = Skill.objects.get_or_create(
                    name=skill.get("name"),
                    defaults={"bonus": skill.get("bonus"), "race": race}
                )
        guild_data = player_data.get("guild")
        if guild_data:
            guild, created = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description")}
            )
        else:
            guild = None
        Player.objects.create(
            nickname=player_name,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()

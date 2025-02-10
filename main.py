import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)
    for player in data:
        race_data = data[player].get("race")
        if race_data:
            race, created = Race.objects.get_or_create(
                name=race_data.get("name"),
                defaults={"description": race_data.get("description")}
            )
        skills_data = data[player]["race"].get("skills")
        for skill in skills_data:
            if skill:
                skill_, created = Skill.objects.get_or_create(
                    name=skill.get("name"),
                    defaults={"bonus": skill.get("bonus"), "race": race}
                )
        guild_data = data[player].get("guild")
        if guild_data:
            guild, created = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description")}
            )
        else:
            guild = None
        Player.objects.get_or_create(
            nickname=player,
            defaults={
                "email": data[player].get("email"),
                "bio": data[player].get("bio"),
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()

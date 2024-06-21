import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_data in data:
        race_data = data[player_data]["race"]
        guild_data = data[player_data]["guild"]
        skills_data = race_data["skills"]

        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )
        if guild_data is not None:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description", "")}
            )
        else:
            guild = None

        skills = []
        for skill_data in skills_data:
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"], "race": race}
            )
            skills.append(skill)

        player, _ = Player.objects.get_or_create(
            nickname=player_data,
            defaults={
                "email": data[player_data]["email"],
                "bio": data[player_data]["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()

import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        data = json.load(f)

    for player_name, player_data in data.items():

        data_race = player_data.get("race")
        race, _ = Race.objects.get_or_create(
            name=data_race.get("name"),
            description=data_race.get("description")
        )

        data_skills = data_race.get("skills")
        for skill in data_skills:
            skill, _ = Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race
            )

        data_guild = player_data.get("guild")
        if data_guild:
            guild, _ = Guild.objects.get_or_create(
                name=data_guild.get("name"),
                description=data_guild.get("description")
            )
        else:
            guild = None

        _, created = Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_data.get("email"),
                "bio": player_data.get("bio"),
                "race": race,
                "guild": guild,
            }
        )
        if created:
            print(f"{player_name} successfully created")
        else:
            print(f"{player_name} already exists")


if __name__ == "__main__":
    main()

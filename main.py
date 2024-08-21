import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    def get_or_create_race(race_data: dict) -> Race:
        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]})

        for skill_data in race_data["skills"]:
            Skill.objects.get_or_create(name=skill_data["name"],
                                        defaults={"bonus": skill_data["bonus"],
                                                  "race": race})

        return race

    def get_or_create_guild(guild_data: dict) -> Guild:
        if guild_data:
            guild, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]})
            return guild
        return None

    for player_name, player_data in data.items():
        race = get_or_create_race(player_data["race"])
        guild = get_or_create_guild(player_data.get("guild"))

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()

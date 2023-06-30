import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    def create_guild(guild: dict) -> None:
        if guild and not Guild.objects.filter(name=guild["name"]).exists():
            Guild.objects.create(
                name=guild["name"],
                description=guild["description"]
            )

    def get_guild_id(guild: dict) -> int:
        return Guild.objects.get(name=guild["name"]).id if guild else None

    def create_race(race: dict) -> None:
        if not Race.objects.filter(name=race["name"]).exists():
            Race.objects.create(
                name=race["name"],
                description=race["description"]
            )

    def get_race_id(race_name: dict) -> int:
        return Race.objects.get(name=race_name).id

    def create_skills(race: dict) -> None:

        for skill in race["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race_id=get_race_id(race["name"])
                )

    def create_players() -> None:
        with open("players.json", "r") as players:
            players = json.load(players)
            print(players)
        for player, info in players.items():
            name = player
            email = info["email"]
            bio = info["bio"]
            guild = info["guild"]
            race = info["race"]
            print(race)

            create_guild(guild)
            create_race(race)
            create_skills(race)

            guild_id = get_guild_id(guild)
            race_id = get_race_id(race["name"])

            Player.objects.create(
                nickname=name,
                email=email,
                bio=bio,
                guild_id=guild_id,
                race_id=race_id
            )

    create_players()


if __name__ == "__main__":
    main()

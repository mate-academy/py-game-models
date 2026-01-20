import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def create_race(race: dict) -> Race:
    if not Race.objects.filter(name=race["name"]).exists():
        new_race = Race(
            name=race["name"],
            description=race["description"]
        )
        new_race.save()
        for skill in race["skills"]:
            new_skill = Skill(
                name=skill["name"],
                bonus=skill["bonus"],
                race=new_race
            )
            new_skill.save()
        return new_race
    return Race.objects.get(name=race["name"])


def create_guild(guild: dict) -> Guild | None:
    if not guild:
        return None
    if not Guild.objects.filter(name=guild["name"]).exists():
        new_guild = Guild(
            name=guild["name"],
            description=guild["description"]
        )
        new_guild.save()
        return new_guild
    return Guild.objects.get(name=guild["name"])


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

        for player, value in players.items():
            if not Player.objects.filter(nickname=player).exists():
                new_player = Player(
                    nickname=player,
                    email=value["email"],
                    bio=value["bio"],
                    race=create_race(value["race"]),
                    guild=create_guild(value["guild"])
                )
                new_player.save()


if __name__ == "__main__":
    main()

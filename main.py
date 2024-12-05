import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, player_data in data.items():
        race = player_data["race"]
        new_race, _ = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )

        for skill in player_data["race"]["skills"]:
            new_skill, _ = Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=new_race
            )

        guild = player_data["guild"]

        if guild:
            new_guild, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )
        else:
            new_guild = None

        new_player = Player(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=new_race,
            guild=new_guild
        )

        new_player.save()


if __name__ == "__main__":
    main()

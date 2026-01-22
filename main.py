import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_data = json.load(file)

    for nickname, player in players_data.items():
        race = player["race"]
        new_race, _ = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )

        for skill in player["race"]["skills"]:
            new_skill, _ = Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=new_race
            )

        guild = player["guild"]
        if guild:
            new_guild, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )
        else:
            new_guild = None

        new_player = Player(
            nickname=nickname,
            email=player["email"],
            bio=player["bio"],
            race=new_race,
            guild=new_guild
        )

        new_player.save()


if __name__ == "__main__":
    main()

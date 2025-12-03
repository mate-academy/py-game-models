import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for name, player in players.items():
        nickname = name
        email = player.get("email")
        bio = player.get("bio")
        race = player.get("race")
        guild = player.get("guild")
        skills = []
        player_guild = None

        if guild is not None:
            player_guild, _ = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )

        player_race = None
        if player.get("race"):
            player_race, _ = Race.objects.get_or_create(
                name=race.get("name"),
                description=race.get("description")
            )
            skills = player.get("race").get("skills")

        if skills:
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=player_race
                )

        Player(
            nickname=nickname,
            email=email,
            bio=bio,
            race=player_race,
            guild=(player_guild if guild else None)).save()


if __name__ == "__main__":
    main()

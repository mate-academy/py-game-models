import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file_out:
        players = json.load(file_out)
    for player in players.items():

        player_race, _ = Race.objects.get_or_create(
            name=player[1]["race"]["name"],
            description=player[1]["race"]["description"]
        )

        if skill_list := player[1]["race"].get("skills"):
            for skill in skill_list:
                Skill.objects.get_or_create(
                    **skill,
                    race=player_race
                )

        if player_guild := player[1]["guild"]:
            player_guild, _ = Guild.objects.get_or_create(
                **player_guild
            )

        Player.objects.get_or_create(
            nickname=player[0],
            email=player[1]["email"],
            bio=player[1]["bio"],
            race=player_race,
            guild=player_guild,
            ),


if __name__ == "__main__":
    main()

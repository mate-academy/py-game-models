import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    race_inst = None
    guild_inst = None

    with open("players.json", "r") as file:
        players = json.load(file)

    for player_name, player in players.items():
        if not Race.objects.filter(name=player["race"]["name"]).exists():
            race_inst, created = Race.objects.get_or_create(
                name=player["race"]["name"],
                defaults={"description": player["race"]["description"]}
            )

        for skill in player["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                skill_inst, created = Skill.objects.get_or_create(
                    name=skill["name"],
                    defaults={"bonus": skill["bonus"], "race": race_inst}
                )

        guild = player.get("guild")
        if guild is not None:
            if not Guild.objects.filter(name=player["guild"]["name"]).exists():
                guild_inst, created = Guild.objects.get_or_create(
                    name=player["guild"]["name"],
                    defaults={"description": player["guild"]["description"]}
                )

        else:
            guild_inst = None

        if not Player.objects.filter(nickname=player_name).exists():
            Player.objects.create(
                nickname=player_name,
                email=player["email"],
                bio=player["bio"],
                race=race_inst,
                guild=guild_inst
            )


if __name__ == "__main__":
    main()

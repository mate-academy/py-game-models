import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players = json.load(f)

    for nick, player in players.items():
        race = player.get("race")
        race_obj = None
        if race and race.get("name"):
            race_obj, _ = Race.objects.get_or_create(
                name=race["name"],
                defaults={"description": race.get("description", "")}
            )

            for skill in race.get("skills") or []:
                if skill.get("name") and skill.get("bonus") and race_obj:
                    Skill.objects.get_or_create(
                        name=skill["name"],
                        defaults={
                            "bonus": skill["bonus"],
                            "race": race_obj
                        }
                    )

        guild_obj = None
        guild = player.get("guild")
        if guild and guild.get("name"):
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild["name"],
                defaults={"description": guild.get("description")}
            )

        if all((
            nick,
            player.get("email"),
            player.get("bio"),
            race_obj
        )):
            Player.objects.get_or_create(
                nickname=nick,
                defaults={
                    "email": player["email"],
                    "bio": player["bio"],
                    "race": race_obj,
                    "guild": guild_obj
                }
            )


if __name__ == "__main__":
    main()

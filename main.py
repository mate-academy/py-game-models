import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.loads(file.read())
    for nick, info in data.items():
        player_race, _ = Race.objects.get_or_create(
            name=info.get("race").get("name"),
            description=info.get("race").get("description"),
        )
        player_guild = info.get("guild")
        if player_guild:
            player_guild, _ = Guild.objects.get_or_create(
                name=info.get("guild").get("name"),
                description=info.get("guild").get("description"),
            )
        player = Player.objects.create(
            nickname=nick,
            email=info.get("email"),
            bio=info.get("bio"),
            race=player_race,
            guild=player_guild,
        )
        skills = info.get("race").get("skills")
        if skills:
            for skill in skills:
                if not Skill.objects.filter(name=skill.get("name")).exists():
                    player.race.skill_set.create(
                        name=skill.get("name"), bonus=skill.get("bonus")
                    )


if __name__ == "__main__":
    main()

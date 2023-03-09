import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.loads(file.read())
    for nick, info in data.items():
        race_data = info.get("race")
        player_guild = info.get("guild")
        skills = info.get("race").get("skills")
        player_race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            description=race_data.get("description"),
        )
        if player_guild:
            player_guild, _ = Guild.objects.get_or_create(
                name=player_guild.get("name"),
                description=player_guild.get("description"),
            )
        player = Player.objects.create(
            nickname=nick,
            email=info.get("email"),
            bio=info.get("bio"),
            race=player_race,
            guild=player_guild,
        )
        if skills:
            for skill in skills:
                if not Skill.objects.filter(name=skill.get("name")).exists():
                    player.race.skill_set.create(
                        name=skill.get("name"), bonus=skill.get("bonus")
                    )


if __name__ == "__main__":
    main()

import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_info = json.load(file)

    for nickname, player_info in players_info.items():
        email = player_info.get("email")
        bio = player_info.get("bio")
        race_info = player_info.get("race")
        skills_info = race_info.get("skills")
        guild_info = player_info.get("guild")

        race_name = race_info.get("name")
        if not Race.objects.filter(name=race_name).exists():
            race = Race.objects.create(
                name=race_name,
                description=race_info.get("description")
            )
        else:
            race = Race.objects.get(name=race_name)

        skills = []
        for skill in skills_info:
            skill_name = skill.get("name")
            if Skill.objects.filter(name=skill_name).exists():
                skills.append(Skill.objects.get(name=skill_name))
                continue
            Skill.objects.create(
                name=skill_name,
                bonus=skill.get("bonus"),
                race_id=race.id
            )

        if guild_info:
            guild_name = guild_info.get("name")
            if not Guild.objects.filter(name=guild_name).exists():
                guild = Guild.objects.create(
                    name=guild_name,
                    description=guild_info.get("description")
                )
            else:
                guild = Guild.objects.get(name=guild_name)
        else:
            guild = None

        if not Player.objects.filter(nickname=nickname).exists():
            Player.objects.create(
                nickname=nickname,
                email=email,
                bio=bio,
                race_id=race.id,
                guild_id=guild.id if guild else None
            )


if __name__ == "__main__":
    main()

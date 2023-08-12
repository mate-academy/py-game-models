import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as source_file:
        players = json.load(source_file)

    for key, data in players.items():
        new_player = Player(
            nickname=key,
            email=data.get("email"),
            bio=data.get("bio")
        )

        guild = data.get("guild")
        guild_from_db = None
        if guild is not None:
            guild_name = guild.get("name")
            if not Guild.objects.filter(name=guild_name).exists():
                guild_from_db = Guild.objects.create(
                    name=guild_name,
                    description=guild.get("description")
                )
            else:
                guild_from_db = Guild.objects.get(name=guild_name)
        new_player.guild = guild_from_db

        race_ = data.get("race")
        race_name = race_.get("name")
        race_from_db = None
        if not Race.objects.filter(name=race_name).exists():
            Race.objects.create(
                name=race_name,
                description=race_.get("description")
            )
        else:
            race_from_db = Race.objects.get(name=race_name)

        skills = race_.get("skills")
        if skills is not None:
            for skill in skills:
                if not Skill.objects.filter(name=skill.get("name")).exists():
                    Skill.objects.create(
                        name=skill.get("name"),
                        bonus=skill.get("bonus"),
                        race=race_from_db
                    )

        new_player.race = race_from_db
        if not Player.objects.filter(nickname=new_player.nickname).exists():
            new_player.save()


if __name__ == "__main__":
    main()

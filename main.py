import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        data = json.load(f)

        for player, info in data.items():
            # Create guilds
            if "guild" in info and info["guild"] is not None:
                guild_list = Guild.objects.values_list("name", flat=True)
                if info["guild"]["name"] not in guild_list:
                    guild = Guild.objects.create(
                        name=info["guild"]["name"],
                        description=info["guild"]["description"],
                    )
            else:
                guild = None
            # Create races and skills
            if "race" in info and info["race"] is not None:
                race_list = Race.objects.values_list("name", flat=True)
                if info["race"]["name"] not in race_list:
                    race = Race.objects.create(
                        name=info["race"]["name"],
                        description=info["race"]["description"]
                    )
                # Skills
                skills_list_data = info["race"]["skills"]
                if "skills" in info["race"] and skills_list_data is not None:
                    skills_list = Skill.objects.values_list("name", flat=True)
                    for skill in skills_list_data:
                        if skill["name"] not in skills_list:
                            Skill.objects.create(
                                name=skill["name"],
                                bonus=skill["bonus"],
                                race=race
                            )
            # Create players
            if player not in Player.objects.values_list("nickname"):
                Player.objects.create(
                    nickname=player,
                    email=info["email"],
                    bio=info["bio"],
                    race=race,
                    guild=guild,
                )


if __name__ == "__main__":
    main()

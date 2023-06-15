import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
       
        
        player_json = json.load(f)

        for nickname, other in player_json.items():
            race_date = other.get("race")
            race, _ = Race.objects.get_or_create(
                name=race_date["name"],
                description=race_date["description"]
            )

            skill_date = race_date["skills"]
            for skill in skill_date:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

            guild_date = other.get("guild")

            if guild_date:
                guild_date, _ = Guild.objects.get_or_create(
                    name=guild_date["name"],
                    description=guild_date["description"]
                )

            Player.objects.create(
                nickname=nickname,
                email=other.get("email"),
                bio=other.get("bio"),
                race=race,
                guild=guild_date
            )


if __name__ == "__main__":
    main()

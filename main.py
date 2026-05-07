import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_info = json.load(f)
        for nickname, player_info in players_info.items():
            race_name = player_info["race"]["name"]
            race_desc = player_info["race"].get("description", "")
            race, _ = Race.objects.get_or_create(
                name=race_name,
                defaults={"description": race_desc}
            )

            guild_info = player_info.get("guild")
            guild = None
            if guild_info:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_info["name"],
                    defaults={"description": guild_info.get("description")})

            skills = []
            for skill_info in player_info["race"].get("skills", []):
                skill, _ = Skill.objects.get_or_create(
                    name=skill_info["name"],
                    race=race,
                    defaults={"bonus": skill_info["bonus"]}
                )
                skills.append(skill)

            Player.objects.create(
                nickname=nickname,
                email=player_info["email"],
                bio=player_info["bio"],
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()

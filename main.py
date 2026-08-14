import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)

    for nickname, player_data in players_data.items():
        race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            defaults={"description":
                      player_data["race"].get("description", " ")}
        )
        guild = None
        if player_data.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                defaults={"description":
                          player_data["guild"].get("description")}
            )

        skills = []
        for skill_data in player_data["race"].get("skills", []):
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                race=race,
                defaults={"bonus": skill_data["bonus"]}
            )
            skills.append(skill)

        Player.objects.create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data.get("bio", ""),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()

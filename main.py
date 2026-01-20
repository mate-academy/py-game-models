import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for nickname, player_data in data.items():
        race_data = player_data.get("race", {}) or {}

        race, created = Race.objects.get_or_create(
            name=race_data.get("name"), defaults={
                "description": race_data.get("description", "")}
        )
        guild = None
        if player_data.get("guild"):
            guild, created = Guild.objects.get_or_create(
                name=player_data.get("guild").get("name"), defaults={
                    "description":
                        player_data.get("guild").get("description", None)}
            )
        if race_data.get("skills"):
            for skill_data in (race_data.get("skills") or []):
                skill, created = Skill.objects.get_or_create(
                    name=skill_data.get("name"), defaults={
                        "bonus": str(skill_data.get("bonus", "")),
                        "race": race}
                )
        player, created = Player.objects.get_or_create(
            nickname=nickname, defaults={
                "email": player_data.get("email"),
                "bio": player_data.get("bio", ""),
                "race": race,
                "guild": guild}
        )


if __name__ == "__main__":
    main()

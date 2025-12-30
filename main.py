import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as json_file:
        data = json.load(json_file)
        for nickname, player_data in data.items():
            race_data = player_data["race"]
            race, _ = Race.objects.get_or_create(
                name=race_data["name"],
                defaults={"description": race_data.get("description", "")}
            )

            guild = None
            if player_data["guild"]:
                guild_data = player_data["guild"]
                guild, _ = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    defaults={"description": guild_data.get("description", "")}
                )

            # Створення або отримання скілів, пов’язаних із расою
            for skill in race_data.get("skills", []):
                skill_obj, _ = Skill.objects.get_or_create(
                    name=skill["name"],
                    defaults={"bonus": skill.get("bonus", "")},
                    race=race  # Вказуємо зв’язок зі створеною расою
                )

            # Створення гравця
            Player.objects.create(
                nickname=nickname,
                email=player_data["email"],
                bio=player_data["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()

import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, player_data in data.items():
        race_data = player_data["race"]
        guild_data = player_data.get("guild")

        try:
            race = Race.objects.get(name=race_data["name"])
        except Race.DoesNotExist:
            race = Race(
                name=race_data["name"],
                description=race_data.get("description")
            )
            race.save()

        guild = None
        if guild_data:
            try:
                guild = Guild.objects.get(name=guild_data["name"])
            except Guild.DoesNotExist:
                guild = Guild(
                    name=guild_data["name"],
                    description=guild_data.get("description")
                )
                guild.save()

        try:
            Player.objects.get(nickname=nickname)
        except Player.DoesNotExist:
            player = Player(
                nickname=nickname,
                email=player_data["email"],
                bio=player_data["bio"],
                race=race,
                guild=guild,
            )
            player.save()

        for skill_data in race_data.get("skills", []):
            try:
                Skill.objects.get(name=skill_data["name"], race=race)
            except Skill.DoesNotExist:
                Skill(
                    name=skill_data["name"],
                    bonus=skill_data["bonus"],
                    race=race).save()


if __name__ == "__main__":
    main()

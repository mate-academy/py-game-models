import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", encoding="utf-8") as f:
        players = json.load(f)

    for nickname, player_data in players.items():
        player = Player()
        player.nickname = nickname
        player.email = player_data["email"]
        player.bio = player_data["bio"]

        race_data = player_data["race"]

        player.race = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )[0]

        for skill in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=player.race
            )

        guild_data = player_data.get("guild")
        if isinstance(guild_data, dict):
            player.guild = Guild.objects.get_or_create(**guild_data)[0]

        player.save()


if __name__ == "__main__":
    main()

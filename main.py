import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as read_file:
        players = json.load(read_file)

    for nickname, player_data in players.items():

        race_data = player_data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )

        skill_list = race_data["skills"]
        for skill_data in skill_list:
            Skill.objects.get_or_create(
                name=skill_data.get("name"),
                race=race,
                defaults={"bonus": skill_data.get("bonus")}
            )

        guild_data = player_data.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description", "")},
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data.get("email"),
                "bio": player_data.get("bio"),
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()

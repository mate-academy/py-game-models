import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json") as f:
        players_data = json.load(f)

    for player in players_data:
        nickname = player
        email = players_data[player]["email"]
        bio = players_data[player]["bio"]


        race_name = players_data[player]["race"]["name"]
        race_description = players_data[player]["race"]["description"]
        race_obj, _ = Race.objects.update_or_create(
            name=race_name,
            defaults={
                "description": race_description
                if race_description is not None
                else ""
            },
        )

        for skill in players_data[player]["race"]["skills"]:
            Skill.objects.update_or_create(
                name=skill["name"],
                race=race_obj,
                defaults={"bonus": skill["bonus"]},
            )

        if players_data[player]["guild"]:
            guild_name = players_data[player]["guild"]["name"]
            guild_description = players_data[player]["guild"]["description"]
            guild_obj, _ = Guild.objects.update_or_create(
                name=guild_name,
                defaults={"description": guild_description},
            )
        else:
            guild_obj = None

        Player.objects.update_or_create(
            nickname=nickname,
            defaults={
                "email": email,
                "bio": bio,
                "race": race_obj,
                "guild": guild_obj,
            }
        )


if __name__ == "__main__":
    main()

import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for nickname, player_data in players.items():

        race_info = player_data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_info["name"],
            defaults={"description": race_info.get("description", "")}
        )

        skills = race_info.get("skills", [])
        for skill in skills:
            skill_obj, _ = Skill.objects.get_or_create(
                name=skill["name"],
                race=race,
                defaults={"bonus": skill.get("bonus", "")})

        guilds = player_data.get("guild")
        if guilds:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guilds["name"],
                defaults={"description": guilds.get("description")})
        else:
            guild_obj = None

        Player.objects.get_or_create(nickname=nickname,
                                     defaults={"email": player_data["email"],
                                               "bio": player_data["bio"],
                                               "race": race,
                                               "guild": guild_obj}
                                     )


if __name__ == "__main__":
    main()

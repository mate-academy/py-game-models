import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as json_file:
        players = json.load(json_file)

    for player_name, player in players.items():
        guild_name = player.get("guild")
        nickname = player.get("nickname", f"{player_name}")
        email = player.get("email")
        race_name = player.get("race")
        bio_discord = player.get("bio")
        skills = race_name.get("skills", [])
        skill_name = [skill.get("name") for skill in skills]

        guild, _ = Guild.objects.get_or_create(
            name=guild_name["name"] if guild_name else "Unknown",
            description=(
                guild_name.get("description") if guild_name else "No description"
            ),
        )
        race, _ = Race.objects.get_or_create(
            name=race_name["name"],
            description=race_name["description"])
        for skill_name in skill_name:
            Skill.objects.get_or_create(name=skill_name, race=race)

        player_obj, _ = Player.objects.get_or_create(nickname=nickname,
                                                     email=email,
                                                     bio=bio_discord,
                                                     race=race,
                                                     guild=guild
                                                     )
    pass


if __name__ == "__main__":
    main()

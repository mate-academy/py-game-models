import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as json_file:
        players = json.load(json_file)

    for player in players:
        guild_name = player.get("guild")
        nickname = player.get("nickname")
        email = player.get("email")
        race_name = player.get("race")
        bio_discord = player.get("bio")
        skill_name = player.get("skill")

        guild, _ = Guild.objects.get_or_create(name=guild_name)
        race, _ = Race.objects.get_or_create(name=race_name)
        skill, _ = Skill.objects.get_or_create(name=skill_name)

        player_obj, _ = Player.objects.get_or_create(nickname=nickname,
                                                     email=email,
                                                     bio=bio_discord,
                                                     race=race,
                                                     guild=guild
                                                     )
    pass


if __name__ == "__main__":
    main()

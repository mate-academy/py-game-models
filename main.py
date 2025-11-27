import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, player in data.items():
        race_name = player.get("race").get("name")
        race_description = player.get("race").get("description")
        race, created_race = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description}
        )

        if player.get("guild"):
            guild_info = player.get("guild")
            guild_name = guild_info.get("name")
            guild_description = guild_info.get("description")
            guild, created_guild = Guild.objects.get_or_create(
                name=guild_name, defaults={"description": guild_description}
            )
        else:
            guild = None

        skills = player.get("race").get("skills", [])
        for _skill in skills:
            skill_name = _skill.get("name")
            skill_bonus = _skill.get("bonus")
            skill, created_skill = Skill.objects.get_or_create(
                name=skill_name,
                defaults={"bonus": skill_bonus, "race": race}
            )

        email = player.get("email")
        bio = player.get("bio")
        player_obj , created_player = Player.objects.get_or_create(
            nickname=nickname,
            defaults={"email": email,
                      "bio": bio,
                      "race": race,
                      "guild": guild}
        )


if __name__ == "__main__":
    main()

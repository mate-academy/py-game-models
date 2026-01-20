import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for nickname, player_data in data.items():

        race_info = player_data.get("race")

        if not isinstance(race_info, dict) or "name" not in race_info:
            continue

        race_obj, _ = (
            Race.objects.get_or_create(
                name=race_info["name"],
                defaults={"description": race_info.get("description", "")})
        )

        guild_info = player_data.get("guild")

        if guild_info is None:
            guild_obj = None
        elif not isinstance(guild_info, dict) or "name" not in guild_info:
            guild_obj = None
        else:
            guild_obj, _ = (
                Guild.objects.get_or_create(
                    name=guild_info["name"],
                    defaults={
                        "description": guild_info.get("description", "")
                    })
            )

        player_obj, created = (
            Player.objects.get_or_create(
                nickname=nickname,
                defaults={"email": player_data.get("email", ""),
                          "bio": player_data.get("bio", ""),
                          "race": race_obj,
                          "guild": guild_obj})
        )

        if not created:
            email = player_data.get("email")
            if email is not None:
                player_obj.email = email
            bio = player_data.get("bio")
            if bio is not None:
                player_obj.bio = bio
            if player_data.get("race") is not None:
                player_obj.race = race_obj
            if player_data.get("guild") is not None:
                player_obj.guild = guild_obj
            player_obj.save()

        skills = race_info.get("skills", [])

        for skill in skills:
            name = skill.get("name")
            bonus = skill.get("bonus")
            if not name or not bonus:
                continue
            skill_obj, created = Skill.objects.get_or_create(
                name=name,
                defaults={"bonus": bonus, "race": race_obj}
            )

            if not created:
                changed = False
                if skill_obj.bonus != bonus:
                    skill_obj.bonus = bonus
                    changed = True
                if changed:
                    skill_obj.save()


if __name__ == "__main__":
    main()

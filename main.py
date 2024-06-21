import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file_info:
        all_users_info = json.load(file_info)

    for user in all_users_info:
        new_race, created = Race.objects.get_or_create(
            name=all_users_info[user]["race"]["name"],
            description=all_users_info[user]["race"]["description"]
        )
        for skill in all_users_info[user]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=new_race
            )
        if all_users_info[user]["guild"]:
            new_guild, created = Guild.objects.get_or_create(
                name=all_users_info[user]["guild"]["name"],
                description=all_users_info[user]["guild"]["description"]
            )
        else:
            new_guild = None
        Player.objects.create(
            nickname=user,
            email=all_users_info[user]["email"],
            bio=all_users_info[user]["bio"],
            race=new_race,
            guild=new_guild if new_guild else None
        )


if __name__ == "__main__":
    main()

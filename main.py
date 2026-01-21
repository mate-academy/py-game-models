import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    for nickname, pdata in data.items():
        # race
        race_data = pdata["race"]
        race_obj, created = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )
        if created:
            print(f"new object of Race is created: {race_obj.name}")
        else:
            print(f"object of Race is existed: {race_obj.name}")
            if race_obj.description != race_data.get("description", ""):
                race_obj.description = race_data.get("description", "")
                race_obj.save()
                print(f"description is updated: {race_obj.name}")

        # skill
        for skill_data in race_data.get("skills", []):
            skill_obj, created = Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race_obj
                }
            )
            if created:
                print(f"new Skill is created: {skill_obj.name}")
            else:
                print(f"skill is existed: {skill_obj.name}")
                if (skill_obj.bonus != skill_data["bonus"]
                        or skill_obj.race != race_obj):
                    skill_obj.bonus = skill_data["bonus"]
                    skill_obj.race = race_obj
                    skill_obj.save()
                    print(f"skill is updated: {skill_obj.name}")

        # guild
        guild_data = pdata.get("guild")
        guild_obj = None
        if guild_data:
            guild_obj, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )
            if created:
                print(f"new Guild is created: {guild_obj.name}")
            else:
                print(f"Guild is existed: {guild_obj.name}")
                if guild_obj.description != guild_data.get("description"):
                    guild_obj.description = guild_data.get("description")
                    guild_obj.save()
                    print(f"description is updated: {guild_obj.name}")

        # create/update the player
        player_obj, created = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": pdata["email"],
                "bio": pdata["bio"],
                "race": race_obj,
                "guild": guild_obj,
            }
        )
        if created:
            print(f"new Player is created: {player_obj.nickname}")
        else:
            print(f"player is existed: {player_obj.nickname}")
            player_obj.email = pdata["email"]
            player_obj.bio = pdata["bio"]
            player_obj.race = race_obj
            player_obj.guild = guild_obj
            player_obj.save()
            print(f"player is updated: {player_obj.nickname}")


if __name__ == "__main__":
    main()

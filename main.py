import init_django_orm  # noqa: F401
import json


from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        data = json.load(players_file)
    print(list(data))

    for nickname, pdata in data.items():
        nickname = nickname[:255]
        email = pdata.get("email", "")[:255]
        raw_bio = pdata.get("bio")
        bio = (raw_bio or "")[:255]
        race_data = pdata.get("race")
        if race_data:
            race_name = race_data.get("name")
            race_description = race_data.get("description")
        else:
            race_name = ""
            race_description = ""
        race, _ = (Race.objects.
                   get_or_create(name=race_name,
                                 defaults={
                                     "description": race_description}))

        for skill in race_data.get("skills", []):
            skill_name = (skill.get("name") or "")[:255]
            skill_bonus = (skill.get("bonus") or "")[:255]
            skill, _ = (Skill.objects.
                        get_or_create(
                            name=skill_name,
                            race=race,
                            defaults={"bonus": skill_bonus}))
        guild_data = pdata.get("guild")
        if guild_data:
            guild_name = guild_data.get("name")[:255]
            guild_description = guild_data.get("description")
            guild, _ = (Guild.objects.
                        get_or_create(
                            name=guild_name,
                            defaults={"description": guild_description}))
        else:
            guild = None
        Player.objects.create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race,
            guild=guild or None,
        )


if __name__ == "__main__":
    main()

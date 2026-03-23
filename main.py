import init_django_orm  # noqa: F401


from db.models import Race, Skill, Player, Guild


import json


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, playerinfo in players.items():
        race_data = playerinfo.get("race")
        if not isinstance(race_data, dict):
            continue
        race_name = race_data.get("name")
        race_description = race_data.get("description")
        guild_data = playerinfo.get("guild")
        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description})
        if guild_data:
            guild_name = guild_data.get("name")
            guild_description = guild_data.get("description")
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description})
        else:
            guild = None
        skills = race_data.get("skills", [])
        for skill_ in skills:
            Skill.objects.get_or_create(
                name=skill_.get("name"),
                defaults={"bonus": skill_.get("bonus"), "race": race})

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": playerinfo.get("email"),
                "bio": playerinfo.get("bio"),
                "race": race,
                "guild": guild})


if __name__ == "__main__":
    main()

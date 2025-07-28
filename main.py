import json
from db.models import Player, Race, Skill, Guild


def main() -> None:
    with open("players.json") as file:
        players_data = json.load(file)

    for key, value in players_data.items():
        race_data = value["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )

        for skill_data in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )

        guild_data = value.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        player, _ = Player.objects.update_or_create(
            nickname=key,
            defaults={
                "email": value["email"],
                "bio": value.get("bio"),
                "race": race,
                "guild": guild
            }
        )

        for skill_data in race_data["skills"]:
            skill = Skill.objects.get(name=skill_data["name"])
            player.skills.add(skill)


if __name__ == "__main__":
    main()

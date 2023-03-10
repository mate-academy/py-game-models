import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as config_file:
        data = json.load(config_file)

    for name in data:
        config_race_name = data[name]["race"].get("name")
        config_race_description = data[name]["race"].get("description")

        race_entry, _ = Race.objects.get_or_create(
            name=config_race_name,
            defaults={"description": config_race_description},
        )

        config_skills_list = data[name]["race"].get("skills", [])
        for skill in config_skills_list:
            conf_skill_name = skill.get("name")
            conf_skill_bns = skill.get("bonus")
            skill_entry, _ = Skill.objects.get_or_create(
                name=conf_skill_name,
                defaults={"bonus": conf_skill_bns, "race": race_entry},
            )

        if data[name]["guild"]:
            config_guild_name = (
                data[name]["guild"].get("name")
                if data[name]["guild"]
                else None
            )
            config_guild_description = (
                data[name]["guild"].get("description")
                if data[name]["guild"]
                else None
            )

            guild_entry, _ = Guild.objects.get_or_create(
                name=config_guild_name,
                defaults={"description": config_guild_description},
            )

        config_player_nickname = name
        config_email = data[name].get("email")
        config_bio = data[name].get("bio")
        Player.objects.create(
            nickname=config_player_nickname,
            email=config_email,
            bio=config_bio,
            race=race_entry,
            guild=guild_entry if data[name]["guild"] else None ,
        )


if __name__ == "__main__":
    main()

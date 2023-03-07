import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as config_file:
        data = json.load(config_file)

    for name in data:
        config_race_name = (
            data[name]["race"]["name"]
            if data[name]["race"]["name"]
            else None
        )
        config_race_description = (
            data[name]["race"]["description"]
            if data[name]["race"]["description"]
            else None
        )
        if not Race.objects.filter(name=config_race_name).exists():
            race_entry = Race.objects.create(
                name=config_race_name,
                description=config_race_description
            )
            config_skills_list = data[name]["race"]["skills"]
            if config_skills_list:
                for skill in config_skills_list:
                    conf_skill_name = skill["name"] if skill["name"] else None
                    conf_skill_bns = skill["bonus"] if skill["bonus"] else None
                    if not Skill.objects.filter(
                            name=conf_skill_name
                    ).exists():
                        Skill.objects.create(
                            name=conf_skill_name,
                            bonus=conf_skill_bns,
                            race=race_entry,
                        )
        if data[name]["guild"] is not None:
            config_guild_name = (
                data[name]["guild"]["name"]
                if data[name]["guild"]["name"] else None
            )
            config_guild_description = (
                data[name]["guild"]["description"]
                if data[name]["guild"]["description"]
                else None
            )
            if not Guild.objects.filter(name=config_guild_name).exists():
                guild_entry = Guild.objects.create(
                    name=config_guild_name,
                    description=config_guild_description
                )
        config_player_nickname = name
        config_email = data[name]["email"] if data[name]["email"] else None
        config_bio = data[name]["bio"] if data[name]["bio"] else None
        Player.objects.create(
            nickname=config_player_nickname,
            email=config_email,
            bio=config_bio,
            race=race_entry if data[name]["race"]["name"] else None,
            guild=guild_entry if data[name]["guild"] else None,
        )


if __name__ == "__main__":
    main()

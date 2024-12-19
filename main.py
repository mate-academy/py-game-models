import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_info = json.load(file)

    for player_key, player in players_info.items():
        # RACE
        race_dict = player.get("race")
        if race_dict:
            race_name = race_dict.get("name")
            race_description = race_dict.get("description")
            if race_name:
                race, created = Race.objects.get_or_create(
                    name=race_name,
                    defaults={"description": race_description}
                    if race_description else {}
                )
        # Guild
        guild_dict = player.get("guild")
        if guild_dict:
            guild_name = guild_dict.get("name")
            guild_description = guild_dict.get("description")
            if guild_name:
                guild, created = Guild.objects.get_or_create(
                    name=guild_name,
                    defaults={"description": guild_description}
                    if guild_description else {}
                )
            else:
                guild = None
        else:
            guild = None

        # SKILL
        if race_dict:
            skill_dict = race_dict.get("skills")
            if skill_dict:
                for skills in skill_dict:
                    skill_name = skills.get("name")
                    skill_bonus = skills.get("bonus")
                    if skill_name:
                        skill, created = Skill.objects.get_or_create(
                            name=skill_name,
                            defaults={"bonus": skill_bonus, "race": race}
                            if skill_bonus else {"race": race}
                        )
        # Player
        email = player.get("email", None)
        bio = player.get("bio", None)

        player_obj, created = Player.objects.get_or_create(
            nickname=player_key,
            defaults={
                "email": email,
                "bio": bio,
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()

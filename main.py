import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f_in:
        player_profile = json.load(f_in)
    if isinstance(player_profile, dict):
        player_list = player_profile.items()
    elif isinstance(player_profile, list):
        player_list = ((item["nickname"], item) for item in player_profile)
    else:
        raise ValueError("players.json must contain a list or dict of players")
    for nickname, player_data in player_list:
        race_data = player_data.get("race", "")
        if not race_data:
            continue
        race, created = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={"description": race_data.get("description", "")})
        for skill_data in race_data.get("skills", []):
            skill_name = skill_data.get("name", "")
            if not skill_name:
                continue
            skill, created = Skill.objects.get_or_create(
                name=skill_name,
                race=race,
                defaults={"bonus": skill_data.get("bonus", "")})
        guild = None
        guild_info = player_data.get("guild", "")
        if guild_info and isinstance(guild_info, dict):
            guild_name = guild_info.get("name", "")
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_info.get("description", "")},)

        player, created = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data.get("email", ""),
                "bio": player_data.get("bio", ""),
                "race": race,
                "guild": guild})


if __name__ == "__main__":
    main()

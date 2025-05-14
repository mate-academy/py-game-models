import django
import init_django_orm  # noqa: F401
import json
import os
from db.models import Race, Skill, Player, Guild

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()


def main() -> None:
    with open("players.json") as file:
        players_data = json.load(file)

    print(f"Carregados {len(players_data)} jogadores do arquivo JSON")
    process_players_data(players_data)


def process_players_data(players_data: dict) -> None:
    for player, data in players_data.items():
        race_data = data.get("race")
        if race_data:
            race = process_race(race_data)
        else:
            continue

        guild_data = data.get("guild")
        guild = process_guild(guild_data) if guild_data else None

        process_player(player, data, race, guild)


def process_race(race_data: dict) -> Race:
    race_name = race_data.get("name")
    if not race_name:
        return None

    race, created = Race.objects.get_or_create(
        name=race_name,
        defaults={"description": race_data.get("description", "")}
    )

    skills_data = race_data.get("skills", [])
    for skill_data in skills_data:
        process_skill(skill_data, race)

    return race


def process_skill(skill_data: dict, race: Race) -> None:
    skill_name = skill_data.get("name")
    if not skill_name:
        return None

    Skill.objects.get_or_create(
        name=skill_name,
        race=race,
        defaults={"bonus": skill_data.get("bonus", " ")}
    )


def process_guild(guild_data: dict) -> Guild:
    guild_name = guild_data.get("name")
    if not guild_name:
        return None

    guild, _ = Guild.objects.get_or_create(
        name=guild_name,
        defaults={"description": guild_data.get("description")}
    )

    return guild


def process_player(
        nickname: str,
        player_data: dict,
        race: Race,
        guild: Guild
) -> None:
    if not nickname:
        return None

    player, created = Player.objects.get_or_create(
        nickname=nickname,
        defaults={
            "email": player_data.get("email", ""),
            "bio": player_data.get("bio", ""),
            "race": race,
            "guild": guild
        }
    )

    if not created:
        player.email = player_data.get("email", player.email)
        player.bio = player_data.get("bio", player.bio)
        player.race = race if race else player.race
        player.guild = guild if guild else player.guild
        player.save()


if __name__ == "__main__":
    main()

import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    # Carregar dados do arquivo JSON
    with open("players.json", "r") as file:
        data = json.load(file)

    # Criar ou obter as raças
    for race_data in data["races"]:
        Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]}
        )

    # Criar ou obter as guildas
    for guild_data in data["guilds"]:
        Guild.objects.get_or_create(
            name=guild_data["name"],
            defaults={"description": guild_data["description"]}
        )

    # Criar ou obter as habilidades
    for skill_data in data["skills"]:
        race = Race.objects.get(name=skill_data["race"])
        Skill.objects.get_or_create(
            name=skill_data["name"],
            defaults={
                "bonus": skill_data["bonus"],
                "race": race
            }
        )

    # Criar os jogadores
    for player_data in data["players"]:
        race = Race.objects.get(name=player_data["race"])

        guild = None
        if player_data["guild"] is not None:
            guild = Guild.objects.get(name=player_data["guild"])

        Player.objects.get_or_create(
            nickname=player_data["nickname"],
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()

import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Guild, Player


def main() -> None:
    # 1. Ler os dados do arquivo JSON de forma segura com encoding UTF-8
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)

    # 2. Percorrer os dados e usar get_or_create para evitar duplicados
    for player_name, data in players_data.items():
        # Obter ou criar a Raça (Race)
        race, _ = Race.objects.get_or_create(
            name=data["race"]["name"],
            defaults={"description": data["race"].get("description", "")}
        )

        # Obter ou criar as Habilidades (Skills) da raça
        for skill_data in data["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race
                }
            )

        # Obter ou criar a Guilda (Guild) se o jogador fizer parte de uma
        guild = None
        if data.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=data["guild"]["name"],
                defaults={"description": data["guild"].get("description")}
            )

        # Criar ou obter o Jogador (Player) vinculando suas chaves estrangeiras
        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": data["email"],
                "bio": data["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()

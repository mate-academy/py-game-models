import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Guild, Player


def main() -> None:
    # 1. Abrir e ler o arquivo JSON com os dados dos jogadores
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)

    # 2. Percorrer cada jogador do arquivo usando um loop for
    for username, data in players_data.items():
        # Criar ou buscar a Raça (usando get_or_create para não duplicar)
        race_instance, _ = Race.objects.get_or_create(
            name=data["race"]["name"],
            defaults={"description": data["race"].get("description")}
        )

        # Criar ou buscar as Habilidades desta raça
        for skill_data in data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race_instance
                }
            )

        # Criar ou buscar a Guilda (se o jogador tiver uma guilda)
        guild_instance = None
        if data.get("guild"):
            guild_instance, _ = Guild.objects.get_or_create(
                name=data["guild"]["name"],
                defaults={"description": data["guild"].get("description")}
            )

        # Criar ou buscar o Jogador usando o nickname único
        Player.objects.get_or_create(
            nickname=username,
            defaults={
                "email": data["email"],
                "bio": data["bio"],
                "race": race_instance,
                "guild": guild_instance
            }
        )


if __name__ == "__main__":
    main()

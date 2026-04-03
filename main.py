import os
import json
from db.models import Race, Skill, Guild, Player

JSON_FILE = os.path.join(os.path.dirname(__file__), "players.json")


def main() -> None:
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        # Carrega como um dicionário
        players_data = json.load(f)

    # Itera sobre as chaves (nicknames) e os valores (dados do jogador)
    for nickname, player_data in players_data.items():

        # 1. Processar Raça e Skills
        race_data = player_data.get("race", {})
        race_obj = None

        if race_data:
            # Incluímos o description no defaults para passar no test_races
            race_obj, _ = Race.objects.get_or_create(
                name=race_data.get("name"),
                defaults={"description": race_data.get("description")}
            )

            # Criar skills da raça
            for skill_data in race_data.get("skills", []):
                Skill.objects.get_or_create(
                    name=skill_data.get("name"),
                    defaults={
                        "bonus": skill_data.get("bonus"),
                        "race": race_obj
                    }
                )

        # 2. Processar Guild
        # Pode ser None, então não usamos {} como fallback
        guild_data = player_data.get("guild")
        guild_obj = None

        if guild_data:
            # Incluímos o description no defaults para passar no test_guilds
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description")}
            )

        # 3. Criar Player
        # Preenchendo todos os campos esperados no test_players
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data.get("email"),
                "bio": player_data.get("bio"),
                "race": race_obj,
                "guild": guild_obj
            }
        )


if __name__ == "__main__":
    main()

import json
from django.db import transaction
from db.models import Race, Skill, Guild, Player

def main():
    with open("players.json", "r", encoding="utf-8") as f:
        players_data = json.load(f)

    with transaction.atomic():
        for player_data in players_data:
            # Criar ou obter raça
            race, _ = Race.objects.get_or_create(
                name=player_data["race"]["name"],
                defaults={"description": player_data["race"].get("description", "")}
            )

            # Criar ou obter habilidades da raça
            for skill_data in player_data["race"].get("skills", []):
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    race=race,
                    defaults={"bonus": skill_data.get("bonus", "")}
                )

            # Criar ou obter guilda
            guild_name = player_data.get("guild")
            guild = None
            if guild_name:
                guild, _ = Guild.objects.get_or_create(name=guild_name)

            # Criar jogador
            Player.objects.get_or_create(
                nickname=player_data["nickname"],
                defaults={
                    "email": player_data.get("email", ""),
                    "bio": player_data.get("bio", ""),
                    "race": race,
                    "guild": guild,
                }
            )

if __name__ == "__main__":
    main()

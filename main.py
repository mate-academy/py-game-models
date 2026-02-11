import json
import init_django_orm  # noqa: F401

from typing import Optional

from db.models import Race, Skill, Player, Guild


def load_json_data(filepath: str) -> dict:
    """Carrega dados do arquivo JSON."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Erro: Arquivo '{filepath}' não encontrado!")
        return {}
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        return {}


def create_races(races_data: list) -> None:
    """Cria ou obtém as raças do banco de dados."""
    print("Criando raças...")
    for race_data in races_data:
        race, created = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={"description": race_data.get("description", "")}
        )
        status = "✓ criada" if created else "- já existe"
        print(f"  {status}: '{race.name}'")


def create_guilds(guilds_data: list) -> None:
    """Cria ou obtém as guildas do banco de dados."""
    print("\nCriando guildas...")
    for guild_data in guilds_data:
        guild, created = Guild.objects.get_or_create(
            name=guild_data.get("name"),
            defaults={"description": guild_data.get("description")}
        )
        status = "✓ criada" if created else "- já existe"
        print(f"  {status}: '{guild.name}'")


def create_skills(skills_data: list) -> None:
    """Cria ou obtém as habilidades do banco de dados."""
    print("\nCriando habilidades...")
    for skill_data in skills_data:
        try:
            race = Race.objects.get(name=skill_data.get("race"))
            skill, created = Skill.objects.get_or_create(
                name=skill_data.get("name"),
                defaults={
                    "bonus": skill_data.get("bonus", ""),
                    "race": race
                }
            )
            status = "✓ criada" if created else "- já existe"
            print(f"  {status}: '{skill.name}' (raça: '{race.name}')")
        except Race.DoesNotExist:
            race_name = skill_data.get("race")
            skill_name = skill_data.get("name")
            print(f"  ✗ Erro: Raça '{race_name}' não encontrada")
            print(f"    para habilidade '{skill_name}'")


def get_player_guild(
    guild_name: str,
    player_nickname: str
) -> Optional[Guild]:
    """Obtém a guilda do jogador ou retorna None."""
    if not guild_name:
        return None

    try:
        return Guild.objects.get(name=guild_name)
    except Guild.DoesNotExist:
        print(f"  ✗ Aviso: Guilda '{guild_name}' não encontrada")
        print(f"    para jogador '{player_nickname}'")
        return None


def create_players(players_data: list) -> None:
    """Cria ou obtém os jogadores do banco de dados."""
    print("\nCriando jogadores...")
    for player_data in players_data:
        try:
            race = Race.objects.get(name=player_data.get("race"))
            guild = get_player_guild(
                player_data.get("guild"),
                player_data.get("nickname")
            )

            player, created = Player.objects.get_or_create(
                nickname=player_data.get("nickname"),
                defaults={
                    "email": player_data.get("email", ""),
                    "bio": player_data.get("bio", ""),
                    "race": race,
                    "guild": guild
                }
            )

            guild_info = f" (guilda: '{guild.name}')" if guild else ""
            status = "✓ criado" if created else "- já existe"
            print(f"  {status}: '{player.nickname}'{guild_info}")

        except Race.DoesNotExist:
            race_name = player_data.get("race")
            player_name = player_data.get("nickname")
            print(f"  ✗ Erro: Raça '{race_name}' não encontrada")
            print(f"    para jogador '{player_name}'")


def main() -> None:
    """
    Carrega dados do arquivo players.json e popula o banco de dados
    com raças, guildas, habilidades e jogadores.
    """
    data = load_json_data("players.json")

    if not data:
        return

    create_races(data.get("races", []))
    create_guilds(data.get("guilds", []))
    create_skills(data.get("skills", []))
    create_players(data.get("players", []))

    print("\n✅ Importação concluída!")


if __name__ == "__main__":
    main()

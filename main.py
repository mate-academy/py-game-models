import json
import os
from db.models import Race, Skill, Guild, Player
from typing import List, Dict

# Constrói o caminho absoluto para o diretório onde este script (main.py) está
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Constrói o caminho para players.json (um nível acima, na raiz do projeto)
PLAYERS_JSON_PATH = os.path.join(SCRIPT_DIR, "..", "players.json")


def load_races(race_data: List[Dict]) -> None:
    print(f"--- load_races: Tentando carregar {len(race_data)} raças. ---")
    for race_info in race_data:
        obj, created = Race.objects.get_or_create(
            name=race_info["name"],
            defaults={"description": race_info.get("description", "")},
        )
        print(f"Raça: {obj.name}, Criada: {created}")
    count = Race.objects.count()
    print(f"Total de Raças no BD após load_races: {count}")


def load_skills(skill_data: List[Dict]) -> None:
    print(
        f"--- load_skills: Tentando carregar {len(skill_data)} "
        "habilidades. ---"
    )
    if not Race.objects.exists() and skill_data:
        print(
            "!!! AVISO: Nenhuma raça no BD. Habilidades que dependem de "
            "raças não podem ser carregadas. !!!"
        )
        return

    for skill_info in skill_data:
        try:
            race_obj = Race.objects.get(name=skill_info["race"])
            obj, created = Skill.objects.get_or_create(
                name=skill_info["name"],
                race=race_obj,
                defaults={"bonus": skill_info.get("bonus", "")},
            )
            print(
                f"Habilidade: {obj.name} para Raça: {race_obj.name}, "
                f"Criada: {created}"
            )
        except Race.DoesNotExist:
            race_name = skill_info["race"]
            skill_name = skill_info["name"]
            msg = (
                f"!!! ERRO: Raça '{race_name}' não encontrada para a "
                f"habilidade '{skill_name}'. Pulando habilidade."
            )
            print(msg)
        except Exception as e:
            skill_name_safe = skill_info.get('name', 'DESCONHECIDA')
            print(
                f"!!! ERRO ao carregar habilidade {skill_name_safe}: "
                f"{e} !!!"
            )

    skill_count = Skill.objects.count()
    print(f"Total de Habilidades no BD após load_skills: {skill_count}")


def load_guilds(guild_data: List[Dict]) -> None:
    print(f"--- load_guilds: Tentando carregar {len(guild_data)} guildas. ---")
    for guild_info in guild_data:
        obj, created = Guild.objects.get_or_create(
            name=guild_info["name"],
            defaults={"description": guild_info.get("description")},
        )
        print(f"Guilda: {obj.name}, Criada: {created}")
    count = Guild.objects.count()
    print(f"Total de Guildas no BD após load_guilds: {count}")


def load_players(player_data: List[Dict]) -> None:
    print(
        f"--- load_players: Tentando carregar {len(player_data)} "
        "jogadores. ---"
    )

    for player_info in player_data:
        try:
            race_obj = Race.objects.get(name=player_info["race"])
            guild_obj = None
            if player_info.get("guild"):
                guild_obj = Guild.objects.get(name=player_info["guild"])

            obj, created = Player.objects.get_or_create(
                nickname=player_info["nickname"],
                defaults={
                    "email": player_info["email"],
                    "bio": player_info["bio"],
                    "race": race_obj,
                    "guild": guild_obj,
                },
            )
            print(f"Jogador: {obj.nickname}, Criado: {created}")
        except Race.DoesNotExist:
            race_name = player_info["race"]
            nickname = player_info["nickname"]
            msg = (
                f"!!! ERRO: Raça '{race_name}' não encontrada "
                f"para o jogador '{nickname}'. Pulando jogador. !!!"
            )
            print(msg)
        except Guild.DoesNotExist:
            if player_info.get("guild"):
                guild_name = player_info["guild"]
                nickname = player_info["nickname"]
                msg = (
                    f"!!! ERRO: Guilda '{guild_name}' não encontrada "
                    f"para o jogador '{nickname}'. Pulando jogador. !!!"
                )
                print(msg)
        except Exception as e:
            nickname_safe = player_info.get('nickname', 'DESCONHECIDO')
            print(
                f"!!! ERRO ao carregar jogador {nickname_safe}: "
                f"{e} !!!"
            )

    player_count = Player.objects.count()
    print(f"Total de Jogadores no BD após load_players: {player_count}")


def main() -> None:
    print(f"--- main: Tentando abrir players.json de: {PLAYERS_JSON_PATH} ---")
    print(f"--- main: Diretório de trabalho atual (CWD): {os.getcwd()} ---")
    data = {}
    try:
        with open(PLAYERS_JSON_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
        print("--- main: players.json carregado com sucesso. ---")
    except FileNotFoundError:
        # Removido o print aninhado
        print(
            f"!!! ERRO FATAL: ARQUIVO players.json NÃO ENCONTRADO EM "
            f"{PLAYERS_JSON_PATH} !!!"
        )
        cwd_on_fail = os.getcwd()
        # Corrigida indentação e removido espaço extra no início da f-string
        print(f"Diretório de trabalho atual ao falhar: {cwd_on_fail}")
        return
    except json.JSONDecodeError:
        print(
            f"!!! ERRO FATAL: ARQUIVO players.json em '{PLAYERS_JSON_PATH}' "
            "contém JSON inválido. !!!"
        )
        return

    race_data = data.get("races", [])
    skill_data = data.get("skills", [])
    guild_data = data.get("guilds", [])
    player_data = data.get("players", [])

    msg = (
        f"--- main: Dados crus do JSON - Raças: {len(race_data)}, "
        f"Habilidades: {len(skill_data)}, Guildas: {len(guild_data)}, "
        f"Jogadores: {len(player_data)} ---"
    )
    print(msg)

    if not any([race_data, skill_data, guild_data, player_data]):
        print(
            "--- main: Nenhum dado encontrado para carregar (raças, "
            "habilidades, guildas, jogadores) do JSON. O banco de dados "
            "permanecerá como está. ---"
        )

    load_races(race_data)
    load_skills(skill_data)
    load_guilds(guild_data)
    load_players(player_data)

    print("--- main: Processo de carregamento de dados concluído. ---")


if __name__ == "__main__":
    main()

import json
import os
from db.models import Race, Skill, Guild, Player
from typing import List, Dict

# Obtém o diretório onde este script está localizado
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Caminho para players.json (na mesma pasta que este script)
PLAYERS_JSON_PATH = os.path.join(SCRIPT_DIR, "players.json")


def load_races(race_data: List[Dict]) -> None:
    """Carrega os dados das raças no banco de dados."""
    print(f"--- load_races: Carregando {len(race_data)} raças ---")
    for race_info in race_data:
        name = race_info.get("name")
        if not name:
            print(f"ERRO: Raça sem nome: {race_info}")
            continue
        obj, created = Race.objects.get_or_create(
            name=name,
            defaults={"description": race_info.get("description", "")},
        )
        print(f"Raça: {obj.name}, Criada: {created}")
    print(f"Total de Raças no BD: {Race.objects.count()}")


def load_skills(skill_data: List[Dict]) -> None:
    """Carrega os dados das habilidades no banco de dados."""
    print(f"--- load_skills: Carregando {len(skill_data)} habilidades ---")

    if not Race.objects.exists() and skill_data:
        print("AVISO: Nenhuma raça no BD. Habilidades podem não ser "
              "carregadas corretamente.")

    for skill_info in skill_data:
        try:
            skill_name = skill_info.get("name")
            race_name = skill_info.get("race")

            if not skill_name:
                print(f"ERRO: Habilidade sem nome: {skill_info}")
                continue
            if not race_name:
                print(f"ERRO: Raça não especificada: {skill_info}")
                continue

            race_obj = Race.objects.get(name=race_name)
            obj, created = Skill.objects.get_or_create(
                name=skill_name,
                race=race_obj,
                defaults={"bonus": skill_info.get("bonus", "")},
            )
            msg = (f"Habilidade: {obj.name} (Raça: {race_obj.name}), "
                   f"Criada: {created}")
            print(msg)
        except Race.DoesNotExist:
            msg = (f"ERRO: Raça '{skill_info.get('race')}' não encontrada "
                   f"para '{skill_info.get('name')}'")
            print(msg)
        except KeyError as e:
            print(f"ERRO: Chave ausente {e}: {skill_info}")
        except Exception as e:
            msg = (f"ERRO ao carregar habilidade "
                   f"'{skill_info.get('name', 'DESCONHECIDA')}': {e}")
            print(msg)
    print(f"Total de Habilidades no BD: {Skill.objects.count()}")


def load_guilds(guild_data: List[Dict]) -> None:
    """Carrega os dados das guildas no banco de dados."""
    print(f"--- load_guilds: Carregando {len(guild_data)} guildas ---")
    for guild_info in guild_data:
        name = guild_info.get("name")
        if not name:
            print(f"ERRO: Guilda sem nome: {guild_info}")
            continue
        obj, created = Guild.objects.get_or_create(
            name=name,
            defaults={"description": guild_info.get("description", "")},
        )
        print(f"Guilda: {obj.name}, Criada: {created}")
    print(f"Total de Guildas no BD: {Guild.objects.count()}")


def load_players(player_data: List[Dict]) -> None:
    """Carrega os dados dos jogadores no banco de dados."""
    print(f"--- load_players: Carregando {len(player_data)} jogadores ---")

    for player_info in player_data:
        try:
            nickname = player_info.get("nickname")
            email = player_info.get("email")
            race_name = player_info.get("race")
            guild_name = player_info.get("guild")

            if not nickname:
                print(f"ERRO: Jogador sem nickname: {player_info}")
                continue
            if not email:
                print(f"ERRO: Jogador sem email: {player_info}")
                continue
            if not race_name:
                print(f"ERRO: Jogador sem raça: {player_info}")
                continue

            race_obj = Race.objects.get(name=race_name)
            guild_obj = None
            if guild_name:
                guild_obj = Guild.objects.get(name=guild_name)

            obj, created = Player.objects.get_or_create(
                nickname=nickname,
                defaults={
                    "email": email,
                    "bio": player_info.get("bio", ""),
                    "race": race_obj,
                    "guild": guild_obj,
                },
            )
            print(f"Jogador: {obj.nickname}, Criado: {created}")
        except Race.DoesNotExist:
            msg = (f"ERRO: Raça não encontrada para "
                   f"'{player_info.get('nickname', 'DESCONHECIDO')}'")
            print(msg)
        except Guild.DoesNotExist:
            msg = (f"ERRO: Guilda não encontrada para "
                   f"'{player_info.get('nickname', 'DESCONHECIDO')}'")
            print(msg)
        except KeyError as e:
            print(f"ERRO: Chave ausente {e}: {player_info}")
        except Exception as e:
            msg = (f"ERRO ao carregar jogador "
                   f"'{player_info.get('nickname', 'DESCONHECIDO')}': {e}")
            print(msg)
    print(f"Total de Jogadores no BD: {Player.objects.count()}")


def main() -> None:
    """Função principal que carrega todos os dados do arquivo JSON."""
    print(f"--- main: Tentando abrir players.json em: {PLAYERS_JSON_PATH} ---")

    try:
        with open(PLAYERS_JSON_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
        print("Arquivo carregado com sucesso.")

        if "races" in data:
            load_races(data["races"])
        else:
            print("AVISO: Chave 'races' não encontrada.")

        if "skills" in data:
            load_skills(data["skills"])
        else:
            print("AVISO: Chave 'skills' não encontrada.")

        if "guilds" in data:
            load_guilds(data["guilds"])
        else:
            print("AVISO: Chave 'guilds' não encontrada.")

        if "players" in data:
            load_players(data["players"])
        else:
            print("AVISO: Chave 'players' não encontrada.")

        print("--- Processamento concluído ---")

    except FileNotFoundError:
        print(f"ERRO: Arquivo não encontrado: {PLAYERS_JSON_PATH}")
        print(f"Diretório atual: {os.getcwd()}")
        print("--- Processo falhou ---")
        return
    except json.JSONDecodeError:
        print(f"ERRO: JSON inválido: {PLAYERS_JSON_PATH}")
        print("--- Processo falhou ---")
        return
    except Exception as e:
        print(f"ERRO inesperado: {e}")
        print("--- Processo falhou ---")
        return

    print("--- Script concluído com sucesso ---")


if __name__ == "__main__":
    main()

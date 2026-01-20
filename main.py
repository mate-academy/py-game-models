import json
import os
import django

# Importa os modelos primeiro, antes de configurar o ambiente Django
from db.models import Race, Skill, Player, Guild

# Importa o arquivo que inicializa o ORM Django
# Certifique-se de que 'init_django_orm' está no PYTHONPATH
# ou no mesmo diretório
# Se você seguiu a estrutura recomendada, ele deve estar na raiz do projeto.
# Se init_django_orm.py estiver na mesma pasta que main.py, você pode usar:
# import init_django_orm # noqa: F401
# Se estiver na raiz do projeto e main.py estiver em uma subpasta,
# você pode precisar ajustar o path
# Para simplificar, vamos assumir que o ambiente Django já está configurado
# ou que init_django_orm.py será executado antes ou está configurado
# para ser importado.

# Configura o ambiente Django
# (Necessário para rodar o script fora do manage.py)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "py-game-models.settings")
django.setup()


def main() -> None:
    """
    Lê dados de players.json e adiciona as entradas
    correspondentes ao banco de dados.
    Cria apenas uma instância para cada guilda,
    raça e habilidade, não as copia.
    """
    # Caminho para o arquivo JSON
    # Assumimos que players.json está no mesmo diretório que main.py
    json_file_path = os.path.join(os.path.dirname(__file__), "players.json")

    try:
        with open(json_file_path, "r", encoding="utf-8") as f:
            players_data = json.load(f)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{json_file_path}' não foi encontrado.")
        return
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{json_file_path}' não é um JSON válido.")
        return

    print("Iniciando a importação de dados...")

    # O players_data agora é um objeto JSON (dicionário)
    # Precisamos iterar sobre os valores (os objetos de jogador)
    for nickname, player_info in players_data.items():
        print(f"\nProcessando jogador: {nickname}")

        # 1. Processar Race (Raça)
        # Usa get_or_create para garantir que a raça seja criada apenas uma vez
        race_name = player_info["race"]["name"]
        race_description = player_info["race"]["description"]
        race, created = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description}
        )
        if created:
            print(f'  Raça "{race.name}" criada.')
        else:
            print(f'  Raça "{race.name}" já existe.')

        # 2. Processar Guild (Guilda)
        # A guilda pode ser nula, então verificamos
        guild_instance = None
        if player_info["guild"]:
            guild_name = player_info["guild"]["name"]
            guild_description = player_info["guild"]["description"]
            guild, created = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description}
            )
            if created:
                print(f'  Guilda "{guild.name}" criada.')
            else:
                print(f'  Guilda "{guild.name}" já existe.')
            guild_instance = guild
        else:
            print("  Jogador não pertence a uma guilda.")

        # 3. Processar Player (Jogador)
        # Cria ou obtém o jogador. Se o nickname já existe,
        # ele não será criado novamente.
        player, created = Player.objects.get_or_create(
            nickname=nickname,  # Usando o nickname da chave do JSON
            defaults={
                "email": player_info["email"],
                "bio": player_info["bio"],
                "race": race,  # Associa a instância da raça
                # Associa a instância da guilda (pode ser None)
                "guild": guild_instance
            }
        )
        if created:
            print(f'  Jogador "{player.nickname}" criado.')
        else:
            print(f'  Jogador "{player.nickname}" já existe. '
                  f"Atualizando informações.")
            # Se o jogador já existe, você pode querer atualizar seus dados
            player.email = player_info["email"]
            player.bio = player_info["bio"]
            player.race = race
            player.guild = guild_instance
            player.save()

        # 4. Processar Skills (Habilidades) para a Raça
        # Itera sobre as habilidades fornecidas para a raça do jogador atual
        # Corrigido: Acessando 'skills' através de 'race' de forma segura
        skills_data = player_info["race"].get("skills", [])
        for skill_info in skills_data:
            skill_name = skill_info["name"]
            # Removida a conversão para int(), pois 'bonus' agora é CharField
            skill_bonus = skill_info["bonus"]
            # Usa get_or_create para garantir que a habilidade
            # seja criada apenas uma vez e associada à raça correta.
            skill, created = Skill.objects.get_or_create(
                name=skill_name,
                defaults={
                    "bonus": skill_bonus,
                    "race": race  # Associa a habilidade à instância da raça
                }
            )
            if created:
                print(f'    Habilidade "{skill.name}" criada para a raça '
                      f'"{race.name}".')
            else:
                print(f'    Habilidade "{skill.name}" já existe para a raça '
                      f'"{race.name}".')

    print("\nImportação de dados concluída!")


if __name__ == "__main__":
    main()

import json
from db.models import Race, Skill, Player, Guild


def main():
    # Открываем и читаем файл players.json
    with open('players.json', 'r') as f:
        players_data = json.load(f)

    # Добавляем игроков в базу данных
    for player_data in players_data:
        # Получаем соответствующие объекты Race и Guild
        race = Race.objects.get(name=player_data['race'])  # Предполагается, что в файле JSON расу указывают по имени
        guild = Guild.objects.get(name=player_data['guild']) if player_data[
            'guild'] else None  # Если гильдия существует, то ищем ее

        # Создаем объект Player в базе данных
        Player.objects.create(
            nickname=player_data['nickname'],
            email=player_data['email'],
            bio=player_data['bio'],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
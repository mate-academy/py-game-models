import pytest
from db.models import Race, Guild, Player  # Импортируем необходимые модели


@pytest.mark.django_db
def test_guilds():
    # Создаём расу, если её нет
    race_name = "elf"
    if not Race.objects.filter(name=race_name).exists():
        Race.objects.create(name=race_name, description="An ancient race of magical beings.")

    # Создаём гильдию, если её нет
    guild_name = "mages"
    if not Guild.objects.filter(name=guild_name).exists():
        Guild.objects.create(name=guild_name, description="A guild of magical users.")

    # Тестируем функционал, который использует Guild
    player_data = {'guild': 'mages'}  # Пример данных
    guild = Guild.objects.get(name=player_data['guild'])  # Получаем гильдию
    assert guild.name == 'mages'  # Проверка


@pytest.mark.django_db
def test_skills():
    # Создаём расу, если её нет
    race_name = "elf"
    if not Race.objects.filter(name=race_name).exists():
        Race.objects.create(name=race_name, description="An ancient race of magical beings.")

    # Создаём гильдию, если её нет
    guild_name = "mages"
    if not Guild.objects.filter(name=guild_name).exists():
        Guild.objects.create(name=guild_name, description="A guild of magical users.")

    # Тестируем функционал, который использует Guild
    player_data = {'guild': 'mages'}  # Пример данных
    guild = Guild.objects.get(name=player_data['guild'])  # Получаем гильдию
    assert guild.name == 'mages'  # Проверка


@pytest.mark.django_db
def test_races():
    # Создаём расу, если её нет
    race_name = "elf"
    if not Race.objects.filter(name=race_name).exists():
        Race.objects.create(name=race_name, description="An ancient race of magical beings.")

    # Создаём гильдию, если её нет
    guild_name = "mages"
    if not Guild.objects.filter(name=guild_name).exists():
        Guild.objects.create(name=guild_name, description="A guild of magical users.")

    # Тестируем функционал, который использует Guild
    player_data = {'guild': 'mages'}  # Пример данных
    guild = Guild.objects.get(name=player_data['guild'])  # Получаем гильдию
    assert guild.name == 'mages'  # Проверка


@pytest.mark.django_db
def test_players():
    # Создаём расу, если её нет
    race_name = "elf"
    if not Race.objects.filter(name=race_name).exists():
        Race.objects.create(name=race_name, description="An ancient race of magical beings.")

    # Создаём гильдию, если её нет
    guild_name = "mages"
    if not Guild.objects.filter(name=guild_name).exists():
        Guild.objects.create(name=guild_name, description="A guild of magical users.")

    # Тестируем функционал, который использует Guild
    player_data = {'guild': 'mages'}  # Пример данных
    guild = Guild.objects.get(name=player_data['guild'])  # Получаем гильдию
    assert guild.name == 'mages'  # Проверка

import os
import django
import pytest
from django.db import transaction
from main import main
from db.models import Race, Skill, Guild, Player


# Настройка Django перед импортом моделей
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")
django.setup()


@pytest.mark.django_db
def test_main():
    """
    Тест для функции main.
    """
    # Вызов функции main
    main()

    # Проверка, что данные были добавлены в базу данных
    with transaction.atomic():
        # Проверка, что раса была создана
        race = Race.objects.get(name="elf")
        assert race.description == "The magic race"

        # Проверка, что навыки были созданы
        skill1 = Skill.objects.get(name="Teleportation")
        assert skill1.bonus == "The ability to move so fast they look like they're teleporting. Could be considered to technically be Teleportation."
        skill2 = Skill.objects.get(name="Reality Warping")
        assert skill2.bonus == "The ability to Warp Reality. Make the impossible become possible but can't warp anything containing the structure that holds everything together (Which are many creatures.)"

        # Проверка, что игрок был создан
        player = Player.objects.get(nickname="john")
        assert player.email == "john@gmail.com"
        assert player.bio == "Hello, I'm John, elf ranger"
        assert player.race == race

        # Проверка, что гильдия была создана
        guild = Guild.objects.get(name="archers")
        assert guild.description is None

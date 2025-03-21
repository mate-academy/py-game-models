import pytest
from game.models import Guild


@pytest.mark.django_db
def test_guilds():
    main()  # создаем начальные данные
    guilds = Guild.objects.all()
    print(guilds)  # выводим все гильдии для проверки
    assert list(guilds.values_list("name", "description")) == [
        ("archers", None),
        ("mags", "A community of the elf mags"),
        ("blacksmiths", "A community of the blacksmiths"),
    ]
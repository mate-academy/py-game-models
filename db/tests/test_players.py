import pytest
from game.models import Player


@pytest.mark.django_db
def test_players():
    main()  # создаем начальные данные
    players = Player.objects.all()
    print(players)  # выводим всех игроков для проверки
    assert list(
        players.values_list("nickname", "email", "bio", "race__name", "guild__name")
    ) == [
        ("john", "john@gmail.com", "Hello, I'm John, elf ranger", "elf", "archers"),
        ("max", "max@gmail.com", "Hello, I'm Max, elf mag", "elf", "mags"),
        ("arthur", "arthur@gmail.com", "Arthur, elf mag", "elf", "mags"),
        ("andrew", "andrew@gmail.com", "Hello, I'm Andrew", "human", "blacksmiths"),
        ("nick", "nick@gmail.com", "Hello, I'm Nick", "human", None),
    ]
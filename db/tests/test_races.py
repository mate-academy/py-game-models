import pytest
from game.models import Race


@pytest.mark.django_db
def test_races():
    main()  # создаем начальные данные
    races = Race.objects.all()
    print(races)  # выводим все расы для проверки
    assert list(races.values_list("name", "description")) == [
        ("elf", "The magic race"),
        ("human", "Human race"),
    ]
import pytest
from game.models import Skill


@pytest.mark.django_db
def test_skills():
    main()  # создаем начальные данные
    skills = Skill.objects.all()
    print(skills)  # выводим все навыки для проверки
    assert list(skills.values_list("name", "bonus")) == [
        (
            "Teleportation",
            "The ability to move so fast they look like they're teleporting. "
            "Could be considered to technically be Teleportation.",
        ),
        (
            "Reality Warping",
            "The ability to Warp Reality. Make the impossible become possible "
            "but can't warp anything containing the structure that holds "
            "everything together (Which are many creatures.)",
        ),
    ]
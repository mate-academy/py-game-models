import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,  # skill видаляється, якщо race видаляється
        related_name="skills"
    )

    def __str__(self):
        return f"{self.name} ({self.race})"


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,  # player видаляється якщо race видаляється
        related_name="players"
    )
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,  # player НЕ видаляється якщо guild видаляється
        null=True,
        blank=True,
        related_name="members"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nickname


if __name__ == "__main__":
    main()

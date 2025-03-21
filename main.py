from django.db import models

# Модели
class Guild(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)

class Race(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Skill(models.Model):
    name = models.CharField(max_length=100)
    bonus = models.TextField()
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name="skills", null=True)

class Player(models.Model):
    nickname = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)

# Функция для создания начальных данных
def main():
    # Создание гильдий
    Guild.objects.create(name="archers", description=None)
    Guild.objects.create(name="mags", description="A community of the elf mags")
    Guild.objects.create(name="blacksmiths", description="A community of the blacksmiths")

    # Создание рас
    Race.objects.create(name="elf", description="The magic race")
    Race.objects.create(name="human", description="Human race")

    # Создание навыков
    Skill.objects.create(name="Teleportation", bonus="The ability to move so fast they look like they're teleporting. Could be considered to technically be Teleportation.")
    Skill.objects.create(name="Reality Warping", bonus="The ability to Warp Reality. Make the impossible become possible but can't warp anything containing the structure that holds everything together (Which are many creatures.)")

    # Создание игроков
    race_elf = Race.objects.get(name="elf")
    race_human = Race.objects.get(name="human")

    guild_archers = Guild.objects.get(name="archers")
    guild_mags = Guild.objects.get(name="mags")
    guild_blacksmiths = Guild.objects.get(name="blacksmiths")

    Player.objects.create(nickname="john", email="john@gmail.com", bio="Hello, I'm John, elf ranger", race=race_elf, guild=guild_archers)
    Player.objects.create(nickname="max", email="max@gmail.com", bio="Hello, I'm Max, elf mag", race=race_elf, guild=guild_mags)
    Player.objects.create(nickname="arthur", email="arthur@gmail.com", bio="Arthur, elf mag", race=race_elf, guild=guild_mags)
    Player.objects.create(nickname="andrew", email="andrew@gmail.com", bio="Hello, I'm Andrew", race=race_human, guild=guild_blacksmiths)
    Player.objects.create(nickname="nick", email="nick@gmail.com", bio="Hello, I'm Nick", race=race_human, guild=None)
import init_django_orm  # noqa: F401
import json


from db.models import Race, Skill, Player, Guild


def create_guild(data: dict):
    if 'description' in data :
        print(data['name'])
        return Guild.objects.get_or_create(
            name=data['name'],
            description=data['description'],
        )[0]
    else:
        return Guild.objects.get_or_create(
            name=data['name'],
        )[0]


def main():
    with open('players.json', 'r') as fin:
        raw_players = json.load(fin)

    for raw_player in raw_players:
        player_data = raw_players[raw_player]
        race_data = player_data['race']
        skills_data = race_data['skills']
        guild_data = player_data['guild']
        race = Race.objects.get_or_create(
            name=race_data['name'],
            description=race_data['description']
        )[0]
        race.save()
        skills = [
            Skill.objects.get_or_create(
                name=skill['name'],
                bonus=skill['bonus'],
                race=race,
            )[0]
            for skill in skills_data
        ]
        for skill in skills:
            skill.save()
        guild = None
        if guild_data is not None:
            guild = create_guild(guild_data)
            guild.save()
        player = Player.objects.create(
            nickname=raw_player,
            email=player_data['email'],
            bio=player_data['bio'],
            race=race,
            guild=guild,
        )
        player.save()


if __name__ == "__main__":
    main()

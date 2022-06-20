import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json", 'r') as f:
        content = json.load(f)
        for row in content:
            if not Race.objects.filter(
                    name=content[row]["race"]["name"]).exists():
                Race.objects.create(
                    name=content[row]["race"]["name"],
                    description=content[row]["race"]["description"]
                )
            if isinstance(content[row]["guild"], dict):
                if not Guild.objects.filter(
                        name=content[row]["guild"]["name"]).exists():
                    Guild.objects.create(
                        name=content[row]["guild"]["name"],
                        description=content[row]["guild"]["description"]
                    )

            for i in range(len(content[row]["race"]["skills"])):
                if len(content[row]["race"]["skills"]):
                    skill = content[row]["race"]["skills"][i]["name"]
                    if not Skill.objects.filter(name=skill).exists():
                        Skill.objects.create(
                            name=content[row]["race"]["skills"][i]["name"],
                            bonus=content[row]["race"]["skills"][i]["bonus"],
                            race_id=Race.objects.get(
                                name=content[row]["race"]["name"]).id
                        )
            if not Player.objects.filter(nickname=row).exists():
                try:
                    Player.objects.create(
                        nickname=row,
                        email=content[row]["email"],
                        bio=content[row]["bio"],
                        guild_id=Guild.objects.get(
                            name=content[row]["guild"]["name"]).id,
                        race_id=Race.objects.get(
                            name=content[row]["race"]["name"]).id
                    )
                except TypeError:
                    Player.objects.create(
                        nickname=row,
                        email=content[row]["email"],
                        bio=content[row]["bio"],
                        race_id=Race.objects.get(
                            name=content[row]["race"]["name"]).id
                    )


if __name__ == "__main__":
    main()

import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file_out:
        players_data = json.load(file_out)

    for nickname_, info_ in players_data.items():
        email_ = info_["email"]
        bio_ = info_["bio"]
        guild_ = None
        race_ = None

        if info_["guild"]:
            if not Guild.objects.filter(name=info_["guild"]["name"]).exists():
                guild_ = Guild.objects.create(
                    name=info_["guild"]["name"],
                    description=info_["guild"]["description"]
                )
            else:
                guild_ = Guild.objects.get(name=info_["guild"]["name"])

        if not Race.objects.filter(name=info_["race"]["name"]).exists():
            race_ = Race.objects.create(
                name=info_["race"]["name"],
                description=info_["race"]["description"]
            )
        else:
            race_ = Race.objects.get(name=info_["race"]["name"])

        skills_list = info_["race"]["skills"]
        for skill_ in skills_list:
            if not Skill.objects.filter(name=skill_["name"]).exists():
                Skill.objects.create(
                    name=skill_["name"],
                    bonus=skill_["bonus"],
                    race=race_
                )

        Player.objects.create(
            nickname=nickname_,
            email=email_,
            bio=bio_,
            guild=guild_,
            race=race_
        )


if __name__ == "__main__":
    main()

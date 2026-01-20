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
            guild_, _ = Guild.objects.get_or_create(
                name=info_["guild"]["name"],
                description=info_["guild"]["description"]
            )

        race_, _ = Race.objects.get_or_create(
            name=info_["race"]["name"],
            description=info_["race"]["description"]
        )

        skills_list = info_["race"]["skills"]
        for skill_ in skills_list:
            Skill.objects.get_or_create(
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

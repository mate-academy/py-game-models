from db.models import Skill, Race


def create_skills(users_data: dict) -> list:

    skills_ = {}

    for nickname, other_data in users_data.items():
        skills = other_data["race"]["skills"]
        race_name = other_data["race"]["name"]
        race = Race.objects.get(
            name=race_name
        )
        for skill in skills:
            skill = Skill(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

            skills_[skill.name] = skill

    return list(skills_.values())

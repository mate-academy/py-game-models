from db.models import Skill, Race


def create_skills(users_data):
    for nickname, other_data in users_data.items():
        skills = other_data["race"]["skills"]
        race_name = other_data["race"]["name"]
        race = Race.objects.get(
            name=race_name
        )

        for skill in skills:
            skill_already_exists = Skill.objects.filter(
                name=skill["name"]
            )

            if not skill_already_exists:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

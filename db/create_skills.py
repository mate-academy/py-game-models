from db.models import Skill, Race


def create_skills(users_data):
    for nickname, other_data in users_data.items():
        skills = other_data["race"]["skills"]
        race_name = other_data["race"]["name"]
        race = Race.objects.get(
            name=race_name
        )

        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

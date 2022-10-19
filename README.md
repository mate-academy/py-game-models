# Game models

Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before starting.

## First task:
In `db/models.py` create the following models:

#### 1. Race
Each player should choose a race to play, such as Elf, Dwarf, Human, or Ork.
`Race` has the following fields:
- `name` - a *unique* char field with the maximum length of 255 characters.
- `description` - a text field, can be blank.

#### 2. Skill
Each race has unique skills. Create a model `Skill` for them.
Each skill has:
- `name` - a *unique* char field with a maximum length of 255 characters.
- `bonus` - a char field with a maximum length of 255 characters. 
This field describes what kind of bonus players can get from it. 
- `race` - a foreign key that points to the `Race` model. It shows which race has the corresponding skill.

#### 3. Guild
The player has an opportunity to become a member of a guild. 
It has:
- `name` - a *unique* char field with the maximum length of 255 characters.
- `description` - a text field, can be blank.


#### 4. Player model
And finally, a `Player` model.
It should have the following fields:
- `nickname` - a *unique* char field with a maximum length of 255 characters.
- `email` - an email field with a maximum length of 255 characters.
- `bio` - a char field with a maximum length of 255 characters. 
It stores a short description provided by a user about himself/herself.
- `race` - a foreign key that points to the `Race` model and shows 
the race of the player.
- `guild` - a foreign key that points to the `Guild` model and stores
an id of the guild the player is a member of.
- `created_at` - a DateTime field, that is set with the current time by default.


## Second Task:

Implement function `main()` in `main.py`:

Read data about players from `players.json` and add the corresponding entries to the database.
Note, that some guilds, races and skills are used for different players. Create only one
instance for each guild, race and skill, do not copy them.

**Note**: You can check, if some record already exists using 
`Model.objects.filter(some_field="data").exists()` (returns `True` or `False`)

### Note: Check your code using this [checklist](checklist.md) before pushing your solution.

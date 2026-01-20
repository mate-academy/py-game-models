from pathlib import Path
from db.management.commands.import_players import import_players


def main() -> None:
    pass


def run() -> None:
    file_path = Path("db/players.json")
    import_players(file_path)


if __name__ == "__main__":
    run()

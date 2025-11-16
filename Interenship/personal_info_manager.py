from dataclasses import dataclass, asdict
from typing import List
import json
import os


@dataclass
class Person:
    name: str
    age: int
    city: str
    hobbies: List[str]


class PersonalInformationManager:
    def __init__(self, person: Person | None = None):
        self.person = person

    def set_info(self, name: str, age: int, city: str, hobbies: List[str]) -> None:
        self.person = Person(name=name.strip(), age=int(age), city=city.strip(), hobbies=[h.strip() for h in hobbies])

    def get_info(self) -> Person:
        if not self.person:
            raise ValueError("No person info set yet.")
        return self.person

    def display(self) -> None:
        p = self.get_info()

        title = " Personal Information "
        line = "─" * 50
        print(f"┌{line}┐")
        print(f"│{title.center(50)}│")
        print(f"├{line}┤")
        print(f"│ Name   : {p.name:<38}│")
        print(f"│ Age    : {p.age:<38}│")
        print(f"│ City   : {p.city:<38}│")
        print(f"│ Hobbies: {'':<38}│")
        if p.hobbies:
            for i, h in enumerate(p.hobbies, start=1):
                bullet = f"  {i}. {h}"
                print(f"│ {bullet:<46}│")
        else:
            print(f"│   (none){'':<39}│")
        print(f"└{line}┘")

    # --- Optional: save/load to file (JSON) ---
    def save(self, path: str = "person.json") -> None:
        p = self.get_info()
        with open(path, "w", encoding="utf-8") as f:
            json.dump(asdict(p), f, ensure_ascii=False, indent=2)

    def load(self, path: str = "person.json") -> None:
        if not os.path.exists(path):
            raise FileNotFoundError(f"No saved file at {path}")
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.person = Person(**data)


if __name__ == "__main__":
    pim = PersonalInformationManager()

    pim.set_info(
        name="Basanagouda D",
        age=21,
        city="Bengaluru",
        hobbies=["Coding", "Cricket", "Reading tech blogs"]
    )


    pim.display()


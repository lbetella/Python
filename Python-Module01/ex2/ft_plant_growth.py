class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")

    def age(self) -> None:
        self.age_days += 1

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)


def main() -> None:
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30)
    rose.show()
    initial_height: float = rose.height
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()
    print(f"Growth this week: {round(rose.height - initial_height, 1)}cm")


if __name__ == "__main__":
    main()

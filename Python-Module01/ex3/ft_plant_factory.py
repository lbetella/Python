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
    print("=== Plant Factory Output ===")
    plants_data = [
        ("Rose", 25.0, 30),
        ("Oak", 200.0, 365),
        ("Cactus", 5.0, 90),
        ("Sunflower", 80.0, 45),
        ("Fern", 15.0, 120),
    ]
    for name, height, age in plants_data:
        plant = Plant(name, height, age)
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._statics = self.Statics()

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        self._statics.add_show()

    def age(self) -> None:
        self._age += 1
        self._statics.add_age()

    def grow(self) -> None:
        self._height = round(self._height + 0.8, 1)
        self._statics.add_grow()

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days")

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm")

    @staticmethod
    def is_older_than_a_year(nbr: int) -> bool:
        if nbr > 365:
            return True
        else:
            return False

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    class Statics:
        def __init__(self) -> None:
            self._grow_counter: int = 0
            self._age_counter: int = 0
            self._show_counter: int = 0
            self._shade_counter: int = 0

        def add_grow(self) -> None:
            self._grow_counter += 1

        def add_age(self) -> None:
            self._age_counter += 1

        def add_show(self) -> None:
            self._show_counter += 1

        def add_shade(self) -> None:
            self._shade_counter += 1

        def show(self) -> None:
            print(f"Stats: {self._grow_counter} grow, {self._age_counter} "
                  f"age, {self._show_counter} show")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self.blooming = False

    def show(self) -> None:
        Plant.show(self)
        print(f" Color: {self._color}")
        if self.blooming is True:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")

    def grow(self) -> None:
        self._height = round(self._height + 8.0, 1)
        self._statics.add_grow()

    def bloom(self) -> None:
        self.blooming = True


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        Plant.show(self)
        print(f" Trunk diameter: {self._trunk_diameter}cm")

    def shade(self) -> None:
        print(f"Tree {self._name} now produce a shade of {self._height}cm "
              f"long and {self._trunk_diameter}cm wide.")
        self._statics.add_shade()


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str,
                 nutricional_value: int) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutricional_value = nutricional_value

    def show(self) -> None:
        Plant.show(self)
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutricional value: {self._nutricional_value}")

    def grow(self) -> None:
        self._height = round(self._height + 2.1, 1)
        self._statics.add_grow()

    def age(self) -> None:
        Plant.age(self)
        self._nutricional_value += 1


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seed = 0

    def grow(self) -> None:
        self._height = round(self._height + 30.0, 1)
        self._statics.add_grow()

    def age(self) -> None:
        self._age += 20
        self._statics.add_age()

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seed}")

    def bloom(self) -> None:
        super().bloom()
        self.seed += 42


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print(f"is 400 days more than a year? "
          f"-> {Plant.is_older_than_a_year(400)}")
    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statics for Rose]")
    rose._statics.show()
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    rose._statics.show()
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    oak._statics.show()
    print(f"{oak._statics._shade_counter} shade")
    print("[asking the oak to produce shade]")
    oak.shade()
    print("[statistics for Oak]")
    oak._statics.show()
    print(f"{oak._statics._shade_counter} shade")
    print()
    print("=== Seed")
    sunflower_seed = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower_seed.show()
    print("[make sunflower grow, age and bloom]")
    sunflower_seed.grow()
    sunflower_seed.age()
    sunflower_seed.bloom()
    sunflower_seed.show()
    print("[statistics for Sunflower]")
    sunflower_seed._statics.show()
    print()
    print("=== Anonymous")
    unknown_plant = Plant.anonymous()
    unknown_plant.show()
    print("[statistics for Unknown plant]")
    unknown_plant._statics.show()


if __name__ == "__main__":
    main()

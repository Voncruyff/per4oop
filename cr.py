class Animal:
    # Constructor
    def __init__(self, name):
        self._name = name  # Menggunakan underscore untuk menandakan bahwa ini adalah atribut privat

    # Getter untuk nama
    @property
    def name(self):
        return self._name

    # Setter untuk nama
    @name.setter
    def name(self, new_name):
        self._name = new_name

    # Metode untuk bertarung
    def fight(self):
        print(f"{self._name} is fighting!")

    # Destructor
    def __del__(self):
        print(f"{self._name} has been destroyed.")

# Kelas turunan dari Animal
class Monkey(Animal):
    # Constructor
    def __init__(self, name, favorite_food):
        super().__init__(name)  # Memanggil constructor dari kelas induk
        self.favorite_food = favorite_food

    # Override metode fight()
    def fight(self):
        print(f"{self._name} says: Banana is my favorite food!")

    # Overloading metode fight() dengan parameter tambahan
    def fight_with_weapon(self, weapon=None):
        if weapon:
            print(f"{self._name} is fighting with a {weapon}!")
        else:
            print(f"{self._name} is fighting!")

# Membuat objek dari kelas Monkey
labrador = Monkey("Wukong", "Banana")

# Menggunakan getter untuk mendapatkan nama
print("Nama:", labrador.name)

# Menggunakan setter untuk mengubah nama
labrador.name = "Monkey King"
print("Nama setelah diubah:", labrador.name)

# Memanggil metode fight() yang di-override
labrador.fight()

# Memanggil metode fight_with_weapon() dengan parameter
labrador.fight_with_weapon("stick")

# Menghapus objek
del labrador
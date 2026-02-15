class Pet:
    # ctor
    def __init__(self,name,hunger_level,energy_level,mood):
        """constructor - initialize the pet's status"""
        self.name: str = name
        self.hunger_level: int = hunger_level
        self.energy_level: int = energy_level
        self.mood: str = mood

    # helper method to make updating the mood much easier
    def _update_mood(self):
        if self.hunger_level <= 3 and self.energy_level >= 7:
            self.mood = "Happy"
        elif self.hunger_level <= 6 and self.energy_level >= 4:
            self.mood = "Okay"
        else:
            self.mood = "Grumpy"
        updated_status = f'Name: {self.name} | Hunger: {self.hunger_level} | Energy: {self.energy_level} | Mood: {self.mood}'
        return updated_status
    # class methods
    def feed(self, amount):
        self.hunger_level = max(0, self.hunger_level - amount)
        self._update_mood()
        
    def play(self, minutes):
        energy_loss = minutes // 10
        self.energy_level = max(0,self.energy_level - energy_loss)
        self._update_mood()

    def rest(self, hours):
        self.energy_level = min(10, self.energy_level + hours)
        self._update_mood()

    def status(self):
        current_status = f'Name: {self.name} | Hunger: {self.hunger_level} | Energy: {self.energy_level} | Mood: {self.mood}'
        return current_status
        


class Publisher:

    def __init__(self):
        self.observer = []
        self.temperature = 0

    def set_temperature(self, temp):
        self.temperature = temp
        self.notify_all_observers()

    def notify_all_observers(self):
        for obs in self.observer:
            obs.update(self.temperature)

    def add_observer(self, observer):
        self.observer.append(observer)

    def remove_observer(self, observer):
        self.observer.remove(observer)

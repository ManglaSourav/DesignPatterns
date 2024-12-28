

class UI:
    def update(self):
        raise Exception("Method 'update()' must be implemented")


class WebUI(UI):

    def update(self, temp):
        print("Temperature showing in web UI: ", temp)


class MobileUI(UI):

    def update(self, temp):
        print("Temperature showing in Mobile UI: ", temp)

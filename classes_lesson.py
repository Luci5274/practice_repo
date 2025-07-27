class LightSwitch:
    def __init__(self):
        self.is_on = True

    def turn_on(self):
        self.is_on =True

    def turn_off(self):
        self.is_on =False

    def check_status(self):
        if self.is_on:
            print('Bing Bong the light is on')
        else:
            print('skiff skoff the light is off')

    def toggle(self):
         self.is_on = not self.is_on

switch = LightSwitch()

switch.toggle()
switch.check_status()
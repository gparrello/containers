import appdaemon.plugins.hass.hassapi as hass

class your_class_name(hass.Hass):

    def initialize(self):
        self.switch = self.args["switchID"]
        self.light = self.args["lightID"]
        self.listen_state(self.what_we_want_to_do, self.switch, new="on")

    def what_we_want_to_do(self, entity, attribute, old, new, kwargs):
        self.log(f"{self.switch} is on")
        self.toggle(self.light)

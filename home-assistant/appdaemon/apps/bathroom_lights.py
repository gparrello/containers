import appdaemon.plugins.hass.hassapi as hass

class BathroomLights(hass.Hass):

    def initialize(self):
        self.door_sensor = self.args["door_sensor"]
        self.motion_sensor = self.args["motion_sensor"]
        self.lights = self.args["lights"]
        # self.listen_state(self.turn_lights_on, self.door_sensor, new="on")
        self.listen_state(self.toggle_lights, self.motion_sensor)

    def toggle_lights(self, entity, attribute, old, new, kwargs):
        self.log(f"{self.motion_sensor} is {new}")
        for l in self.lights:
            light = self.get_entity(l)
            light.set_state(state=new)
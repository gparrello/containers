import appdaemon.plugins.hass.hassapi as hass
from random import randrange, choice

class DiscoLights(hass.Hass):

    def initialize(self):
        self.switch = self.args['switch']
        self.lights = self.args['lights']
        self.color = [255,255,255]
        self.is_enabled = True
        self.listen_state(self.set_state, self.switch, attribute='state')
        self.listen_state(self.set_color, self.switch, attribute='rgb_color')

    def set_color(self, entity, attribute, old, new, kwargs):
        self.color = new

    def random_color(self):
        predominant = max(self.color)
        return [predominant if rgb == predominant else randrange(predominant) for rgb in self.color]

    def loop_light(self, kwargs):
        light = kwargs['light']
        self.turn_on(light, rgb_color=self.random_color(), brightness=255)
        if self.is_enabled:
            self.run_in(
                self.loop_light,
                delay=1,
                random_start=-3,
                random_end=3,
                light=light
            )
        else:
            [self.turn_off(l) for l in self.lights]

    def set_state(self, entity, attribute, old, new, kwargs):
        if new == 'on':
            self.is_enabled = True
            for light in self.lights:
                self.run_in(
                    self.loop_light,
                    delay=1,
                    random_start=0,
                    random_end=0,
                    light=light
                )
        else:
            self.is_enabled = False
            [self.turn_off(l) for l in self.lights]

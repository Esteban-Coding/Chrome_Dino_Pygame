from dino_runner.components.power_ups.power_up import Power_Up
from dino_runner.utils.constants import HEART_TYPE

class Heart(Power_Up):

    def __init__(self, image):
        super().__init__(image)
        self.type = HEART_TYPE
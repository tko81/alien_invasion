class Settings:

    def __init__(self):
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (0, 0, 0)

        self.bullet_width = 6
        self.bullet_height = 30
        self.bullet_color = (255, 165, 0)
        self.bullet_allowed = 50

        self.fleet_drop_speed = 10
        self.ship_limit = 3
        self.fleet_direction = 1
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.score_scale * self.alien_points)

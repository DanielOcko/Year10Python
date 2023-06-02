import arcade
import random

SCREEN_WIDTH = 520
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Selection Sort Visualization"

class Visualizer(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.index = 0
        self.heights = []
        for i in range(SCREEN_WIDTH):
            self.heights.append(random.randint(1, SCREEN_HEIGHT))

    def on_draw(self):
        arcade.start_render()
        for index, height in enumerate(self.heights):
            arcade.draw_line(index, 0, index, height, arcade.color.WHITE)

    def on_update(self, delta_time):
        if self.index < len(self.heights):
            min_index = self.index
            for mini in range(self.index + 1, len(self.heights)):
                if self.heights[mini] < self.heights[min_index]:
                    min_index = mini
            self.heights[min_index], self.heights[self.index] = self.heights[self.index], self.heights[min_index]
            self.index += 1

visualizer = Visualizer()
arcade.run()

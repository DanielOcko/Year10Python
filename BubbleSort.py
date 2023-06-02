import arcade
import random

SCREEN_WIDTH = 520
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Bubble Sort Visualization"

class Visualizer(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.heights = []
        for i in range(SCREEN_WIDTH):
            self.heights.append(random.randint(1, SCREEN_HEIGHT))

        self.timer = 0
        self.is_sorted = False
    def on_draw(self):
        arcade.start_render()
        for index, height in enumerate(self.heights):
            arcade.draw_line(index, 0, index, height, arcade.color.WHITE)

    def on_update(self, delta_time):
        if not self.is_sorted:
            self.is_sorted = True
            self.timer += delta_time
            #sort the heights
            #iterate through the list
            for n in range(len(self.heights)-1):
                #look at item n and n+1
                #if item n>n+1:
                if self.heights[n] > self.heights[n+1]:
                    #swap items
                    self.heights[n], self.heights[n+1] = self.heights[n+1], self.heights[n]
                    self.is_sorted = False
        else:
            print(self.timer)

visualizer = Visualizer()
arcade.run()

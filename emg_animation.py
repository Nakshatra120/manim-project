import numpy as np
import pandas as pd

from manim import *

# Load data
data = pd.read_csv('EMG_data_ses1.txt')

# Custom Config
CUSTOM_BLUE = "#013848"
CUSTOM_GREY = "#696969"

# Set the background color
config.background_color = WHITE
config.axes_color = CUSTOM_GREY

# Visualization
class EMGAnimation(Scene):
    def construct(self):
        # Define the axes
        axes = Axes(
            x_range=[0, len(data.iloc[:, 0]), 1],  # Assuming time data is in first column
            y_range=[data.min().min(), data.max().max(), 1],
            x_length=10,
            y_length=6,
            axis_config={"color": CUSTOM_GREY, "include_ticks": False},
            tips=False,
        )

        # Add labels to the axes
        axes_labels = axes.get_axis_labels(x_label="Time", y_label="Reading")

        # Add axes and labels to the scene
        self.add(axes, axes_labels)

        # Plot each electrode's data one at a time
        for i in range(1, data.shape[1]):  # Assuming electrode data starts at second column
            # Define the graph
            graph = axes.get_graph(
                lambda x: data.iloc[int(x), i] if x < len(data.iloc[:, 0]) else None
            ).set_color(CUSTOM_BLUE) # set color here

            # Add the graph to the scene
            self.play(FadeIn(graph))
            self.wait(1)  # Wait for 1 second with graph on screen

            # Remove the graph from the scene
            self.play(FadeOut(graph))


# if __name__ == "__main__":
#     script_name = f"{__file__}"
#     os.system(f"manim -p -ql {script_name} EMGAnimation")

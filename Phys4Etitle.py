from manim import *

class TitleinCircle(Scene):
	def construct(self):
		c = Circle(4, color = RED, fill_opacity =0.1)
		self.play(DrawBorderThenFill(c), run_time = 2)
		title = Text("Disorder in the Early Universe", font_size = 72, slant = "ITALIC").shift(UP*0.3)
		subtitle = Text("Daniel Green", slant = "ITALIC").shift(DOWN * 0.5)
		#render both of the objects with the Write animation
		self.play(Write(title), Write(subtitle))


		#add an arc just bigger than the circle
		a = Arc(4.5, TAU*0.25, -TAU*2/4, color = BLUE, stroke_width = 15)
		#this time let's animate it using the Create animation
		self.play(Create(a))
		self.wait(5)
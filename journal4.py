class Cat:
	def _init_(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
		self.arm_length = arm_length #float
		self.leg_length = leg_length #float
		self.num_eyes = num_eyes #int
		self.has_tail = has_tail #bool
		self.is_furry = is_furry #bool

	def describe(self):
		#physical characteristics

		print("Cat Physical Characteristics:")
		print(" Arm length:", self.arm_length, "meters")
		print:(" Leg length:", self.leg_length, "meters")
		print:(" Number of eyes:", self.num_eyes)
		print:(" Has tail:", "Yes" if self.has_tail else "No")
		print:(" Is furry:", "Yes" if self.is_furry else "No")

my_cat= Cat(arm_length = 0.3, leg_length = 0.4, num_eyes = 2, has_tail = True, is_furry= True)
my_cat.describe()


from django.db import models

# Create your models here.

class Brand(models.Model):

	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title

class Computer(models.Model):

	title = models.CharField(max_length=100)
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

	is_instock = models.BooleanField(default=True)
	price = models.IntegerField(default=0)
	stars = models.IntegerField(default=0)

	is_laptop = models.BooleanField(default=False)
	is_gamingtype = models.BooleanField(default=False)
	has_monitor = models.BooleanField(default=False)
	CPU_BRANDS = models.TextChoices("CPU_BRANDS", "RedA BlueI")
	RAM_CHOICES = models.TextChoices("RAM_CHOICES", "4Gb 8Gb 16Gb 32Gb 64Gb")
	GPU_BRANDS = models.TextChoices("GPU_BRANDS", "RedA BlueI GreenN")
	STORAGE_CHOICES = models.TextChoices("STORAGE_CHOICES", "128Gb 256Gb 512Gb 1Tb 2Tb 4Tb")
	STORAGE_TYPE = models.TextChoices("STORAGE_TYPE", "HDD SSD")
	SIZE_CHOICES = models.TextChoices("SIZE_CHOICES", '14" 15.6" 16" 24" 27" 32"')
	CASE_CHOICES = models.TextChoices("CASE_CHOICES", "mini-ITX micro-ATX ATX")
	RESOLUTION_CHOICES = models.TextChoices("RESOLUTION_CHOICES", "768p 1080p 1440p 4K")
	REFRESHRATE_CHOICES = models.TextChoices("REFRESHRATE_CHOICES", "60hz 75hz 90hz 120hz 144hz 240hz")
	DISPLAY_CHOICES = models.TextChoices("DISPLAY_CHOICES", "IPS TN VA OLED")

	cpu = models.CharField(max_length=100)
	cpu_brand = models.CharField(choices=CPU_BRANDS.choices, max_length=10, blank=False)
	ram = models.CharField(choices=RAM_CHOICES.choices, max_length=10, blank=False)
	gpu = models.CharField(max_length=100)
	gpu_brand = models.CharField(choices=GPU_BRANDS.choices, max_length=10, blank=False)
	storage = models.CharField(max_length=10)
	storage_type = models.CharField(choices=STORAGE_TYPE.choices, max_length=10, blank=False)
	size = models.CharField(choices=SIZE_CHOICES.choices, max_length=10)
	case = models.CharField(choices=CASE_CHOICES.choices, max_length=10)
	resolution = models.CharField(choices=RESOLUTION_CHOICES.choices, max_length=10)
	refreshrate = models.CharField(choices=REFRESHRATE_CHOICES.choices, max_length=10)
	display = models.CharField(choices=DISPLAY_CHOICES.choices, max_length=10)

	def __str__(self):
		return self.title

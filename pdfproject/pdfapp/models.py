from django.db import models
import os

# Create your models here.

GTK_FOLDER = r"C:\Program Files\GTK3-Runtime Win64\bin"
os.environ["PATH"] = GTK_FOLDER + os.pathsep + os.environ.get("PATH", "")

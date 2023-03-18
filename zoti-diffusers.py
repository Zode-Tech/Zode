import os
os.environ["HF_ENDPOINT"] = "https://huggingface.co"
from diffusers import DiffusionPipeline
pipeline = DiffusionPipeline.from_pretrained("Zode/MODEL")

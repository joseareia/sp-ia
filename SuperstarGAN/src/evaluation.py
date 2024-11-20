import os
import time
import utils
import dotenv
import datetime

# Load the environment variables.
dotenv.load_dotenv()

# Assign the environment variables to local ones.
SUPERSTARGAN_IMAGENET_RESULT = os.getenv('SUPERSTARGAN_IMAGENET_RESULT')
SUPERSTARGAN_IMAGENET_TRANSFORMED = os.getenv('SUPERSTARGAN_IMAGENET_TRANSFORMED')
IMAGENET_PATH = os.getenv('IMAGENET_PATH')
IMAGENET_MAPPING_CLASS = os.getenv('IMAGENET_MAPPING_CLASS')
CLASSIFICATION_LOGS = os.getenv('CLASSIFICATION_LOGS')
IMAGENET_VGG_MODEL = os.getenv('IMAGENET_VGG_MODEL')

# Start time.
start_time = time.time()

# Transform the images that were generated by the SuperstarGAN.
utils.img_transform(SUPERSTARGAN_IMAGENET_RESULT, SUPERSTARGAN_IMAGENET_TRANSFORMED, 12)

# Classifies the images that were previously transformed.
utils.adversarial_classifier(IMAGENET_PATH, SUPERSTARGAN_IMAGENET_TRANSFORMED, IMAGENET_MAPPING_CLASS, CLASSIFICATION_LOGS, IMAGENET_VGG_MODEL)

# Evaluates the FID score.
utils.fid(IMAGENET_PATH, SUPERSTARGAN_IMAGENET_TRANSFORMED)

# Calculates de LPIPS similarity.
utils.calculate_lpips(IMAGENET_PATH, SUPERSTARGAN_IMAGENET_TRANSFORMED)

# End time.
elapsed = time.time() - start_time

# Final message.
print(f"[ INFO ] All the tasks completed in {str(datetime.timedelta(seconds=int(elapsed)))}.")
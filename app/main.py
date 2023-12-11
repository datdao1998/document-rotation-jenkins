from io import BytesIO

import numpy as np
from fastapi import FastAPI, UploadFile
from PIL import Image

from utils.image_processing import normalize_image
from models.rotatenet import RotateNet
from config import config


app = FastAPI()

@app.get('/health')
async def check_health():
    return True


@app.post('/rotate')
def rotate_document(file: UploadFile):
    rotate_engine = RotateNet(
        model_path=config.rotatenet_path,
        input_size=config.input_size,
        mean=config.mean,
        std=config.std
    )

    stream = file.file.read()

    pil_image = Image.open(BytesIO(stream))

    pil_image = normalize_image(pil_image)

    image = np.array(pil_image)

    image, angle = rotate_engine.execute(image)

    return {
        "statusCode": 200,
        "angle": angle
    }
    





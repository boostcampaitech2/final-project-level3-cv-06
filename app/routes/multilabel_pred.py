import io
import os
from typing import List

from app.customrouter import fileRouter
from fastapi import File, UploadFile
from PIL import Image

from multilabel.API.model import (get_multilabel_prediction_toLabel,
                                  model_loader)

try:
    MODEL = model_loader()
except:
    raise Exception("multilabel model loader Error")

router = fileRouter(prefix=__file__)


@router.post("/")
async def get_multilabel(files: List[UploadFile] = File(...)):
    predictions = []
    for file in files:
        file_bytes = await file.read()
        image = Image.open(io.BytesIO(file_bytes))
        pred = get_multilabel_prediction_toLabel(MODEL, image)
        predictions.append(pred)
        print(predictions[0])
    return predictions[0] # [12,15,26]

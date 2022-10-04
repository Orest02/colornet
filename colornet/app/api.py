import io
from typing import Union

import PIL
from fastapi import FastAPI, File, Response, UploadFile
# from fastapi.openapi.models import Response
from hydra import compose, initialize
from pydantic import BaseModel

from colornet.hydra.init_runner import instantiate_runner

app = FastAPI()

initialize(version_base=None, config_path="../../configs")
cfg = compose(config_name="config")

runner = instantiate_runner(cfg)


@app.put("/transform")
async def transform(file: UploadFile = File(...)) -> Response:
    img = await file.read()
    stream = io.BytesIO(img)

    img = runner.run_one_cycle(stream)
    bytes_image = runner.postprocess.save_output_to_bytestream(img)

    return Response(content=bytes_image.getvalue(), media_type="image/png")

from typing import List, Tuple, Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from main import *
from main import image
from main import ImageGeneration


app = FastAPI()


def validate_schema(dimensions, corner_points):
    if dimensions[0] < 2 or dimensions[1] < 2:
        raise HTTPException(status_code=422, detail="Format error")
        return -1

    if len(corner_points) != 4:
        raise HTTPException(status_code=422, detail="Format error")
        return -1

    for i in corner_points:
        if len(i) != 2 and (i[0].isnumeric() == False or i[1].isnumeric() == False):
            raise HTTPException(status_code=422, detail="Format error")
            return -1
    return True


class schema(BaseModel):
    Dimensions: tuple[int, int]
    Points: list[tuple[float, float]]


@app.get("/")
async def root():
    return {"message": "This is a project."}


@app.post("/getvals")
def tup(ValDict: schema):
    if validate_schema(ValDict.Dimensions, ValDict.Points):
        Image_obj = image(ValDict.Dimensions, ValDict.Points)
        Image = ImageGeneration(Image_obj)
        Solution_mtrx = Image.matrix_generation()
        print(Solution_mtrx)
        return{"Solution Matrix": Solution_mtrx,
               "Dimensions": ValDict.Dimensions}


if __name__ == '__main__':
    uvicorn.run("app:app", port=8000, host="0.0.0.0")

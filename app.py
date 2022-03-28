from typing import List, Tuple, Dict
from fastapi import FastAPI
from pydantic import BaseModel
from main import *
from main import image
from main import ImageGeneration


app = FastAPI()

# I was forced to use the inputs as strings because of already setting up a strict validation
# method using regex. Alternatively, I could have used List[tuples] in the Schema
# for Corner_Points. Apologies for this inconvenience.


class schema(BaseModel):
    Dimensions: str
    Corner_Points: str


@app.get("/")
async def root():
    return {"message": "This is the Fetch_rewards project."}


@app.post("/getvals")
def tup(ValDict: schema):
    Dimensions = InputDimensions(ValDict.Dimensions)
    Corner_Points = InputCoordinates(ValDict.Corner_Points)
    Image_obj = image(Dimensions, Corner_Points)
    Image = ImageGeneration(Image_obj)
    Solution_mtrx = Image.matrix_generation()
    print(Solution_mtrx)
    return{"Solution Matrix": Solution_mtrx,
           "Dimensions": ValDict.Dimensions}

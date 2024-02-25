from fastapi import APIRouter


router = APIRouter(
    prefix="/predict",
    responses={404: {"description": "Not found"}},
    tags=["Model"]
)


@router.get("/")
async def predict():
    """
    description

    Returns:
        dict: {"status": "Done", "data": "Hello World"}
    """
    # Prepare and return response
    response = {"status": "Done", "data": "Hello World"}
    return response

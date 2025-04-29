from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

# Allow frontend (HTML page) to talk to FastAPI from browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use specific origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/get-lab-tests")
async def get_lab_tests(file: UploadFile = File(...)):
    # Placeholder logic: Replace this with your actual image processing logic
    # You can use Tesseract, OpenCV, regex, or ML models to extract data

    _output = {
        "is_success": True,
        "lab_tests": [
            {
                "test_name": "Hemoglobin",
                "test_value": 12.5,
                "bio_reference_range": "13.0-17.0",
                "lab_test_out_of_range": True
            },
            {
                "test_name": "WBC Count",
                "test_value": 7500,
                "bio_reference_range": "4000-11000",
                "lab_test_out_of_range": False
            }
        ]
    }

    return JSONResponse(content=_output)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

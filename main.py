from fastapi import FastAPI, Request, UploadFile, File, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from inference import predict
from glasses import generate_recommendation
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

UPLOAD_DIR = "Uploaded_images"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# Mount the uploaded images directory
app.mount("/Uploaded_images", StaticFiles(directory=UPLOAD_DIR), name="Uploaded_images")


@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    # FileResponseをTemplateResponseに変更します
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict/")
async def upload_file(request: Request, file: UploadFile = File(...)):
    # Validate file extension
    allowed_extensions = {".jpg", ".jpeg", ".png", ".gif"}
    file_extension = os.path.splitext(file.filename)[1]
    if file_extension not in allowed_extensions:
        raise HTTPException(status_code=415, detail="Unsupported file type")

    input_image_path = os.path.join(UPLOAD_DIR, file.filename)
    try:
        with open(input_image_path, "wb") as buffer:
            buffer.write(await file.read())

        result_text = predict(input_image_path)

        # Ensure the file is available for the response
        file_url = app.url_path_for("Uploaded_images", path=file.filename)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result_text": result_text, "file_url": file_url},
    )

@app.get("/predict_glasses/")  # GETメソッドを許可
async def predict_glasses(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict_glasses/")
async def predict_glasses(request: Request, weekend_activity: str = Form(...), gender_age: str = Form(...)):
    quiz_answers = {
        "weekend_activity": weekend_activity,
        "gender_age" : gender_age,
    }

    recommendation = generate_recommendation(quiz_answers)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "recommendation": recommendation,
        },
    )

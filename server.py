from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn
import uuid

app = FastAPI()

# middleware
app.add_middleware(
    CORSMiddleware, 
    allow_credentials=True, 
    allow_origins=["*"], 
    allow_methods=["*"], 
    allow_headers=["*"]
)

images_dir = "./images/"
video_dir = "./videos/"
output_dir = "./animations"

@app.post("/uploadImage/")
async def upload_image(image: UploadFile = File(...), number: int = Form(...)):
    # Generate a unique filename using UUID
    unique_filename = uuid.uuid4()
    image_path = os.path.join(images_dir, f"{unique_filename}.jpg")
    
    # Save the uploaded image
    with open(image_path, "wb") as buffer:
        buffer.write(await image.read())

    # Define the video path
    video_name = f"test{number}"    
    
    return_video = os.path.join(output_dir, f"test1.mp4")
    return FileResponse(return_video, media_type="video/mp4")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

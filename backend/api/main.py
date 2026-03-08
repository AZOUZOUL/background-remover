from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from rembg import remove
from PIL import Image
import io

# ⚡ Définir l'app au tout début
app = FastAPI()

# ⚡ Middleware CORS — avant les routes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # frontend Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Route de santé
@app.get("/health")
def health():
    return {"status": "ok"}


# Route principale
@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))

        output = remove(image)

        buffer = io.BytesIO()
        output.save(buffer, format="PNG")
        buffer.seek(0)

        return StreamingResponse(buffer, media_type="image/png")
    except Exception as e:
        return {"error": str(e)}


"""from fastapi import FastAPI, UploadFile, File
from rembg import remove
from PIL import Image
import io
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))

    output = remove(image)

    buffer = io.BytesIO()
    output.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer.getvalue()
"""


# uvicorn api.main:app --reload --port 8001
"""
const imageInput = document.getElementById("imageInput");
const removeBtn = document.getElementById("removeBtn");
const resultImage = document.getElementById("resultImage");
const downloadLink = document.getElementById("downloadLink");

removeBtn.addEventListener("click", async () => {
  const file = imageInput.files[0];

  if (!file) {
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch("http://localhost:8001/remove-bg", {
    method: "POST",
    body: formData,
  });

  const blob = await response.blob();
  const imageUrl = URL.createObjectURL(blob);

  resultImage.src = imageUrl;
  downloadLink.href = imageUrl;
  downloadLink.style.display = "inline";
});

"""

# index.htlm basique
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css" />
    <title>Akim's Background Remover</title>
</head>
<body>
    <h1>Abdoul-Akim's Background Remover</h1>
    
    <input type="file" id="imageInput" />
    <button id="removeBtn">Remove Background</button>
    
    <div class="result">
        <img id="resultImage" />
    </div>
    
    <a id="downloadLink" download>Download Image</a>
    
    <script src="app.js"></script>
    
</body>
</html>
"""

# styles.css basique
"""
body {
    font-family: sans-serif;
    max-width: 600px;
    margin: 40px auto;
}

button {
    margin-top: 10px;
}

.result {
    margin-top: 20px;
}

img {
    max-width: 100%;
}

#downloadLink {
    display: none;
    margin-top: 10px;
}

body {
    background: red;
}
"""

# github repository
"""
git init
git add .
git commit -m "Initial background remover project"
git branch -M main
git remote add origin YOUR_REPO_URL
git push -u origin main
"""

from fastapi import APIRouter, Request
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model + tokenizer once at startup
model_path = "model/RADAR-Vicuna-7B"  # change to your folder path

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)
model.eval()

Detectroute = APIRouter(prefix="/detect")

# Define request body
class TextInput(BaseModel):
    text: str

@Detectroute.post("/detect")
async def detect_text(data: TextInput):
    # Tokenize and run inference
    inputs = tokenizer(data.text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    probs = torch.softmax(logits, dim=1)
    confidence, prediction = torch.max(probs, dim=1)

    result = {
        "input_text": data.text,
        "predicted_label": int(prediction),
        "confidence": float(confidence)
    }
    return result

@Detectroute.get("/")
async def root():
    return {"message": "AI text detection API is running 🚀"}

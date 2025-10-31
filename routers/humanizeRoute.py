from fastapi import APIRouter
from pydantic import BaseModel
from llama_cpp import Llama


HumanizeRouter = APIRouter(prefix="/humanizer")

# Load the GGUF model
llm = Llama(
    model_path="model/Nemo-12b-Humanize-KTO-v0.1-Q2_K_L.gguf",
    n_ctx=4096,        # context length
    n_threads=8,       # adjust based on your CPU
    n_gpu_layers=20,   # set 0 if no GPU
    verbose=False
)

# Define request schema
class HumanizeRequest(BaseModel):
    input_text: str

@HumanizeRouter.post("/humanize")
def humanize_text(data: HumanizeRequest):
    """Takes text and returns a humanized version."""
    prompt = f"Humanize the following text:\n\n{data.input_text}\n\nRewritten version:"
    print("enter")
    # Generate text
    result = llm(prompt, max_tokens=512, temperature=0.7, stop=["</s>"])
    print("out")
    response = result["choices"][0]["text"].strip()
    
    return {"original": data.input_text, "humanized": response}

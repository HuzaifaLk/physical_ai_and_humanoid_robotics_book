from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import get_answer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class QuestionRequest(BaseModel):
    question: str

@app.post("/qa/")
def ask_question(request: QuestionRequest):
    """
    Receives a question, gets a grounded answer from the RAG agent, 
    and returns it.
    """
    if not request.question:
        raise HTTPException(status_code=400, detail="No question provided")
    
    try:
        # Call the get_answer function from the agent
        answer = get_answer(request.question)
        return {"answer": answer}
    except Exception as e:
        # In a real app, you'd want more specific error handling
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    """
    Root endpoint to confirm the server is running.
    """
    return {"status": "FastAPI server is running"}
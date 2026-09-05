from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import PyPDF2
import google.generativeai as genai
import uuid
import os
import json

# Initialize FastAPI
app = FastAPI(title="AI Study Buddy API")

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, change to your Netlify/GitHub Pages URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure AI (Ensure you set your API key in your environment variables)
# os.environ["GEMINI_API_KEY"] = "your_key_here"
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

# In-memory storage for MVP (Replace with PostgreSQL/Pinecone for production)
document_store = {}

class ChatRequest(BaseModel):
    session_id: str
    question: str

class GenerateRequest(BaseModel):
    session_id: str

@app.post("/api/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    try:
        # Extract text from PDF
        pdf_reader = PyPDF2.PdfReader(file.file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
            
        if not text.strip():
            raise HTTPException(status_code=400, detail="Could not extract text from PDF.")

        # Generate a session ID and store text
        session_id = str(uuid.uuid4())
        document_store[session_id] = text
        
        return {"session_id": session_id, "message": "Document processed successfully."}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/chat")
async def chat_with_notes(request: ChatRequest):
    if request.session_id not in document_store:
        raise HTTPException(status_code=404, detail="Session expired or not found. Please re-upload.")
    
    context = document_store[request.session_id]
    prompt = f"Based on the following notes:\n\n{context[:10000]}\n\nAnswer the user's question: {request.question}"
    
    response = model.generate_content(prompt)
    return {"answer": response.text}

@app.post("/api/generate/quiz")
async def generate_quiz(request: GenerateRequest):
    if request.session_id not in document_store:
        raise HTTPException(status_code=404, detail="Session not found.")
    
    context = document_store[request.session_id]
    prompt = f"""
    Based on the following text, generate a 5-question multiple choice quiz.
    You MUST return the response strictly as a JSON array of objects with this exact format:
    [
        {{"question": "...", "options": ["A", "B", "C", "D"], "answer": "The exact correct option string"}}
    ]
    Text: {context[:10000]}
    """
    
    response = model.generate_content(prompt)
    
    # Strip markdown formatting if AI wraps it in ```json
    cleaned_response = response.text.replace('```json', '').replace('```', '').strip()
    
    try:
        quiz_data = json.loads(cleaned_response)
        return {"quiz": quiz_data}
    except:
        return {"error": "Failed to parse AI output as JSON.", "raw": cleaned_response}

@app.post("/api/generate/flashcards")
async def generate_flashcards(request: GenerateRequest):
    if request.session_id not in document_store:
        raise HTTPException(status_code=404, detail="Session not found.")
    
    context = document_store[request.session_id]
    prompt = f"""
    Extract the 10 most important key terms and definitions from this text for flashcards.
    Return strictly as a JSON array of objects:
    [
        {{"term": "...", "definition": "..."}}
    ]
    Text: {context[:10000]}
    """
    
    response = model.generate_content(prompt)
    cleaned_response = response.text.replace('```json', '').replace('```', '').strip()
    
    try:
        flashcards_data = json.loads(cleaned_response)
        return {"flashcards": flashcards_data}
    except:
        return {"error": "Failed to parse AI output as JSON.", "raw": cleaned_response}

@app.post("/api/summarize")
async def summarize_notes(request: GenerateRequest):
    if request.session_id not in document_store:
        raise HTTPException(status_code=404, detail="Session not found.")
    
    context = document_store[request.session_id]
    prompt = f"Provide a comprehensive, highly structured summary of the following text, using markdown formatting, bullet points, and bold text for key concepts:\n\n{context[:15000]}"
    
    response = model.generate_content(prompt)
    return {"summary": response.text}

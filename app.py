from flask import Flask, render_template, request, jsonify
import os
import glob
import requests
from bs4 import BeautifulSoup
from pypdf import PdfReader
from docx import Document
import ollama

app = Flask(__name__)

# Store conversation history in memory
messages = [
    {"role": "system", "content": "You are a helpful, concise AI teaching assistant. Use the provided document context from ACEBS College and its Facebook page to answer questions accurately when relevant."}
]

def fetch_facebook_info(query):
    """Fetches public info if the user asks about the Facebook page, announcements, or posts."""
    if not any(keyword in query.lower() for keyword in ["facebook", "page", "post", "social", "announcement"]):
        return ""
        
    fb_url = "https://www.facebook.com/profile.php?id=100054375586584"
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(fb_url, headers=headers, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract basic meta descriptions or text snippets if accessible
            meta_desc = soup.find("meta", property="og:description")
            content = meta_desc["content"] if meta_desc else "ACEBS College official Facebook profile."
            return f"\n--- Source: ACEBS College Facebook Page ({fb_url}) ---\n{content}\n"
    except Exception as e:
        print(f"Could not fetch Facebook page directly: {e}")
        
    return f"\n--- Source: ACEBS College Facebook Link ---\nOfficial Link: {fb_url}\n"

def search_local_documents(query):
    """Optimized search: quickly scans local files and the Facebook link for keywords."""
    base_folder = r"C:\Users\LEARNING IT\Desktop\ACEBS COLLEGE STUFF"
    query_words = [w.lower() for w in query.split() if len(w) > 3]
    
    relevant_text = fetch_facebook_info(query)
    
    if not query_words:
        return relevant_text

    # Gather local files quickly
    files = []
    for ext in ("*.txt", "*.pdf", "*.docx"):
        files.extend(glob.glob(os.path.join(base_folder, "**", ext), recursive=True))
    
    for file_path in files:
        file_name = os.path.basename(file_path).lower()
        name_match = any(w in file_name for w in query_words)
        
        if name_match or len(files) < 10: 
            ext = os.path.splitext(file_path)[1].lower()
            content = ""
            try:
                if ext == ".txt":
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                elif ext == ".pdf":
                    reader = PdfReader(file_path)
                    for page in reader.pages[:3]:
                        t = page.extract_text()
                        if t: content += t + "\n"
                elif ext == ".docx":
                    doc = Document(file_path)
                    for para in doc.paragraphs[:50]:
                        if para.text: content += para.text + "\n"
                
                if any(w in content.lower() for w in query_words):
                    relevant_text += f"\n--- Source: {os.path.basename(file_path)} ---\n{content[:1000]}...\n"
            except Exception as e:
                print(f"Skipping {file_path} due to error.")
                
    return relevant_text

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global messages
    user_message = request.json.get("message", "")
    
    if not user_message.strip():
        return jsonify({"reply": "Please enter a valid message."})

    # Search local folder + Facebook link context
    document_context = search_local_documents(user_message)
    
    prompt_with_context = user_message
    if document_context:
        prompt_with_context = f"Context from ACEBS College sources:\n{document_context}\n\nQuestion: {user_message}"

    messages.append({"role": "user", "content": prompt_with_context})

    try:
        response = ollama.chat(model='llama3.2', messages=messages)
        bot_reply = response['message']['content']
        
        messages[-1]["content"] = user_message 
        messages.append({"role": "assistant", "content": bot_reply})
        
        return jsonify({"reply": bot_reply})
    except Exception as e:
        return jsonify({"reply": f"Error connecting to local Ollama: {str(e)}"})

if __name__ == "__main__":
    print("Starting ACEBS RAG AI Web Server with Facebook Integration...")
    print("Open your browser and go to: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
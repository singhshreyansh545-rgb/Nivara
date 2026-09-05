# Nivara

> **Turn your notes into knowledge.**

Nivara is an AI-powered study companion that transforms your notes and study materials into an interactive learning experience.

Instead of simply reading through PDFs and notes, Nivara helps you **understand, revise, and test yourself** using AI.

## ✨ Features

* 📄 **Upload Study Material** — Upload notes, PDFs, and other learning materials.
* 💬 **Ask Questions** — Ask questions and get answers based on your uploaded material.
* 📝 **Generate Quizzes** — Automatically create quizzes from your study material.
* 🧠 **Create Flashcards** — Turn important concepts into quick revision flashcards.
* 📚 **Summarize Content** — Generate concise summaries of lengthy chapters or notes.
* 📊 **Track Weak Topics** — Identify topics where you consistently struggle.
* 🎯 **Personalized Learning** — Use your performance to focus revision where it matters most.

## 🚀 How It Works

```text
        Study Material
              │
              ▼
       ┌──────────────┐
       │    Nivara    │
       └──────┬───────┘
              │
      ┌───────┼────────┐
      ▼       ▼        ▼
    Ask     Quiz    Summary
      │       │        │
      └───────┼────────┘
              ▼
       Learn & Revise
              │
              ▼
      Track Weak Topics
```

Nivara processes the uploaded material and uses AI to generate learning resources based on its content.

## 🛠️ Tech Stack

**Frontend**

* HTML
* CSS
* JavaScript

**Backend**

* Python
* Flask / FastAPI

**AI**

* AI API / Local LLM

**Database**

* SQLite

> The technology stack may evolve as the project develops.

## 📂 Project Structure

```text
Nivara/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   ├── app.py
│   ├── routes/
│   └── services/
│
├── uploads/
│
├── database/
│
├── requirements.txt
└── README.md
```

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/nivara.git
cd nivara
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
AI_API_KEY=your_api_key_here
```

> Never commit your API keys or `.env` file to GitHub.

### 5. Run the application

```bash
python app.py
```

Open the local URL shown in your terminal.

## 🗺️ Roadmap

### Phase 1 — MVP

* [ ] Basic web interface
* [ ] PDF upload
* [ ] Text extraction
* [ ] AI-powered Q&A
* [ ] Basic summaries

### Phase 2 — Learning Tools

* [ ] Quiz generation
* [ ] Flashcard generation
* [ ] Chapter-wise summaries
* [ ] Difficulty selection

### Phase 3 — Personalization

* [ ] Quiz performance tracking
* [ ] Weak-topic detection
* [ ] Personalized revision recommendations
* [ ] Learning progress dashboard

### Phase 4 — Advanced

* [ ] Semantic search
* [ ] Retrieval-Augmented Generation (RAG)
* [ ] User accounts
* [ ] Cloud deployment
* [ ] Support for multiple file formats
* [ ] Offline/local AI support

## 🎯 Project Goal

The goal of Nivara is to make studying more **active and personalized**.

Rather than simply consuming information, students should be able to interact with their own study material, test their understanding, identify weak areas, and revise more effectively.

## 🔒 Privacy

Study materials may contain personal or academic information. Nivara is designed with privacy in mind.

The project aims to:

* Keep uploaded materials isolated between users.
* Avoid storing unnecessary personal information.
* Never expose API keys in client-side code.
* Provide local AI support where possible.

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you'd like to contribute:

```bash
git clone https://github.com/YOUR_USERNAME/nivara.git
```

Create a new branch, make your changes, and submit a pull request.

## 📜 License

This project is licensed under the MIT License.

---

**Nivara — Turn your notes into knowledge.**

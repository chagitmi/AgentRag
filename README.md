AgentRag – מערכת RAG (Retrieval-Augmented Generation)
📌 תיאור הפרויקט

פרויקט זה מממש מערכת RAG (Retrieval-Augmented Generation), המשלבת בין שליפת מידע ממאגר מסמכים (Retrieval) לבין יצירת תשובות באמצעות מודל שפה (Generation).

המערכת מאפשרת לשאול שאלות בשפה טבעית ולקבל תשובות מבוססות מידע רלוונטי מתוך מקורות נתונים.

⚙️ יכולות המערכת
שליפת מסמכים רלוונטיים לשאלה (Retrieval)
יצירת תשובות מבוססות הקשר (LLM)
שילוב בין embedding + similarity search
עבודה עם מאגר ידע מקומי
תשתית להרחבה ל-Agent חכם
🧠 טכנולוגיות בשימוש
Python 3.x
Vector Database (כגון ChromaDB)
Embeddings (למשל OpenAI / אחרים)
LangChain / או מימוש ידני (לפי הפרויקט)
PyTorch (במידת הצורך)
📁 מבנה הפרויקט
AgentRag/
│
├── main.py              # קובץ הרצה ראשי
├── retriever.py        # שליפת מסמכים
├── generator.py        # יצירת תשובות
├── data/               # מאגר מסמכים
├── utils/              # פונקציות עזר
├── requirements.txt    # ספריות נדרשות
└── README.md
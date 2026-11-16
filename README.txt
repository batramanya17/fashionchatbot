THE EVERYDAY STYLE EDIT — STREAMLIT APP
=========================================

FILES
-----
app.py                       Streamlit chatbot application
requirements.txt             Python dependencies
.streamlit/secrets.toml      Gemini API key configuration

SETUP ON WINDOWS
----------------
1. Extract the ZIP file.
2. Open the extracted folder.
3. Open .streamlit/secrets.toml in Notepad or a code editor.
4. Replace PASTE_YOUR_GEMINI_API_KEY_HERE with your real Gemini API key.
   Keep the quotation marks, for example:
   GEMINI_API_KEY = "YOUR API KEY "
5. Open Command Prompt in this folder.
6. Install dependencies:
      python -m pip install -r requirements.txt
7. Run the app:
      python -m streamlit run app.py
8. Streamlit will open the chatbot in your browser. If it does not,
   open the Local URL printed in Command Prompt (usually http://localhost:8501).

IMPORTANT SECURITY NOTES
------------------------
- The ZIP contains a placeholder API key, not a real key. Add your own key.
- Do not share your secrets.toml file or publish it in a public repository.
- If you deploy the app, add GEMINI_API_KEY using the deployment platform's
  secrets manager instead of publishing your local secrets file.
- The app uses the Gemini model ID gemini-2.5-flash. Model availability
  depends on your Google AI Studio/API account and region.

🎬 AI Movie Recommendation System (Gemini + Streamlit)

An AI-powered Movie Recommendation System that suggests similar movies based on a user’s favorite movie using Google Gemini (Generative AI).
Built with Streamlit for a simple and interactive web interface.

🔗 Live App: https://moviefind.streamlit.app/

🚀 Features

Accepts a movie name as user input

Uses Google Gemini AI to generate intelligent movie recommendations

Clean and interactive Streamlit UI

Deployed on Streamlit Cloud

Secure API key handling using .env

🛠️ Tech Stack & Tools

Badges (you can keep these):








📂 Project Structure
Movie-Recommendation-App/
│
├── app.py               # Streamlit application code
├── requirements.txt     # Project dependencies
├── .env                 # API key (not pushed to GitHub)
├── README.md            # Project documentation
└── .venv/               # Virtual environment

⚙️ How It Works

User enters a movie name

Input is sent to Google Gemini Generative AI

Gemini analyzes the movie context

AI generates a list of similar movie recommendations

Results are displayed instantly in the Streamlit app

🧪 Run the App Locally
1️⃣ Clone the Repository
git clone https://github.com/your-username/Movie-Recommendation-App.git
cd Movie-Recommendation-App

2️⃣ Create Virtual Environment
python -m venv .venv
source .venv/Scripts/activate   # Windows
# OR
source .venv/bin/activate       # macOS/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Up Environment Variables

Create a .env file:

GOOGLE_GEMINI_API=your_api_key_here


⚠️ Do not push .env to GitHub

5️⃣ Run the App
streamlit run app.py

📦 requirements.txt
streamlit
google-generativeai
python-dotenv
langchain

🌐 Deployment (Streamlit Cloud)

Push code to GitHub

Login to Streamlit Cloud using GitHub

Click Create App

Select repository & app.py

Add GOOGLE_GEMINI_API in Secrets

Deploy 🎉

🧠 Learning Outcomes

Hands-on experience with Generative AI (Gemini)

Streamlit app development & deployment

API key security using environment variables

End-to-end AI project workflow

📌 Future Improvements

Add movie posters using TMDB API

Genre-based filtering

User rating system

RAG-based recommendations

👩‍💻 Author

Alisha Verma
📧 Email: alishavmca2024@gmail.com

🔗 GitHub: https://github.com/alishaverma0808

🔗 LinkedIn: https://www.linkedin.com/in/alisha-verma-b6a823222/

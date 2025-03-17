# Laptop-Price-Prediction-Model
streamlit : https://laptop-price-prediction-model-3y7cw8pxwypnrrfwsjo7k2.streamlit.app/

Project Overview:

The Laptop Price Prediction Model is a Machine Learning-based Web App that predicts laptop prices based on various specifications like brand, RAM, processor, GPU, screen resolution, etc. The model is trained on a dataset containing different laptop configurations and their market prices.

This project is useful for consumers looking to buy laptops, as well as for businesses that want to analyze pricing trends. The model helps in understanding how different features affect a laptop's price.

🎯 Objective:
The primary goal of this project is to build a regression-based model that accurately predicts laptop prices based on various hardware and brand attributes. The project also involves:
✅ Data collection and preprocessing.
✅ Feature engineering
✅ Model selection and training
✅ Deploying the model as a Streamlit web application

Dataset Details:
The dataset contains information about various laptop models, including:

Feature	Description: 
Brand	Laptop manufacturer (Apple, HP, Dell, etc.)
Type	Category of the laptop (Ultrabook, Gaming, Notebook, etc.)
RAM	Amount of RAM (in GB)
Weight	Laptop weight (in kg)
IPS Panel	Whether the laptop has an IPS display (Yes/No)
Touchscreen	Whether the laptop has a touchscreen (Yes/No)
Screen Size	Screen size in inches
Resolution	Display resolution (1920x1080, 1366x768, etc.)
Processor	Type of CPU (Intel i5, i7, Ryzen 5, etc.)
HDD	Hard Disk capacity (in GB)
SSD	SSD storage (in GB)
GPU Brand	GPU manufacturer (NVIDIA, AMD, Intel)
Operating System	OS type (Windows, macOS, Linux)
Price (Target Variable)	Laptop price in USD.

🛠 Technologies & Tools Used: 
🔹 Python – Main programming language
🔹 Pandas & NumPy – Data preprocessing & analysis
🔹 Scikit-learn – Machine Learning model training
🔹 Streamlit – Web app deployment
🔹 Pickle – Model serialization for deployment
🔹 Matplotlib & Seaborn – Data visualization

📊 Data Preprocessing & Feature Engineering: 
Before training the model, the dataset is cleaned and processed:
✅ Handling Missing Values – Filling or removing missing data
✅ Feature Encoding – Converting categorical features (Brand, OS, GPU, etc.) using Label Encoding & One-Hot Encoding
✅ Feature Scaling – Standardizing numerical values (Weight, RAM, etc.)
✅ Creating New Features – Pixels Per Inch (PPI) calculated from resolution and screen size

 
🔍 Model Selection & Training: 
Different regression models were tested:
✅ Linear Regression
✅ Random Forest Regressor
✅ Gradient Boosting Regressor
✅ XGBoost

After evaluating the models, Linear Regression performed well with a good balance of accuracy and interpretability.

Final Model: Linear Regression with Feature Engineering: 
📌 Evaluation Metrics:
✔️ R² Score: 80%
✔️ Mean Absolute Error (MAE): 20%

🖥️ Web App Deployment (Streamlit): 
The trained model is deployed using Streamlit, where users can input laptop features to get a predicted price.

🔹 How It Works:
1️⃣ Select Brand, Laptop Type, RAM, Processor, GPU, Storage, OS, etc.
2️⃣ Adjust Screen Size, Resolution, and Weight
3️⃣ Click Predict Price
4️⃣ The model returns the estimated laptop price

🌍 Deployment & Future Improvements: 
The model is deployed as a web app using Streamlit, and future improvements include:
🔹 Adding more data for better predictions
🔹 Using Deep Learning for improved accuracy
🔹 Deploying on Cloud (AWS/GCP/Heroku) for better scalability

📌 Conclusion: 
The Laptop Price Prediction Model provides an easy-to-use interface for estimating laptop prices based on their specifications. It helps buyers make informed decisions and provides businesses with pricing insights. 🚀

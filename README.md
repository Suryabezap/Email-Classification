# 📬 Email Classification System – Overview

This project is a web-based system that helps automate the classification of support emails for a company's service desk team. It intelligently assigns incoming emails to one of the following categories:

🚨 Incident 

🙋 Request 

⚙️ Problem 

🔁 Change 

To maintain user privacy, the system first masks any sensitive personal information (PII) in the email before classification. The masked entities include:

🔐 Full Names

📧 Email Addresses

📱 Phone Numbers

🆔 Aadhar Numbers

💳 Credit/Debit Card Numbers

🔢 CVV & Expiry Dates

🎂 Dates of Birth

After the email is categorized, the original content can be restored if needed.

🔧 Tech Stack

Frontend: HTML + CSS

Backend: Flask (Python)

Model: Naive Bayes 

NLP: NLTK for text cleaning & stemming

PII Masking: Regex-based masking

Deployment: Flask local server (easily deployable on cloud platforms)

# Input 

![image](https://github.com/user-attachments/assets/23944b46-3c46-421d-ae5e-eaa4739373bf)

# Output 

![image](https://github.com/user-attachments/assets/f4287e13-eebf-4981-8d57-0f0e200a11d7)





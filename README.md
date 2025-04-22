# 📬 Email Classification System – Overview
This project is a web-based system that helps automate the classification of support emails for a company's service desk team. It intelligently assigns incoming emails to one of the following categories:

🚨 Incident – Something broken or service not working.

🙋 Request – Asking for access, info, or assistance.

⚙️ Problem – Root cause analysis of repeated incidents.

🔁 Change – Proposing or approving a change in the system.

To maintain user privacy, the system first masks any sensitive personal information (PII) in the email before classification. The masked entities include:

🔐 Full Names

📧 Email Addresses

📱 Phone Numbers

🆔 Aadhar Numbers

💳 Credit/Debit Card Numbers

🔢 CVV & Expiry Dates

🎂 Dates of Birth

After the email is categorized, the original content can be restored if needed.

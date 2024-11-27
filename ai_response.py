import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set your OpenAI API key
API_KEY = "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"
API_URL = "https://api.openai.com/v1/chat/completions"

def generate_response(client_details):
    """
    Generate a professional and human-like email response based on client details.
    
    :param client_details: Dictionary containing client and project details.
    :return: Generated email response.
    """
    prompt = f"""
You are a professional project manager. Write a polished and human-like email response to a client inquiry based on the following details:

From Name: {client_details['from_name']}
Client First Name: {client_details['client_first_name']}
Client Last Name: {client_details['client_last_name']}
Client Email: {client_details['client_email']}
Client Country: {client_details['client_country']}
Client Location: {client_details.get('client_location', 'Not provided')}
Client Language: {client_details['client_language']}
Project Type: {client_details['project_type']}
Service Category: {client_details['service_category']}
Client Website: {client_details.get('client_website', 'No')}
Additional Information: "{client_details['additional_information']}"

The email should address the client by their full name, summarize the project details, and provide a professional and helpful response. Maintain a natural tone and avoid overused phrases like 'I hope this email finds you well.'
    """

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a professional project manager."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 300,
        "temperature": 0.7,
        "top_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error generating response: {e}"

def send_email(to_email, subject, body):
    """
    Send an email using Gmail's SMTP server.
    
    :param to_email: Recipient email address.
    :param subject: Subject of the email.
    :param body: Body of the email.
    """
    from_email = "yashikakandadka@gmail.com"
    from_password = "xxkv fume cbev immo"  # Use an app password if you have 2FA enabled

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    client_details = {
        "from_name": "Jesna",
        "client_first_name": "Geminas",
        "client_last_name": "Ket",
        "client_email": "GeminasKet@gmail.com",
        "client_country": "Romania",
        "client_location": "Romania",
        "client_language": "English",
        "project_type": "Content with Databases",
        "service_category": "Web Development",
        "client_website": "No",
        "additional_information": (
            "I need 4 dynamic pages for a real estate Web-application: one each for apartments, "
            "houses, business centres, and land. I need 2 filters for 'for sale' and 'for rent,' "
            "and they should be connected. Don't bother with the design; I'll handle that. I just "
            "need the functionality. The budget should be $100000. Thank you!"
        ),
    }

    response = generate_response(client_details)
    print("Generated Response:\n")
    print(response)

    # Send the email
    if "Error" not in response:
        send_email("geminasket@gmail.com", "Project Inquiry Response", response)

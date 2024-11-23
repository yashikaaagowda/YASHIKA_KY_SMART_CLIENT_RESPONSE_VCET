import openai

# Set your API key
openai.api_key = "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"

def generate_response(client_details):
    """
    Generate a professional and human-like email response based on client details.
    
    :param client_details: Dictionary containing client and project details.
    :return: Generated email response.
    """
    # Build the prompt using the client details
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

    # Call OpenAI's API
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use GPT-3.5 or a higher model if available
            prompt=prompt,
            max_tokens=300,
            temperature=0.7,  # Adjust creativity level
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error generating response: {e}"

# Example usage
if _name_ == "_main_":
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
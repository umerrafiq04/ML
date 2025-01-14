import google.generativeai as genai

# Replace this with your actual Google API key
GOOGLE_API_KEY = "AIzaSyC33x2uw1MYcvm8aGdVL1VotF2L4ZaC58I"

# Configure the API with your API key
genai.configure(api_key=GOOGLE_API_KEY)

def prompt():
    # Input for the generative model
    input_text = "How are you doing today?"

    # Using the gemini model for content generation
    model = genai.Model("gemini-pro")
    response = model.generate_content(input_text)

    # Print the response text
    print(response.text)
    return response

if __name__ == "__main__":
    prompt()

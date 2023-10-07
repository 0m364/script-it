import openai

# Set up OpenAI API
openai.api_key = 'YOUR_API_KEY'  # Replace with your own API key

def generate_script(prompt):
    # Adjust these parameters based on your requirements
    max_tokens = 500
    temperature = 0.8

    # Use OpenAI's "davinci" model for better performance
    model = 'davinci'

    # Generate the script
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        n=1,
        stop=None,
        temperature=temperature
    )

    return response.choices[0].text.strip()

# Example usage
prompt = """
Title: "The Mysterious Treasure"
Genre: Adventure/Mystery

INT. DARK CAVE - NIGHT

A group of explorers is searching for a hidden treasure. Suddenly, they hear a strange noise coming from deep within the cave.

EXPLORER 1
Did you hear that?

EXPLORER 2
Yeah, what could it be?

The explorers exchange worried glances.
"""

generated_script = generate_script(prompt)
print(generated_script)

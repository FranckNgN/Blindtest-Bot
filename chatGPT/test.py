import openai
openai.api_key = None

def generate_response(prompt):
    # Use the OpenAI API to generate a response
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Get the first generated response
    message = completions.choices[0].text
    return message

# Example usage
prompt = "reply in bullet point, I have a youtube link https://www.youtube.com/watch?v=ylssgHLVZaE&ab_channel=SamuelKimMusic, tell me the anime name, tell me the song name, tell me the author, tell me if it represents an opening ending or ost and the number if possible"
response = generate_response(prompt)
print(response)
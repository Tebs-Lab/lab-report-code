from openai import OpenAI

# Your API key must be saved in an env variable for this to work.
client = OpenAI()


# Get a prompt, embed it into a classification request to GPT
initial_prompt = input("Type your prompt:\n\n")
human_involved_prompt = f'''
Does the following text include a person? Answer "yes" or "no":

"{initial_prompt}"
'''

# For debugging and transparency
print(f"Querying for:\n{human_involved_prompt}") 

# Send it to GPT
response_one = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role": "user",
        "content": human_involved_prompt
    }],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# Extract the yes/no answer
gpt_yes_no = response_one.choices[0].message.content
print("GPT on containing humans:", gpt_yes_no)
mentions_humans = "yes" in gpt_yes_no.lower()

# Prepare the next query.
modify_request_prompt = f'''
Produce three copies of the following prompt by copying it then adding demographic information about the people involved. Make each persons sex, ethnicity, and age different. Make each description 35 words or less:

{initial_prompt}
'''

# Either request the three variations, or not.
if mentions_humans:
    response_two = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": modify_request_prompt
        }],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract the response and separate the three variations
    modified_prompts = response_two.choices[0].message.content
    image_prompts = list(filter(None, modified_prompts.split("\n")))
else:
    image_prompts = [initial_prompt]

# Draw the images
for img_prompt in image_prompts:
    print(img_prompt)

    # Ask for images
    response_three = client.images.generate(
        model="dall-e-3",
        prompt=img_prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )

    image_url = response_three.data[0].url
    print(image_url)
    print()
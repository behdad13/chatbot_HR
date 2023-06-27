import openai

# Set up your OpenAI API credentials
openai.api_key = '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'


# Function to create job description
def create_job_description(position, tasks, cloud_exp, prog_langs, db_exp):
    prompt = f"Create a job description for a {position}. The tasks for this role are: {tasks}. The required experience is as follows: {cloud_exp} years of experience in cloud services, {prog_langs} years of experience in the following programming languages, and {db_exp} years of experience in database management."

    response = openai.Completion.create(
        engine="text-davinci-003",  # Change this to the most recent model when GPT-4 is released.
        prompt=prompt,
        temperature=0.7,
        max_tokens=300
    )

    return response.choices[0].text.strip()


# Interactive chat with HR
def chat_with_hr():
    print("Hello, I'm here to help you create a job description.")
    position = input("Please tell me the job position: ")
    tasks = input("Please tell me the job tasks: ")
    cloud_exp = input("Please tell me the years of experience required in cloud services: ")
    prog_langs = input("Please tell me the years of experience required in programming languages: ")
    db_exp = input("Please tell me the years of experience required in database management: ")

    job_description = create_job_description(position, tasks, cloud_exp, prog_langs, db_exp)
    print("\nHere is the job description:\n")
    print(job_description)


# Run the chatbot
chat_with_hr()
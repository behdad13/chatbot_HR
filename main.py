import openai

# Set up your OpenAI API credentials
openai.api_key = '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'


# Function to create job description
def create_job_description(position, tasks, skills_exp, cloud_exp, prog_langs, db_exp, education_req, company_info,
                           formality_level, include_benefits):
    skills_exp_list = skills_exp.split(",")
    skills_exp_formatted = "\n- ".join(skills_exp_list)
    skills_exp_prompt = f"The ideal candidate should possess the following skills and qualifications:\n- {skills_exp_formatted}."

    cloud_exp_prompt = f"The candidate should have at least {cloud_exp} years of experience in working with cloud services."

    prog_langs_prompt = f"The candidate should have expertise in programming languages with a minimum of {prog_langs} years of experience."

    db_exp_prompt = f"The candidate should have {db_exp} years of experience in database management."

    education_req_prompt = f"The candidate should have a {education_req} degree or equivalent educational background."

    company_info_prompt = f"About the Company:\n\n{company_info}\n\n"

    formality_prompt = ""
    if formality_level == "formal":
        formality_prompt = "This job description follows a formal tone."
    elif formality_level == "semi-formal":
        formality_prompt = "This job description has a semi-formal tone."
    elif formality_level == "less formal":
        formality_prompt = "This job description is less formal in tone."

    benefits_prompt = ""
    if include_benefits and include_benefits.lower() == "yes":
        benefits_prompt = f"Company Benefits:\n\n{include_benefits}\n\n"

    prompt = f"Create a job description for the position of {position}.\n\n{company_info_prompt}The primary tasks and responsibilities for this role include:\n{tasks}\n\n{skills_exp_prompt}\n\n{cloud_exp_prompt}\n\n{prog_langs_prompt}\n\n{db_exp_prompt}\n\n{education_req_prompt}\n\n{formality_prompt}\n\n{benefits_prompt}"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1000
    )

    return response.choices[0].text.lstrip().rstrip()


# Interactive chat with HR
def chat_with_hr():
    print("Hello, I'm here to help you create a job description.")
    position = input("Please tell me the job position: ")
    tasks = input("Please tell me the job tasks: ")
    skills_exp = input("Please list the required skills and qualifications (comma-separated): ")
    cloud_exp = input("Please specify the required years of experience in working with cloud services: ")
    prog_langs = input("Please indicate the required years of experience in programming languages: ")
    db_exp = input("Please specify the required years of experience in database management: ")
    education_req = input("Please specify the required educational qualifications: ")
    company_info = input("Please provide some information about your company and its culture: ")
    formality_level = input("Please select the formality level of the job description response (formal, semi-formal, less formal): ")
    include_benefits = input("Do you want to include information about company benefits? (yes/no): ")

    job_description = create_job_description(position, tasks, skills_exp, cloud_exp, prog_langs, db_exp, education_req,
                                             company_info, formality_level, include_benefits)
    print("\nHere is the job description:\n")
    print(job_description)


# Run the chatbot
chat_with_hr()

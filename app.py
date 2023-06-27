from flask import Flask, request, render_template
import openai

# Set up your OpenAI API credentials
openai.api_key = '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'

app = Flask(__name__)

questions = [
    "Please tell me the job position you are hiring for:",
    "Please provide a detailed description of the primary tasks and responsibilities for this position:",
    "Please list the required skills and qualifications for this position (comma-separated):",
    "Please specify the cloud platform/platforms required years of experience in working with cloud services:",
    "Please indicate the required years of experience in programming languages:",
    "Please specify the required years of experience in database management:",
    "Please specify the required educational qualifications for this position:",
    "Please provide some information about your company and its culture:",
    "Please select the formality level of the job description response (formal, semi-formal, less formal):",
    "Do you want to include information about company benefits? (yes/no):"
]

answers = {}

@app.route('/', methods=['GET', 'POST'])
def chat_with_hr():
    if request.method == 'POST':
        question_number = int(request.form.get('question_number'))
        answer = request.form.get('answer')
        answers[str(question_number)] = answer

        if question_number < len(questions) - 1:
            question_number += 1
            return render_template('chatbot.html', question=questions[question_number], question_number=question_number)

        if answers['9'].lower() == 'yes':
            return render_template('benefits.html', question_number=question_number)
        else:
            job_description = create_job_description(answers['0'], answers['1'], answers['2'], answers['3'], answers['4'],
                                                     answers['5'], answers['6'], answers['7'], answers['8'], None)
            return render_template('result.html', job_description=job_description)

    return render_template('chatbot.html', question=questions[0], question_number=0)


@app.route('/benefits', methods=['POST'])
def handle_benefits():
    benefits_info = request.form.get('benefits_info')
    job_description = create_job_description(answers['0'], answers['1'], answers['2'], answers['3'], answers['4'],
                                             answers['5'], answers['6'], answers['7'], answers['8'], benefits_info)
    return render_template('result.html', job_description=job_description)


def create_job_description(position, tasks, skills_exp, cloud_exp, prog_langs, db_exp, education_req, company_info, formality_level, include_benefits):
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
        max_tokens=500
    )

    return response.choices[0].text.strip()


if __name__ == '__main__':
    app.run(debug=True)

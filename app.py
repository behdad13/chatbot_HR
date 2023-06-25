from flask import Flask, request, render_template
import openai

# Set up your OpenAI API credentials
openai.api_key = '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'

app = Flask(__name__)

questions = [
    "Please tell me the job position:",
    "Please tell me the job tasks:",
    "Cloud Experience:",
    "Programming Language Experience:",
    "Database Experience:"
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

        job_description = create_job_description(answers['0'], answers['1'], answers['2'], answers['3'], answers['4'])

        return render_template('result.html', job_description=job_description)

    return render_template('chatbot.html', question=questions[0], question_number=0)


def create_job_description(position, tasks, cloud_exp, prog_langs, db_exp):
    prompt = f"Create a job description for a {position}. The tasks for this role are: {tasks}. The required experience is as follows: {cloud_exp} years of experience in cloud services, {prog_langs} years of experience in the following programming languages, and {db_exp} years of experience in database management."

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=500
    )

    return response.choices[0].text.strip()


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, render_template
import openai

# Set up your OpenAI API credentials
openai.api_key = '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'

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def chat_with_hr():
    if request.method == 'POST':
        position = request.form.get('position')
        tasks = request.form.get('tasks')
        cloud_exp = request.form.get('cloud_exp')
        prog_langs = request.form.get('prog_langs')
        db_exp = request.form.get('db_exp')

        job_description = create_job_description(position, tasks, cloud_exp, prog_langs, db_exp)

        return render_template('result.html', job_description=job_description)

    return render_template('index.html')


def create_job_description(position, tasks, cloud_exp, prog_langs, db_exp):
    prompt = f"Create a job description for a {position}. The tasks for this role are: {tasks}. The required experience is as follows: {cloud_exp} years of experience in cloud services, {prog_langs} years of experience in the following programming languages, and {db_exp} years of experience in database management."

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=300
    )

    return response.choices[0].text.strip()


if __name__ == '__main__':
    app.run(debug=True)

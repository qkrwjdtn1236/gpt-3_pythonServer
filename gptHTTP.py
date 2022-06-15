from flask import Flask,request

import json
import openai



##############################################

app = Flask(__name__)

@app.route("/")
def hello_world():
    parameter_dict = request.args.to_dict()

    if len(parameter_dict) == 0:
        return 'error'

    try:

        openai.api_key = "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"
        response = openai.Completion.create(engine="davinci", prompt="This is a test", max_tokens=5)

        from api import GPT, Example, set_openai_key
        gpt = GPT(engine="davinci",
                temperature=0.7,
                max_tokens=250)

        print(request.args['a'])

        output = gpt.submit_request(request.args['a'])
        print(output.choices[0]['text'])
        return output.choices[0]['text']


    except:
        return 'error'
if __name__ == '__main__':
    app.run(host='10.138.40.2', port=5000, debug=True)
# Run by typing python3 main.py

# **IMPORTANT:** only collaborators on the project where you run
# this can access this web server!



# import basics
import os

# import stuff for our web server
from flask import Flask, request, redirect, url_for, render_template, session
from utils import get_base_url
# import stuff for our models
from aitextgen import aitextgen
from transformers import PreTrainedTokenizerFast, GPT2DoubleHeadsModel, GPT2TokenizerFast, GPT2Tokenizer

def load_model(model_path):
    model = GPT2DoubleHeadsModel.from_pretrained(model_path)
    return model


def load_tokenizer(tokenizer_path):
    tokenizer = GPT2Tokenizer.from_pretrained(tokenizer_path)
    return tokenizer




story_genre = ''


def genre_text_generation(genre):
    
    if genre == 'Java':
        file_dest = 'model/java'
        
    if genre == 'Python':
        file_dest = 'model/python'
        
    if genre == 'C++':
        file_dest = 'model/cpp'
        
    if genre == 'C#':
        file_dest = 'model/csharp'
        
    if genre == 'JavaScript':
        file_dest = 'model/js'
        
    if genre == 'C':
        file_dest = 'model/c'
        
    return file_dest

# load up a model from memory. Note you may not need all of these options.

#ai = aitextgen(model_folder = 'model/action_files', to_gpu=False)
# ai = aitextgen(model_folder="model/", tokenizer_file="model/aitextgen.tokenizer.json", to_gpu=False)
#ai = aitextgen(model="distilgpt2", to_gpu=False)

# setup the webserver
# port may need to be changed if there are multiple flask servers running on same server
port = 12345
base_url = get_base_url(port)


# if the base url is not empty, then the server is running in development, and we need to specify the static folder so that the static files are served
if base_url == '/':
    app = Flask(__name__)
else:
    app = Flask(__name__, static_url_path=base_url+'static')

app.secret_key = os.urandom(64)

generated = "None"
# set up the routes and logic for the webserver

@app.route(f'{base_url}/GenAI_JS', methods=['POST', 'GET'])
def GenAI_JS(): #Works
    print("Request.form" + str(request.form))
    prompt = request.form["JSInput"] #retrieves the prompt from name JSInput
    print(prompt)
    print(prompt)
    model = load_model("model/js")
    tokenizer = load_tokenizer("model/js")
    ids = tokenizer.encode(f'{prompt}', return_tensors='pt')
    if prompt is not None:
        generated = model.generate(
            ids,
            do_sample=True,
            max_length=150,
            pad_token_id=model.config.eos_token_id,
            top_k=50,
            top_p=0.95,
            return_as_list=True
        )
    generated = tokenizer.decode(generated[0], skip_special_tokens=True)
#     generated = "Test: "
#     generated = generated + "Flag for JS!"
    print("Generated: " + generated)
    data = {'generated_ls': generated}
    session['data'] = generated
    return redirect(url_for("JS_Render"))

@app.route(f'{base_url}/JS_Render', methods = ['POST', 'GET'])
def JS_Render():
    if 'data' in session:
        data = session['data']
        print("Session Data: "+ str(data))
        return render_template('JS-Popup.html', generated=data)

@app.route(f'{base_url}/GenAI_Java', methods = ['POST', 'GET'])
def GenAI_Java(): #index out of range of self error
    print("Request.form" + str(request.form))
    prompt = request.form["JavaInput"] #retrieves the prompt from name JSInput
    print(prompt)
    print(prompt)
    model = load_model("model/java")
    tokenizer = load_tokenizer("model/java")
    ids = tokenizer.encode(f'{prompt}', return_tensors='pt')
    if prompt is not None:
        generated = model.generate(
            ids,
            do_sample=True,
            max_length=150,
            pad_token_id=model.config.eos_token_id,
            top_k=50,
            top_p=0.95,
            return_as_list=True
        )
    generated = tokenizer.decode(generated[0], skip_special_tokens=True)
#     generated = "Test: "
#     generated = generated + "Flag for Java!"
    print("Generated: " + generated)
    data = {'generated_ls': generated}
    session['data'] = generated
    return redirect(url_for("Java_Render"))

@app.route(f'{base_url}/Java_Render', methods = ['POST', 'GET'])
def Java_Render():
    if 'data' in session:
        data = session['data']
        print("Session Data: "+ str(data))
        return render_template('Java-Popup.html', generated=data)



@app.route(f'{base_url}/GenAI_Python', methods = ['POST', 'GET'])
def GenAI_Python(): #Works!
    print("Request.form" + str(request.form))
    prompt = request.form["PythonInput"] #retrieves the prompt from name JSInput
    print(prompt)
    print(prompt)
    model = load_model("model/python")
    tokenizer = load_tokenizer("model/python")
    ids = tokenizer.encode(f'{prompt}', return_tensors='pt')
    if prompt is not None:
        generated = model.generate(
            ids,
            do_sample=True,
            max_length=150,
            pad_token_id=model.config.eos_token_id,
            top_k=50,
            top_p=0.95,
            return_as_list=True
        )
    generated = tokenizer.decode(generated[0], skip_special_tokens=True)
#     generated = "Test: "
#     generated = generated + "Flag for Python!"
    print("Generated: " + generated)
    data = {'generated_ls': generated}
    session['data'] = generated
    return redirect(url_for("Python_Render"))

@app.route(f'{base_url}/Python_Render', methods = ['POST', 'GET'])
def Python_Render():
    if 'data' in session:
        data = session['data']
        print("Session Data: "+ str(data))
        return render_template('Python-Popup.html', generated=data)


@app.route(f'{base_url}/GenAI_C', methods = ['POST', 'GET'])
def GenAI_C(): #Works!
    print("Request.form" + str(request.form))
    prompt = request.form["CInput"] #retrieves the prompt from name JSInput
    print(prompt)
    model = load_model("model/c")
    tokenizer = load_tokenizer("model/c")
    ids = tokenizer.encode(f'{prompt}', return_tensors='pt')
    if prompt is not None:
        generated = model.generate(
            ids,
            do_sample=True,
            max_length=150,
            pad_token_id=model.config.eos_token_id,
            top_k=50,
            top_p=0.95,
            return_as_list=True
        )
    generated = tokenizer.decode(generated[0], skip_special_tokens=True)
#     generated = "Test: "
#     generated = generated + "Flag for C!"
    print("Generated: " + generated)
    data = {'generated_ls': generated}
    session['data'] = generated
    return redirect(url_for("C_Render"))

@app.route(f'{base_url}/C_Render', methods = ['POST', 'GET'])
def C_Render():
    if 'data' in session:
        data = session['data']
        print("Session Data: "+ str(data))
        return render_template('C-Popup.html', generated=data)
        
    else:
        return render_template('writer_home.html', generated=None)

@app.route(f'{base_url}/GenAI_Cpp', methods = ['POST', 'GET'])
def GenAI_Cpp(): #Still need the AI
    print(request.form)
    prompt = request.form['CppInput']
    print(prompt)
    ai = aitextgen(model_folder = "model/cpp", to_gpu=False)
    
    if prompt is not None:
        generated = ai.generate(
            n=1,
            batch_size=10,
            prompt=str(prompt),
            max_length=150,
            temperature=1.0,
            return_as_list=True
        )

    generated = generated[0]
    print("Generated: " + generated)
    data = {'generated_ls': generated}
    session['data'] = generated
    return redirect(url_for("Cpp_Render"))

@app.route(f'{base_url}/Cpp_Render', methods = ['POST', 'GET'])
def Cpp_Render():
    if 'data' in session:
        data = session['data']
        print("Session Data: "+ str(data))
        return render_template('Cpp-Popup.html', generated=data)



@app.route(f'{base_url}/GenAI_CS', methods = ['POST', 'GET'])
def GenAI_CS(): #Works!
    print(request.form)
    prompt = request.form['CSInput']
    print(prompt)
    ai = aitextgen(model_folder = "model/csharp", to_gpu=False)
    
    if prompt is not None:
        generated = ai.generate(
            n=1,
            batch_size=10,
            prompt=str(prompt),
            max_length=150,
            temperature=1.0,
            return_as_list=True
        )

    generated = generated[0]
    print("Generated: " + generated)
    data = {'generated_ls': generated}
    session['data'] = generated
    return redirect(url_for("CS_Render"))

@app.route(f'{base_url}/CS_Render', methods = ['POST', 'GET'])
def CS_Render():
    if 'data' in session:
        data = session['data']
        print("Session Data: "+ str(data))
        return render_template('CS-Popup.html', generated=data)



@app.route(f'{base_url}')
def home():
    g="The quick brown fox"
    return render_template('writer_home.html', generated=None, text=g)


@app.route(f'{base_url}', methods=['POST'])
def home_post():
    return redirect(url_for('results'))

@app.route(f'{base_url}/jsRender')
def home_render():
    print("Whole Session:" + str(session))
    if 'data' in session:
        data = session['data']
        print("Session Data: "+ str(data))
        return render_template('writer_home.html', generated=data)
        
    else:
        return render_template('writer_home.html', generated=None)

    
    
@app.route(f'{base_url}/team')
def team():
    return render_template('team.html')

    
@app.route(f'{base_url}/results/')
def results():
    if 'data' in session:
        data = session['data']
        return render_template('Write-your-code-with-AI.html', generated=data)
    else:
        return render_template('Write-your-code-with-AI.html', generated=None)



@app.route(f'{base_url}/generate_text/', methods=["POST"])
def generate_text():
    """
    view function that will return json response for generated text. 
    """

    prompt = request.form['prompt']
    print(prompt)
    genre_type = request.form['genre']
    print('genre type is: ', genre_type)
    story_genre = genre_text_generation(genre_type)
    print('file destination is: ', story_genre)
    ai = aitextgen(model_folder = story_genre, to_gpu=False)
    
    if prompt is not None:
        generated = ai.generate(
            n=1,
            batch_size=10,
            prompt=str(prompt),
            max_length=150,
            temperature=1.0,
            return_as_list=True
        )

    data = {'generated_ls': generated}
    session['data'] = generated[0]
#     return None
    return redirect(url_for('results'))

# define additional routes here
# for example:
# @app.route(f'{base_url}/team_members')
# def team_members():
#     return render_template('team_members.html') # would need to actually make this page


if __name__ == '__main__':
    # IMPORTANT: change url to the site where you are editing this file.
    website_url = 'cocalc11.ai-camp.dev'

    print(f'Try to open\n\n    https://{website_url}' + base_url + '\n\n')
    app.run(host='0.0.0.0', port=port, debug=True)
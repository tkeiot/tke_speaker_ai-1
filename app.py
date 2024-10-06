from flask import Flask, render_template, request, redirect, url_for
import ast
import socket
import json
import os
import subprocess


# Web (Flask) setup
app = Flask(__name__)
JSON_FILE = '/home/pi/tke_speaker_ai/api_key_tke.json'

def read_parameters():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def write_parameters(params):
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(params, f, ensure_ascii=False, indent=4)

@app.route('/')
def index():
    parameters = read_parameters()
    return render_template('index.html', parameters=parameters)

@app.route('/update_parameter/<param>', methods=['POST'])
def update_parameter(param):
    parameters = read_parameters()
    new_value = request.form.get(param)
    
    if new_value:
        parameters[param] = new_value
    
    api_gemini = request.form.get('api_gemini')
    api_chatgpt = request.form.get('api_chatgpt')
    active_home = request.form.get('active_home')
    
    if api_gemini:
        parameters['api_gemini'] = api_gemini
        if api_gemini == "true":
            parameters['api_chatgpt'] = "false"   # Chon true khi trả về false 
        
    if api_chatgpt:
        parameters['api_chatgpt'] = api_chatgpt
        if api_chatgpt=="true":
            parameters['api_gemini'] = "false"
        
    if active_home:
        parameters['active_home'] = active_home

    write_parameters(parameters)
    return redirect(url_for('index'))
    
@app.route('/reset_parameters', methods=['POST'])
def reset_parameters():
    try:
        # Khởi động lại hệ thống
        subprocess.Popen(['sudo', 'reboot'], shell=False)
        return "Hệ thống đang khởi động lại...", 200
    except Exception as e:
        return str(e), 500    

    

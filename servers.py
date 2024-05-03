import os
from flask import Flask, request, jsonify
import server2 as banding
from server2 import rolling_hash

UPLOAD_FOLDER = "Newfolder/"
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    try:
        if request.method == 'POST':
            file = request.files['file']
            files = request.files['files']
            print(file.filename[-3:])
            if (file.filename[-3:] == 'pdf') & (files.filename[-3:] == 'pdf'):
                file.save('Newfolder/'+file.filename)
                files.save('Newfolder/'+files.filename)
                kesamaan = banding.kesamaan(UPLOAD_FOLDER+f'/{file.filename}', UPLOAD_FOLDER+f'/{files.filename}')
                hash1 = []
                hash2 = []
                kgram1 = ''
                kgram2 = ''
                ok=''
                oks=''
                with open('Newfolder/'+file.filename[:-4]+' - preprocessing.txt','r',encoding='utf8') as f:
                    ok = f.read()
                    hash1 = rolling_hash((ok.replace(' ', '')).replace('\n', ' '), 3)
                
                with open('Newfolder/'+files.filename[:-4]+' - preprocessing.txt','r',encoding='utf8') as f:
                    oks = (f.read()).replace(' ', '').replace('\n', ' ')
                    hash2 = rolling_hash((ok.replace(' ', '')).replace('\n', ' '), 3)
                    
                for i in range(len(ok)-3):
                    kgram1 =kgram1 +'['+ ok[i:i+3] + '] '
                
                for i in range(len(oks)-3):
                    kgram2 =kgram2 +'['+ oks[i:i+3] + '] '
                
                return jsonify({"kesamaan":f"{kesamaan}"},{"hash1":' '.join(map(str, hash1))}, {"hash2":' '.join(map(str, hash2))}, {"kgram1":f"{kgram1}"},{"kgram2":f"{kgram2}"},{"preprocessing1":ok},{"preprocessing2":oks})
            else :
                return 'salah file'
    except:
        return "can't read file"
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=file name=files>
      <input type=submit value=Upload>
    </form>
    '''
    
app.run(port=8081, host='0.0.0.0')
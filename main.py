from flask import Flask, request, render_template
from translate import Translator

app = Flask(__name__)

@app.route('/')
def home_page():
  output_file = open('/home/runner/PyLator/templates/output.html', 'w')
  output_file.write('')
  output_file.close()
  return render_template('home.html')

@app.route('/', methods=['POST'])
def translate_input():
  text = request.form['text']
  fl = request.form['fl']
  tl = request.form['tl']
  output_file = open('/home/runner/PyLator/templates/output.html', 'w')
  output_file.write('')
  output_file.close()
  del output_file
  output_file = open('/home/runner/PyLator/templates/output.html', 'w')
  
  if text == '':
    return render_template('blank_input.html')
    
  if fl == '':
    fl = 'en'
  
  if tl == '':
    tl = 'fr'
    
  translation = Translator(to_lang = tl, from_lang = fl).translate(text)
  err = translation.find('EXAMPLE: LANGPAIR=EN|IT USING 2 LETTER ISO OR RFC3066 LIKE ZH-CN. ALMOST ALL LANGUAGES SUPPORTED BUT SOME MAY HAVE NO CONTENT') + 1
  if err:
    print(err)
    tefile = open('/home/runner/PyLator/templates/translation_error1.html', 'w')
    tefile.write(f'''<!DOCTYPE html>
<head>
  <meta charset='utf-8'>
  <meta name='viewport' content='width=device-width'>
  <title>PyLator - Error</title>
  <!--Thanks to jesty0514 (https://www.favicon.cc/?action=icon_list&user_id=279249) for the icon (https://www.favicon.cc/?action=icon&file_id=831343)-->
  <link href='data:image/x-icon;base64,AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAETT//9E0///RNP//0TT//9E0///RNP//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAETT//9E0///RNP//0TT//9E0/////////////9E0///AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABE0///RNP//0TT//9E0///RNP/////////////RNP//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARNP//0TT//9E0///RNP//0TT//9E0///RNP//0TT//8AAAAAAAAAAAAAAAAAAAAAAAAAAJ9wOv+fcDr/n3A6/0TT/5hE0///RNP//0TT//9E0///RNP//0TT//9E0///RNP//0TT//9E0///AAAAAJ9wOv+fcDr/n3A6/59wOv+fcDqVRNP//0TT//9E0///RNP//0TT//9E0///RNP//0TT//9E0///RNP//0TT//+fcDr/n3A6/59wOv+fcDr/RNP/mETT//9E0///RNP//0TT//9E0///RNP//0TT//9E0///RNP//0TT//9E0///n3A6/59wOv+fcDr/n3A6/59wOpVE0/+YRNP/mETT/5hE0/+YRNP/mETT/5hE0///RNP//0TT//9E0///RNP//59wOv+fcDr/n3A6/59wOv+fcDr/n3A6lZ9wOpWfcDqVn3A6lZ9wOpWfcDqVn3A6lUTT//9E0///RNP//0TT//+fcDr/n3A6/59wOv+fcDr/n3A6/59wOv+fcDr/n3A6/59wOv+fcDr/n3A6/0TT/5hE0///RNP//0TT//9E0///n3A6/59wOv+fcDr/n3A6/59wOv+fcDr/n3A6/59wOv+fcDr/n3A6/59wOv+fcDqVRNP//0TT//9E0///RNP//wAAAACfcDr/n3A6/59wOv+fcDr/n3A6/59wOv+fcDr/n3A6/59wOv+fcDr/RNP/mETT//9E0///RNP//wAAAAAAAAAAAAAAAAAAAAAAAAAAn3A6/59wOv+fcDr/n3A6/59wOv+fcDr/n3A6/59wOv8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJ9wOv///////////59wOv+fcDr/n3A6/59wOv+fcDr/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACfcDr///////////+fcDr/n3A6/59wOv+fcDr/n3A6/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJ9wOv+fcDr/n3A6/59wOv+fcDr/n3A6/wAAAAAAAAAAAAAAAAAAAAAAAAAA+B8AAPAPAADwDwAA8A8AAIABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAQAA8A8AAPAPAADwDwAA+B8AAA==' rel='icon' type='image/x-icon'>
</head>

<p style = 'color:#00008c' align = 'center'>{translation}<br></br> If you think this is an error, contact me at <code><strong><a href = 'mailto:PyLator.Info@gmail.com' target='_blank'>PyLator.Info@gmail.com</a></strong></code></p>
<p style = 'color:#00008c' align='center'><br></br><a href="https://PyLator.CodingEssence.Repl.Co">Click here to translate again</a></p>''')
    return render_template('translation_error.html')
    
  output_file.write(f'''<!DOCTYPE html> 
<head> 
  <meta charset='utf-8'> 
  <meta name='viewport' content='width=device-width'> 
  <title>PyLator | Translation</title> 
  <!--Thanks to jesty0514 (https://www.favicon.cc/?action=icon_list&user_id=279249) for the icon (https://www.favicon.cc/?action=icon&file_id=831343)--> 
  <link href="data:image/x-icon;base64,AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAETT//9E0///RNP//0TT//9E0///RNP//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAETT//9E0///RNP//0TT//9E0/////////////9E0///AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABE0///RNP//0TT//9E0///RNP/////////////RNP//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARNP//0TT//9E0///RNP//0TT//9E0///RNP//0TT//8AAAAAAAAAAAAAAAAAAAAAAAAAAJ9wOv+fcDr/n3A6/0TT/5hE0///RNP//0TT//9E0///RNP//0TT//9E0///RNP//0TT//9E0///AAAAAJ9wOv+fcDr/n3A6/59wOv+fcDqVRNP//0TT//9E0///RNP//0TT//9E0///RNP//0TT//9E0///RNP//0TT//+fcDr/n3A6/59wOv+fcDr/RNP/mETT//9E0///RNP//0TT//9E0///RNP//0TT//9E0///RNP//0TT//9E0///n3A6/59wOv+fcDr/n3A6/59wOpVE0/+YRNP/mETT/5hE0/+YRNP/mETT/5hE0///RNP//0TT//9E0///RNP//59wOv+fcDr/n3A6/59wOv+fcDr/n3A6lZ9wOpWfcDqVn3A6lZ9wOpWfcDqVn3A6lUTT//9E0///RNP//0TT//+fcDr/n3A6/59wOv+fcDr/n3A6/59wOv+fcDr/n3A6/59wOv+fcDr/n3A6/0TT/5hE0///RNP//0TT//9E0///n3A6/59wOv+fcDr/n3A6/59wOv+fcDr/n3A6/59wOv+fcDr/n3A6/59wOv+fcDqVRNP//0TT//9E0///RNP//wAAAACfcDr/n3A6/59wOv+fcDr/n3A6/59wOv+fcDr/n3A6/59wOv+fcDr/RNP/mETT//9E0///RNP//wAAAAAAAAAAAAAAAAAAAAAAAAAAn3A6/59wOv+fcDr/n3A6/59wOv+fcDr/n3A6/59wOv8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJ9wOv///////////59wOv+fcDr/n3A6/59wOv+fcDr/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACfcDr///////////+fcDr/n3A6/59wOv+fcDr/n3A6/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJ9wOv+fcDr/n3A6/59wOv+fcDr/n3A6/wAAAAAAAAAAAAAAAAAAAAAAAAAA+B8AAPAPAADwDwAA8A8AAIABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAQAA8A8AAPAPAADwDwAA+B8AAA==" rel="icon" type="image/x-icon">
</head> 

<p style = 'color:#00008c' align = 'center'><strong>{translation}</strong><br></br><a href="https://PyLator.CyberPy.Repl.Co">Click here to translate again</a></p>''')
  output_file.close()
  
  return render_template('output.html')

@app.route('/about')
def about_page():
  return render_template('about.html')

@app.errorhandler(404)
def invalid_route_404(error):
  return render_template('error.html')

@app.route('/translation-error')
def translation_error():
  return render_template('translation_error.html')

@app.route('/translation-error1')
def translation_error1():
  return render_template('translation_error1.html')

@app.route('/blank-input')
def blank_input():
  return render_template('blank_input.html')

@app.route('/output.html')
def blank_output():
  return render_template('blank_output.html')

if __name__ == '__main__':
  app.run(port=443, host='0.0.0.0', debug=True)


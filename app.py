from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('form.html')
@app.route('/submit',methods=['POST'])
def submit():
    name=request.form['name']
    rol=request.form['rol']
    email=request.form['email']
    year=request.form['year']
    return render_template('result.html',name=name,rol=rol,email=email,year=year)
if __name__=='__main__':
    app.run(debug=True)
    
    
    
from flask import Flask,render_template,request,redirect
app_guvi = Flask(__name__)

app_guvi.vars={}

app_guvi.questions={}
app_guvi.questions['How many eyes do you have?']=('1','2','3')
app_guvi.questions['Which fruit do you like best?']=('banana','mango','pineapple')
app_guvi.questions['Do you like cupcakes?']=('yes','no','maybe')

app_guvi.nquestions=len(app_guvi.questions)
#should be 3

@app_guvi.route('/index_guvi',methods=['GET','POST'])
def index_guvi():
    nquestions=app_guvi.nquestions
    if request.method == 'GET':
        return render_template('userinfo_guvi.html',num=nquestions)
    else:
        #request was a POST
        app_guvi.vars['name'] = request.form['name_guvi']
        app_guvi.vars['age'] = request.form['age_guvi']

        f = open('%s_%s.txt'%(app_guvi.vars['name'],app_guvi.vars['age']),'w')
        f.write('Name: %s\n'%(app_guvi.vars['name']))
        f.write('Age: %s\n\n'%(app_guvi.vars['age']))
        f.close()

        return redirect('/main_guvi')

@app_guvi.route('/main_guvi')
def main_guvi2():
    if len(app_guvi.questions)==0 : return render_template('end_guvi.html')
    return redirect('/next_guvi')

#####################################
## IMPORTANT: I have separated /next_guvi INTO GET AND POST
## You can also do this in one function, with If and Else.

@app_guvi.route('/next_guvi',methods=['GET'])
def next_guvi():  #remember the function name does not need to match the URL
    # for clarity (temp variables):
    n=app_guvi.nquestions-len(app_guvi.questions)+1
    q=app_guvi.questions.keys()[0] #python indexes at 0
    # q = list(app.questions.keys())[0] #python indexes at 0
	# Anuar Edition for Pytho 3.4 from following Stackflow source: http://stackoverflow.com/questions/28467967/unhashable-type-dict-keys-works-in-ver-2-7-5-but-not-in-3-4
	# In python3, as opposed to python2, keys returns an iterable set-like view object, not a list. Thus, the need to call the list function on that object to convert it into a list.
    a1=app_guvi.questions[q][0]
    a2=app_guvi.questions[q][1]
    a3=app_guvi.questions[q][2]

    # save current question
    app_guvi.currentq=q

    return render_template('layout_guvi.html',num=n,question=q,ans1=a1,ans2=a2,ans3=a3)

@app_guvi.route('/next_guvi',methods=['POST'])
def next_guvi2():  #can't have two functions with the same name
    # Here, we will collect data from the user.
    # Then, we return to the main function, so it can tell us whether to 
    # display another question page, or to show the end page.

    f=open('%s_%s.txt'%(app_guvi.vars['name'],app_guvi.vars['age']),'a') #a is for append
    f.write('%s\n'%(app_guvi.currentq))
    f.write('%s\n\n'%(request.form['answer_from_layout_guvi'])) #do you know where answer_guvi comes from?
    f.close()

    app_guvi.questions.pop(app_guvi.currentq)

    return redirect('/main_guvi')

if __name__ == "__main__":
    app_guvi.run()

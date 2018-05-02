from flask import Flask, session,render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from questionsdb import Base, Answers, Questions, CQuestions, JQuestions, DSQuestions, DBMSQuestions,User

app = Flask(__name__)

engine = create_engine('sqlite:///questions.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
dbsession = DBSession()

user_login=False

@app.route("/")
@app.route("/registerationForm")
@app.route("/register",methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        obj=User(request.form['Roll_No'],request.form['Name'],request.form['password'])
        obj.insertion()
        return render_template('login.html')
    else:
        return render_template('register.html')

# @app.route("/register",methods = ['GET','POST'])
# def register():
#     if request.method =='POST':
#         Roll_No = request.form['Roll_No']
#         name = request.form['Name']
#         password = request.form['password']

#         try:
#             user = Users(Roll_No,name,password)
#             # db.session.add(user)
#             # db.session.commit()
#             flash("registered successfully")
#         except:
#             # db.session.rollback()
#             flash("Insert unsuccessful")
#     # db.session.close()
#     return render_template("login.html")

@app.route("/loginForm")
@app.route("/login", methods = ['POST', 'GET'])
def login():
    if request.method=='POST':
        user1=''
        try:
            print("in try")
            users=dbsession.query(User).filter_by(user_id=request.form['Roll_No']).one()
            print('after')

            if users.password==request.form['password']:
                print('in if')
                session['uid']=users.user_id
                return render_template('ListofCourses.html')
            else:
                flash("Wrong password. Please try again")
                return render_template('login.html')
        except:
            flash("Please register first")
            return render_template('login.html')
    else:
        return render_template('login.html')

		
		# Roll_No = request.form['Roll_No'] # request .form is a string
		# password = request.form['password']
		
		# if is_valid(Roll_No,password):
		# 	# session['Roll_No'] = Roll_No
		# 	return render_template('ListofCourses.html')
		# else:
		# 	error = 'Invalid UserId / Password'
		# 	return render_template('login.html', error=error)

# def is_valid(Roll_No,password):
# 	stmt = "SELECT Roll_No, password FROM users"
# 	data = db.engine.execute(stmt).fetchall()
# 	print(data)
# 	for row in data:
# 		# print row[0]==int(Roll_No) #type cast to integer
# 		# print row[1]==password
# 		if row[0] == int(Roll_No) and row[1] == password:

# 			return True
# 		return False

# @app.route('/logout')
# def logout():
# 	session.pop('logged_in', None)
# 	flash('You were logged out')
# 	return redirect(url_for('show_entries'))


# @app.route("/registerationForm")
# def registrationForm():
# 	return render_template("register.html")


# @app.route("/loginForm")
# def log():
# 	return render_template("login.html")

# @app.route("/PythonResources")
# def Python():
# 	return render_template("PythonResources.html")

# @app.route("/JavaResources")
# def Java():
# 	return render_template("JavaResources.html")

# @app.route("/C_Resources")
# def C_Lang():
# 	return render_template("C_Resources.html")

# @app.route("/Datastructures_Resources")
# def DataStruct():
# 	return render_template("DatastructureResource.html")

# @app.route("/DATA_BASE_MANAGEMENT_Resources")
# def DataBase():
# 	return render_template("DbmsResource.html")

# app.route('/logout')
# def loggingout():
#     # global user_login
#     if 'uid' in session:
#         # Query = dbsession.query(Cart).all()        
#         # for qq in Query:
#         #     dbsession.delete(qq)
#         #     dbsession.commit()
#         session.pop('uid', None)
#         return render_template('login.html')
#     else:
#         return render_template('register.html')

@app.route('/logout')
def logout():
    return render_template('register.html')

@app.route("/PythonResources")
@app.route('/Python',methods=['GET','POST'])
def Python():
    if request.method == 'POST':
        q=''
        try:
            obj=Questions(request.form['question'],'python',1)
            # print(request.form['question'])
            obj.insertion()
            q=dbsession.query(Questions).filter_by(cid=1)
        # if q2!='':
        # for each in q2:
        # q=each.question
        # print 'xyz'
        # error='abcd'
        # q=obj.question
        # flash("There are no questions. Please post a question.")
        # for q1 in q:
        # print (q1.question)
            return render_template('PythonResources.html',p=q)
        except:
            print 'abc'
            error='There are no questions. Please post a question.'
            flash("There are no questions. Please post a question.")
            return render_template('PythonResources.html',error=error)
    else:
        q=dbsession.query(Questions).filter_by(cid=1)
        print '123'
        return render_template('PythonResources.html',p=q)

# @app.route('/PythonResources',methods=['GET','POST'])
# def course():
#     if request.method == 'POST':
#         q=''
#         try:
#             obj=Questions(request.form['question'])
#             obj.insertion()
#             q=dbsession.query(Questions).all()
#             return render_template('PythonResources.html',p=q)
#         except:
#             print 'abc'
#             # error='There are no questions. Please post a question.'
#             flash("There are no questions. Please post a question.")
#             return render_template('PythonResources.html')
#     else:
#         q=dbsession.query(Questions).all()
#         return render_template('PythonResources.html',p=q)

    # if 'uid' in session:
    #     q=''
    #     if request.method == 'POST':
    #         try:
    #             obj=Questions(request.form['question'])
    #             obj.insertion()
    #             q=session.query(Questions).all()
    #             return render_template('PythonResources.html',p=q)
    #         except:
    #             print 'abc'
    #             # error='There are no questions. Please post a question.'
    #             flash("There are no questions. Please post a question.")
    #             return render_template('PythonResources.html')
    #     else:
    #         q=dbsession.query(Questions).all()
    #         return render_template('PythonResources.html',p=q)
    # 	print '123'
    # 	return render_template('frontpage.html')


@app.route('/JavaResources',methods=['GET','POST'])
def Java():
   if request.method == 'POST':
    q=''
    try:
        obj=Questions(request.form['question'],'java',2)
        print(request.form['question'])
        obj.insertion()
        q=dbsession.query(Questions).filter_by(cid=2)
        # if q2!='':
        # for each in q2:
        # q=each.question
        # print 'xyz'
        # error='abcd'
        # q=obj.question
        # flash("There are no questions. Please post a question.")
        # for q1 in q:
        # print (q1.question)
        return render_template('JavaResources.html',j=q)
    except:
        print 'abc'
        error='There are no questions. Please post a question.'
        flash("There are no questions. Please post a question.")
        return render_template('JavaResources.html',error=error)
   else:
    q=dbsession.query(Questions).filter_by(cid=2)
    print '123'
    return render_template('JavaResources.html',j=q)

@app.route('/Datastructures_Resources',methods=['GET','POST'])
def DataStruct():
   if request.method == 'POST':
    q=''
    try:
        obj=Questions(request.form['question'],'ds',3)
        obj.insertion()
        q=dbsession.query(Questions).filter_by(cid=3)
        # if q2!='':
        # for each in q2:
        # q=each.question




        # print 'xyz'
        # error='abcd'
        # q=obj.question
        # flash("There are no questions. Please post a question.")
        # for q1 in q:
        # print (q1.question)
        return render_template('DatastructureResource.html',p=q)
    except:
        print 'abc'
        error='There are no questions. Please post a question.'
        flash("There are no questions. Please post a question.")
        return render_template('DatastructureResource.html',error=error)
   else:
    q=dbsession.query(Questions).filter_by(cid=3)
    print '123'
    return render_template('DatastructureResource.html',p=q)

@app.route('/C_Resources',methods=['GET','POST'])
def C_Lang():
   if request.method == 'POST':
    q=''
    try:
        obj=Questions(request.form['question'],'c',4)
        obj.insertion()
        q=dbsession.query(Questions).filter_by(cid=4)
        # if q2!='':
        # for each in q2:
        # q=each.question




        # print 'xyz'
        # error='abcd'
        # q=obj.question
        # flash("There are no questions. Please post a question.")
        # for q1 in q:
        # print (q1.question)
        return render_template('C_Resources.html',c=q)
    except:
        print 'abc'
        error='There are no questions. Please post a question.'
        flash("There are no questions. Please post a question.")
        return render_template('C_Resources.html',error=error)
   else:
    q=dbsession.query(Questions).filter_by(cid=4)
    print '123'
    return render_template('C_Resources.html',c=q)

@app.route('/DATA_BASE_MANAGEMENT_Resources',methods=['GET','POST'])
def DataBase():
   if request.method == 'POST':
    q=''
    try:
        #print(request.form['dbmsquestion'])
        obj=Questions(request.form['question'],'dbms',5)
        # str=''
        # str=obj.question
        # print(str)
        obj.insertion()
        q=dbsession.query(Questions).filter_by(cid=5)
        # if q2!='':
        # for each in q2:
        # q=each.question




        # print 'xyz'
        # error='abcd'
        # q=obj.question
        # flash("There are no questions. Please post a question.")
        # for q1 in q:
        # print (q1.question)
        return render_template('DbmsResource.html',p=q)
    except:
        print 'abc'
        error='There are no questions. Please post a question.'
        flash("There are no questions. Please post a question.")
        return render_template('DbmsResource.html',error=error)
   else:
    q=dbsession.query(Questions).filter_by(cid=5)
    print '123'
    return render_template('DbmsResource.html',p=q)

@app.route("/<int:course>/<int:question>/PythonAnswers", methods=['GET','POST'])
def PythonAnswers(course,question):
    q=''
    ans_id=question
    ans=''
    if request.method == 'POST':
        try:
            print('in try')
            # q=dbsession.query(Questions).filter_by(id=question)
            q=dbsession.query(Questions).get(question)
            print(q.id)
            obj=Answers(course,ans_id,request.form['answer'],0,0)
            print(obj.ans_id)
            print(obj.answer)
            obj.insertion()
            ans=dbsession.query(Answers).filter_by(course_id=course, ans_id=ans_id).all()
            return render_template('PythonAnswers.html',q1=q,a=ans)
        except:
            print 'abc'
    else:
        q=dbsession.query(Questions).filter_by(id=question).one()
        ans=dbsession.query(Answers).filter_by(course_id=course,ans_id=ans_id).all()
        # ans=dbsession.query(Answers).all()
        # str=''
        # str=q.question
        # print (str)

    return render_template('PythonAnswers.html',q1=q,a=ans)

@app.route("/<int:course>/<int:question>/JavaAnswers", methods=['GET','POST'])
def JavaAnswers(course,question):
    q=''
    ans_id=question
    ans=''
    if request.method == 'POST':
        try:
            print('in try')
            # q=dbsession.query(Questions).filter_by(id=question)
            q=dbsession.query(Questions).get(question)
            print(q.id)
            obj=Answers(course,ans_id,request.form['answer'],0,0)
            print(obj.ans_id)
            print(obj.answer)
            obj.insertion()
            ans=dbsession.query(Answers).filter_by(course_id=course,ans_id=ans_id).all()
            return render_template('JavaAnswers.html',q1=q,a=ans)
        except:
            print 'abc'
    else:
        q=dbsession.query(Questions).filter_by(id=question).one()
        ans=dbsession.query(Answers).filter_by(course_id=course,ans_id=ans_id).all()
        # ans=dbsession.query(Answers).all()
        # str=''
        # str=q.question
        # print (str)

    return render_template('JavaAnswers.html',q1=q,a=ans)

@app.route("/<int:course>/<int:question>/DSAnswers", methods=['GET','POST'])
def DSAnswers(course,question):
    q=''
    ans_id=question
    ans=''
    if request.method == 'POST':
        try:
            print('in try')
            # q=dbsession.query(Questions).filter_by(id=question)
            q=dbsession.query(Questions).get(question)
            print(q.id)
            obj=Answers(course,ans_id,request.form['answer'],0,0)
            print(obj.ans_id)
            print(obj.answer)
            obj.insertion()
            ans=dbsession.query(Answers).filter_by(course_id=course, ans_id=ans_id).all()
            return render_template('DSAnswers.html',q1=q,a=ans)
        except:
            print 'abc'
    else:
        q=dbsession.query(Questions).filter_by(id=question).one()
        ans=dbsession.query(Answers).filter_by(course_id=course,ans_id=ans_id).all()
        # ans=dbsession.query(Answers).all()
        # str=''
        # str=q.question
        # print (str)

    return render_template('DSAnswers.html',q1=q,a=ans)

@app.route("/<int:course>/<int:question>/CAnswers", methods=['GET','POST'])
def CAnswers(course,question):
    q=''
    ans_id=question
    ans=''
    if request.method == 'POST':
        try:
            print('in try')
            # q=dbsession.query(Questions).filter_by(id=question)
            q=dbsession.query(Questions).get(question)
            print(q.id)
            obj=Answers(course,ans_id,request.form['answer'],0,0)
            print(obj.ans_id)
            print(obj.answer)
            obj.insertion()
            ans=dbsession.query(Answers).filter_by(course_id=course, ans_id=ans_id).all()
            return render_template('CAnswers.html',q1=q,a=ans)
        except:
            print 'abc'
    else:
        q=dbsession.query(Questions).filter_by(id=question).one()
        ans=dbsession.query(Answers).filter_by(course_id=course,ans_id=ans_id).all()
        # ans=dbsession.query(Answers).all()
        # str=''
        # str=q.question
        # print (str)

    return render_template('CAnswers.html',q1=q,a=ans)

@app.route("/<int:course>/<int:question>/DBMSAnswers", methods=['GET','POST'])
def DBMSAnswers(course,question):
    q=''
    ans_id=question
    ans=''
    if request.method == 'POST':
        try:
            print('in try')
            # q=dbsession.query(Questions).filter_by(id=question)
            q=dbsession.query(Questions).get(question)
            print(q.id)
            obj=Answers(course,ans_id,request.form['answer'],0,0)
            print(obj.ans_id)
            print(obj.answer)
            obj.insertion()
            ans=dbsession.query(Answers).filter_by(course_id=course, ans_id=ans_id).all()
            return render_template('DBMSAnswers.html',q1=q,a=ans)
        except:
            print 'abc'
    else:
        q=dbsession.query(Questions).filter_by(id=question).one()
        ans=dbsession.query(Answers).filter_by(course_id=course,ans_id=ans_id).all()
        # ans=dbsession.query(Answers).all()
        # str=''
        # str=q.question
        # print (str)

    return render_template('DBMSAnswers.html',q1=q,a=ans)

@app.route("/PythonAnswers/<int:question>/<int:posts>/Upvotes", methods=['GET','POST'])
def Upvotes(question,posts):
    print('in function')
    print(question)
    print(posts)
    if request.method == 'POST':
        try:
            print('in try')
            ans=dbsession.query(Answers).filter_by(ans_id=ans_id).one()
            ans.upvotes+=1
            q=dbsession.query(Questions).get(question)
            return render_template('PythonAnswers',q1=q,a=ans)
        except:
            print 'abc'
    else:
        print('in get')

        q=dbsession.query(Questions).get(question)
        ans=dbsession.query(Answers).filter_by(ans_id=ans_id).one()
        return render_template('PythonAnswers',q1=q,a=ans)

@app.route("/Downvotes/<int:posts>", methods=['GET','POST'])
def Downvotes(posts):
    if request.method == 'POST':
        try:
            ans=dbsession.query(Answers).filter_by(ans_id=ans_id).all()
            ans.downvotes+=1
            q=dbsession.query(Questions).get(question)
            return render_template('PythonAnswers',q1=q,a=ans)
        except:
            print 'abc'
    else:
        q=dbsession.query(Questions).get(question)
        ans=dbsession.query(Answers).filter_by(ans_id=ans_id).all()
        return render_template('PythonAnswers',q1=q,a=ans)





if __name__=='__main__':
    app.secret_key='super secret key'
    app.debug=True
    app.run(host='0.0.0.0', port=5000)

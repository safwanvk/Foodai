import base64

from flask import Flask, render_template, request, session, redirect
import datetime
from flask.json import jsonify
from connection import conn
app = Flask(__name__)
app.secret_key="hi"
import os

UPLOAD_FOLDER = "/home/safwan/Documents/projects/python/Zabchef/recipe/static/recipe"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/sign_temp')
def sign_temp():
    return render_template("signuptemp.html")

@app.route('/')
def adm_log():
    return render_template("adm_login.html")
@app.route('/adm_login',methods=["post"])
def adm_login():
    name=request.form["txt_uname"]
    password=request.form["txt_pswd"]
    s="select type,loginid from tbl_login where uname='"+name+"' and password='"+password+"'"
    obj=conn()
    t=obj.selectone(s)

    if t is not None:
        type = t[0]
        print(type)
        if type == "admin":
            return load_index()
        elif type=="store":
            session["lgid"]=t[1]
            return render_template('/Store/home.html')
        elif type=="user":
            session["log_id"]=t[1]
            session["emid"]=name
            return redirect('/user_viewprofile')
        else:
            return "<script>alert('invalid user name and password');window.location='/'</script>"
    else:
        return "<script>alert('invalid user name and password');window.location='/'</script>"


@app.route('/adm_home')
def adm_home():
    return render_template("adm _home.html")
@app.route('/st_home')
def st_home():
    return render_template('/Store/home.html')

@app.route('/adm_addveg')
def addveg():
    return render_template("adm_addveg.html")
@app.route('/addveg_post',methods=["post"])
def addveg_post():
    name=request.form["txt_vegname"]
    description=request.form["txt_descrip"]
    i="insert into tbl_vegetables(name,description) values('" + name + "','" + description + "')"
    obj=conn()
    obj.nonreturn(i)
    return adm_viewveg()

@app.route('/back_btn',methods=["post"])
def back_veg():
    return addveg()

@app.route('/adm_viewveg')
def adm_viewveg():
    s="select * from tbl_vegetables"
    obj=conn()
    v=obj.selectall(s)
    return render_template("adm_view_veg.html", data=v)


@app.route('/adm_edit/<id>')
def adm_edit(id):
    s="select * from tbl_vegetables WHERE veg_id='"+id+"'"
    obj=conn()
    e=obj.selectone(s)
    return render_template("adm_update_veg.html",data=e)


@app.route('/adm_update_veg',methods=["post"])
def update_veg():
    id=request.form['veg_id']
    name=request.form['txt_vegname']
    description=request.form['txta_description']
    up="update tbl_vegetables set name='"+name+"',description='"+description+"' where veg_id='"+id+"'"
    obj=conn()
    obj.nonreturn(up)
    return adm_viewveg()

@app.route('/delete/<id>')
def delete(id):
    d="delete from tbl_vegetables WHERE veg_id='"+id+"'"
    obj=conn()
    obj.nonreturn(d)
    return adm_viewveg()

@app.route('/adm_addrecipe')
def adm_addrecipe():
    return render_template("adm_addrecipe.html")
@app.route('/adm_adrecipe',methods=["post"])
def adm_adrecipe():
    rimage = request.files["file_rimage"]

    rname = request.form["txt_rname"]
    session["name"]=rname

    descript=request.form["txta_description"]
    session["des"]=descript

    make=request.form["txta_make"]
    session["making"]=make

    date=str(datetime.datetime.now()).replace(" ","_").replace(":","_").replace("-","_")
    rimage.save(os.path.join(app.config['UPLOAD_FOLDER'], ""+date+".jpg"))
    # rimage.save("E:\\project\\recipe_py\\recipe\\static\\recipe\\"+date+".jpg")
    path="/static/recipe/"+date+".jpg"
    session["image"] = path

    j="select max(reci_id) from tbl_recipe"
    obj = conn()
    r=obj.mid(j)
    i="insert into tbl_recipe(reci_id,name,description,how_to_make,type,author_id,photo,status)values('"+str(r)+"','" + rname + "','" + descript + "','"+make+"','admin','0','"+path+"','approved')"
    obj.nonreturn(i)
    session['rid']=r

    return ingredients()

@app.route('/adm_reci_ingredients')
def ingredients():
    obj = conn()
    s = "select * from tbl_vegetables "
    v = obj.selectall(s)

    i=session["image"]
    n= session["name"]
    d= session["des"]
    m=session["making"]

    s="select tbl_ingredients.*,tbl_vegetables.name from tbl_ingredients inner join tbl_vegetables on tbl_ingredients.veg_id=tbl_vegetables.veg_id where tbl_ingredients.reci_id='"+str(session['rid'])+"'"
    obj = conn()
    ing= obj.selectall(s)
    print(s)
    print(ing)

    return render_template("adm_recipedetails.html",data=v,image=i,name=n,description=d,howto=m,i=ing)



@app.route('/added_items/<id>')
def add_items(id):
    i="insert into tbl_ingredients(reci_id,veg_id)values('"+str(session['rid'])+"','"+id+"')"
    obj=conn()
    obj.nonreturn(i)
    return ingredients()

@app.route('/itemveg_view')
def veg_view():
    s = "select * from tbl_ingredients"
    obj = conn()
    v = obj.selectall(s)
    return render_template("adm_recipedetails.html", data=v)

@app.route('/reciveg_delete/<id>')
def reciveg_dele(id):
    d="delete from tbl_ingredients WHERE serial_no='"+id+"'"
    print(d)
    obj=conn()
    obj.nonreturn(d)
    return ingredients()

@app.route('/search_ing',methods=["post"])
def search_ing():
    b=request.form["btn"]
    if b=="Search":
        ing_name=request.form["txt_search"]
        s="select * from tbl_vegetables where name LIKE '%"+ing_name+"%'"
        obj=conn()
        v=obj.selectall(s)
        i=session["image"]
        n= session["name"]
        d= session["des"]
        m=session["making"]

        s="select tbl_ingredients.*,tbl_vegetables.name from tbl_ingredients inner join tbl_vegetables on tbl_ingredients.veg_id=tbl_vegetables.veg_id where tbl_ingredients.reci_id='"+str(session['rid'])+"'"
        obj = conn()
        ing= obj.selectall(s)
        print(s)
        print(ing)

        return render_template("adm_recipedetails.html",data=v,image=i,name=n,description=d,howto=m,i=ing)
    elif b=="Finish":
        return "<script>alert('completed');window.location='/adm_recipies'</script>"
    elif b=="Delete":
        d1 = "delete from tbl_recipe where reci_id='" + str(session['rid']) + "'"
        obj = conn()
        obj.nonreturn(d1)
        d2 = "delete from tbl_ingredients where reci_id ='" + str(session['rid']) + "'"
        obj = conn()
        obj.nonreturn(d2)
        return "<script>alert('Deleted');window.location='/adm_recipies'</script>"
    else:
        return "no"

@app.route('/adm_viewcomplaint')
def adm_viewcomp():
    s ="select tbl_complaint.*,tbl_user.name,tbl_user.Reg_id from tbl_complaint inner join tbl_user on tbl_complaint.user_id =tbl_user.Reg_id where status='pending'"
    obj=conn()
    v=obj.selectall(s)

    s1 = "select tbl_complaint.*,tbl_user.name,tbl_user.Reg_id from tbl_complaint inner join tbl_user on tbl_complaint.user_id =tbl_user.Reg_id where status='replied'"
    obj = conn()
    v1 = obj.selectall(s1)
    return render_template("adm_viewcomplaints.html", data=v,data1=v1)

@app.route('/adm_viewfeedback')
def adm_viewfeed():
    s="select tbl_feedback.*,tbl_user.name,tbl_user.Reg_id from tbl_feedback inner join tbl_user on tbl_feedback.reg_id =tbl_user.Reg_id"
    obj=conn()
    v=obj.selectall(s)
    qry="update tbl_feedback set status='seen'"
    obj.nonreturn(qry)
    return render_template("adm_viewfeedback.html",data=v)


@app.route('/adm_viewusers')
def adm_viewuser():
    s="select * from tbl_user"
    obj=conn()
    v=obj.selectall(s)
    return render_template("adm_viewusers.html",data=v)



@app.route('/lkma')
def lkma():
    return  render_template('lkindex.html')


@app.route('/adm_reply/<compid>')
def adm_reply(compid):
    session["compid"]=compid
    s="select complaint,reply from tbl_complaint where comp_id='"+compid+"'"
    obj=conn()
    v=obj.selectone(s)
    return render_template("adm_reply.html",com=v[0],rep=v[1])
@app.route('/admreply_post',methods=["post"])
def admreply_post():
    reply=request.form["txt_reply"]
    up="update tbl_complaint set reply='"+reply+"',status='replied' where comp_id='"+str(session["compid"])+"'"
    obj = conn()
    obj.nonreturn(up)
    return adm_viewcomp()

@app.route('/adm_addvegpic/<vegid>')
def adm_addvegpic(vegid):
    session["veg_id"]=vegid
    s1="select name from tbl_vegetables where veg_id='"+vegid+"'"
    s="select image_id,path from tbl_vegimage where veg_id='"+str(session["veg_id"])+"'"
    obj=conn()
    v=obj.selectall(s)
    v1=obj.selectone(s1)
    return render_template("adm_vegphotos.html",data=v,vegname=v1[0])
@app.route('/btn_addvegpic',methods=["post"])
def btn_addvegpic():
    return render_template("adm_uploadvegphoto.html")
@app.route('/vegimg_upload',methods=["post"])
def vegimg_upload():
    im=str(session["veg_id"])
    img=request.files["file_photo"]
    date = str(datetime.datetime.now()).replace(" ", "_").replace(":", "_").replace("-", "_")
    img.save("E:\\project\\recipe_py\\recipe\\static\\veg_photos\\" + date + ".jpg")
    path = "/static/veg_photos/" + date + ".jpg"
    i="insert into tbl_vegimage(veg_id,path)VALUES('"+str(session["veg_id"])+"','"+path+"')"
    obj=conn()
    obj.nonreturn(i)
    return adm_addvegpic(im)
@app.route('/admveg_delete/<id>')
def admveg_delete(id):
    im = str(session["veg_id"])
    d="delete from tbl_vegimage WHERE image_id='"+id+"'"
    obj=conn()
    obj.nonreturn(d)
    return adm_addvegpic(im)

@app.route('/adm_recipies')
def adm_recipies():
    s="select reci_id,name,photo from tbl_recipe where author_id='0'"
    obj=conn()
    val=obj.selectall(s)
    return render_template("adm_recipies.html",data=val)
@app.route('/adm_recisearch',methods=["post"])
def adm_recisearch():
    search=request.form["txt_search"]
    s = "select reci_id,name,photo from tbl_recipe where name LIKE '%" + search + "%'"
    obj = conn()
    val = obj.selectall(s)
    return render_template("adm_recipies.html", data=val)

@app.route('/adm_recidetails/<id>')
def adm_recidetails(id):
    s="select name,description,how_to_make,photo from tbl_recipe where reci_id='"+id+"'"
    obj=conn()
    r=obj.selectone(s)
    session["name"] = r[0]
    session["des"] = r[1]
    session["making"] = r[2]
    session["image"] = r[3]
    session["rid"] = id
    s1 = "select * from tbl_vegetables where veg_id not in (select tbl_vegetables.veg_id from tbl_ingredients inner join tbl_vegetables on tbl_ingredients.veg_id=tbl_vegetables.veg_id where tbl_ingredients.reci_id='" + id + "' )"
    obj = conn()
    v = obj.selectall(s1)
    s2 = "select tbl_ingredients.*,tbl_vegetables.name from tbl_ingredients inner join tbl_vegetables on tbl_ingredients.veg_id=tbl_vegetables.veg_id where tbl_ingredients.reci_id='" + id + "'"
    obj = conn()
    ing = obj.selectall(s2)
    return render_template("adm_recipedetails.html", data=v, image=r[3], name=r[0], description=r[1], howto=r[2], i=ing)

@app.route('/adm_vusereci')
def adm_vusereci():
    s="select tbl_user.name,tbl_recipe.name,tbl_recipe.photo,tbl_recipe.reci_id from tbl_recipe inner join tbl_user on tbl_recipe.author_id=tbl_user.Reg_id where tbl_recipe.status='pending'"
    obj=conn()
    ur=obj.selectall(s)

    s1 = "select tbl_user.name,tbl_recipe.name,tbl_recipe.photo from tbl_user inner join tbl_recipe on tbl_user.Reg_id =tbl_recipe.author_id where status='approved'"
    obj = conn()
    v1 = obj.selectall(s1)

    return render_template("adm_usr_recipe.html",recipe=ur,data1=v1)

@app.route('/adm_approveureci/<id>')
def adm_approveureci(id):
    u="update tbl_recipe set status='approved' where reci_id='"+id+"'"
    obj=conn()
    obj.nonreturn(u)
    return adm_vusereci()

@app.route('/adm_logout')
def adm_logout():
    return render_template("adm_login.html")

@app.route('/adm_loadindex')
def adm_loadindex():
    return render_template("adm _home.html")

@app.route('/load_index')
def load_index():
    obj=conn()
    qry="select count(comp_id) from tbl_complaint where status='pending'"
    r1=obj.selectone(qry)
    qry2="select count(reci_id) from tbl_recipe where status='pending'"
    r2=obj.selectone(qry2)
    qry3="select count(feedback_id) from tbl_feedback where status='pending'"
    r3=obj.selectone(qry3)

    c_cnt=0
    r_cnt=0
    f_cnt=0
    if r1[0]>0:
        c_cnt=r1[0]
    if r2[0]>0:
        r_cnt=r2[0]
    if r3[0]>0:
        f_cnt=r3[0]
    return render_template("adm _home.html",c_cnt=c_cnt,r_cnt=r_cnt,f_cnt=f_cnt)


@app.route('/user_login',methods=["post"])
def user_login():
    name=request.form["username"]
    password=request.form["password"]
    s="select type from tbl_login where email='"+name+"' and password='"+password+"'"
    obj=conn()
    t=obj.selectone(s)
    print(s)
    print(t)
    if str(t[0])=='user':
     id="select Reg_id from tbl_user where email='"+name+"'"
     obj=conn()
     v=obj.selectone(id)
     regid=v[0]
     return jsonify(status="ok",id=regid)
    else:
        return jsonify(status="no")

@app.route('/uregister',methods=["post"])
def u_register():
    name=request.form["name"]
    gender = request.form["gender"]
    hname = request.form["house_nm"]
    street = request.form["street"]
    district = request.form["district"]
    pin = request.form["pin"]
    phone = request.form["phone_no"]
    email = request.form["email"]
    passw = request.form["pass"]
    c = conn()
    ck="select * from tbl_user where email='"+email+"'"
    chk = c.selectone(ck)
    if chk is None:
        i="insert into tbl_user( name, house_nm, district, street, pin, gender, phone_no, email) values ('"+name+"','"+hname+"','"+district+"','"+street+"','"+pin+"','"+gender+"','"+phone+"','"+email+"')"
        c.nonreturn(i)
        i="INSERT INTO `tbl_login`(uname,password,type) VALUES ('"+email+"','"+passw+"','user')"
        print(i)
        c.nonreturn(i)
        return jsonify(status="ok")
    else:
        return jsonify(status="no")

@app.route('/takepic',methods=['post'])
def takepic():

    fnam=request.form["image"]
    import base64
    with open("E:\\project\\recipe_py\\recipe\\static\\imageToSave.png", "wb") as fh:
        fh.write(base64.decodebytes(fnam))
    return "hiii"






@app.route('/android_login',methods=["POST"])
def android_login():
    uname=request.form["name"]
    pasw=request.form["password"]
    c=conn()
    qry="SELECT * FROM `tbl_login` WHERE `uname`='"+uname+"' AND `password`='"+pasw+"'"
    res=c.selectone(qry)
    print(qry)
    if res is not None:
        ary="SELECT `Reg_id` FROM `tbl_user` WHERE `email`='"+uname+"'"
        res1=c.selectone(ary)
        print("ary",ary)
        if res1 is not None:
            return jsonify(status="ok",id=res1[0])
        else:
            return jsonify(status="no")
    else:
        return jsonify(status="no")


@app.route('/andsentcomplaint',methods=["POST"])
def andsentcomplaint():
    uid=request.form["uid"]
    complaint=request.form["complaint"]
    c=conn()
    qr="INSERT INTO `tbl_complaint` (`user_id`,`complaint`,`reply`,`date`,`status`) VALUES ('"+uid+"','"+complaint+"','pending',NOW(),'pending')"
    c.nonreturn( qr)
    return jsonify(status="ok")


@app.route('/andsentfeedback',methods=["POST"])
def andsentfeedback():
    uid=request.form["uid"]
    complaint=request.form["complaint"]
    c=conn()
    qr="INSERT INTO tbl_feedback (reg_id,feedback,date,status) VALUES ('"+uid+"','"+complaint+"',NOW(),'pending')"
    c.nonreturn( qr)
    return jsonify(status="ok")


@app.route('/viewallrecipee',methods=['POST'])
def viewllrecipees():
    qry="SELECT `reci_id`,`name`,`description`,`how_to_make`,`photo`  FROM `tbl_recipe`"
    c=conn()
    res=c.jsonselectall(qry)
    print(res)
    return jsonify(status="ok",data=res)


@app.route('/userviewallrecipee',methods=['POST'])
def userviewllrecipees():
    uid=request.form["uid"]
    qry="SELECT `reci_id`,`name`,`description`,`how_to_make`,`photo`  FROM `tbl_recipe` where author_id='"+uid+"'"
    c=conn()
    res=c.jsonselectall(qry)
    print(res)
    return jsonify(status="ok",data=res)


@app.route('/viewallrecipeesearch',methods=['POST'])
def viewallrecipeesearch():
    kw=request.form["kw"]
    qry="SELECT `reci_id`,`name`,`description`,`how_to_make`,`photo`  FROM `tbl_recipe` where name like '%"+kw+"%'"
    c=conn()
    res=c.jsonselectall(qry)
    print(res)
    return jsonify(status="ok",data=res)

@app.route('/userviewallrecipeesearch',methods=['POST'])
def userviewallrecipeesearch():
    kw=request.form["kw"]
    uid = request.form["uid"]
    qry="SELECT `reci_id`,`name`,`description`,`how_to_make`,`photo`  FROM `tbl_recipe` where name like '%"+kw+"%' and author_id='"+uid+"'"
    c=conn()
    res=c.jsonselectall(qry)
    print(res)
    return jsonify(status="ok",data=res)

@app.route('/viewincredientbyrecpid',methods=["POST"])
def viewddsds():
    id=request.form["recpid"]
    qry="SELECT name,`description` FROM `tbl_vegetables` INNER JOIN `tbl_ingredients`  ON `tbl_ingredients`.`veg_id`=`tbl_vegetables`.`veg_id` WHERE `tbl_ingredients`.`reci_id`='"+id+"'"
    c=conn()
    res=c.jsonselectall(qry)
    print(res)
    return jsonify(status="ok",data=res)


@app.route('/viewcompalintsandroid',methods=['POST'])
def viewcompalintsandroid():
    uid=request.form["uid"]
    qry="SELECT `complaint`,`reply`,`date`,`status` FROM `tbl_complaint` WHERE `user_id`='"+uid+"'"
    c=conn()
    res=c.jsonselectall(qry)
    return  jsonify(status="ok", data=res)


@app.route('/recp_items',methods=['post'])
def recp_items():
    rid=request.form["rid"]

    db=conn()


    qry="select * from tbl_vegetables where veg_id in (select veg_id from tbl_ingredients where reci_id='"+rid+"' )"
    res=db.jsonselectall(qry)
    return jsonify(status="ok",data=res)


@app.route('/avl_store',methods=['post'])
def avl_stores():
    rid=request.form["vid"]

    db=conn()


    qry="select * from store where logid in (select slogid from storevegitems where vegid='"+rid+"')"
    print(qry)
    res=db.jsonselectall(qry)
    return jsonify(status="ok",data=res)







@app.route('/uploadpohoto',methods=["POST"])
def uploadpohoto():
    img=request.form["pro_image"]
    a = base64.b64decode(img)
    fh = open("E:\\project\\recipe_py\\recipe\\static\\a.jpg", "wb")
    fh.write(a)
    fh.close()
    from clarifai.rest import ClarifaiApp
    app = ClarifaiApp(api_key='78742f93a0874e6c93db0aa67f5bb25e')
    model = app.models.get('tomato')
    response = model.predict_by_filename(filename='E:\\project\\recipe_py\\recipe\\static\\a.jpg')
    print(response)
    print("hrrrr")
    arrs = (response["outputs"][0]["data"]["concepts"])
    vegs=[]
    recpid=[]
    recpcnt=[]
    for m in arrs:
        name = (m["name"])
        value = (m["value"])
        print(name,value)
        if value > 0.1:
            vegs.append(name)
    qry="select * from tbl_recipe"
    c=conn()
    print(vegs)
    res=c.selectall(qry)
    for i in res:
        qry1="SELECT `name` FROM `tbl_vegetables` INNER JOIN `tbl_ingredients` ON `tbl_ingredients`.`veg_id`=`tbl_vegetables`.`veg_id` WHERE `tbl_ingredients`.`reci_id`='"+str(i[0])+"'"
        res1= c.selectall(qry1)
        cnt=0
        for ii in res1:
            if ii[0] in vegs:
                cnt=cnt+1
        recpid.append(i[0])
        recpcnt.append(cnt)

    for i in range(len(recpid)):
        for k in range(len(recpid)):
            if recpcnt[i] > recpcnt[k]:
                tempcnt= recpcnt[i]
                recpcnt[i]= recpcnt[k]
                recpcnt[k]= tempcnt
                tem = recpid[i]
                recpid[i] = recpid[k]
                recpid[k] = tem

    print("result")
    print(recpid)
    print(recpcnt)

    jsondata=[]
    for i in range(len(recpid)):
        qry="select * from tbl_recipe where `reci_id`='"+str(recpid[i])+"'"
        resd=c.selectone(qry)
        if resd is not None:
            reci_id= resd[0]
            name=resd[1]
            description=resd[2]
            how_to_make=resd[3]
            type=resd[4]
            author_id=resd[5]
            photo=resd[6]
            status=resd[7]

            s={ "reci_id" : reci_id , "name":name, "description":description,"how_to_make":how_to_make,"type":type,"photo":photo  }
            if recpcnt[i]> 0:
                jsondata.append(s)

    print(jsondata)

    return jsonify(status="ok",data=jsondata)


    return jsonify(status="ok")


@app.route('/andridaddrecipee',methods=["POST"])
def andrpostrecp():
    uid=request.form["uid"]
    name=request.form["name"]
    howto=request.form["howto"]
    desc=request.form["desc"]
    img=request.form["img"]

    a = base64.b64decode(img)

    date = str(datetime.datetime.now()).replace(" ", "_").replace(":", "_").replace("-", "_")

    fh = open("E:\\project\\recipe_py\\recipe\\static\\recipe\\" + date + ".jpg", "wb")
    fh.write(a)
    fh.close()

    path = "/static/recipe/" + date + ".jpg"

    j = "select max(reci_id) from tbl_recipe"
    obj = conn()
    r = obj.mid(j)
    i = "insert into tbl_recipe(reci_id,name,description,how_to_make,type,author_id,photo,status)values('" + str(r) + "','" + name + "','" + desc + "','" + howto + "','user','"+uid+"','" + path + "','pending')"
    obj.nonreturn(i)

    return jsonify(status="ok",data=r)


@app.route('/andviewingredientsnotincludedbyrecpid',methods=["POST"])
def andviewingredientsnotincludedbyrecpid():
    recpid=request.form["recpid"]

    qry="SELECT * FROM `tbl_vegetables` WHERE `veg_id` NOT IN (SELECT `veg_id` FROM `tbl_ingredients` WHERE `reci_id`='"+recpid+"')"

    c=conn()
    res=c.jsonselectall(qry)

    return jsonify(status="ok",data=res)


@app.route('/andviewingredientsincludedbyrecpid', methods=["POST"])
def andviewingredientsincludedbyrecpid():
    recpid = request.form["rid"]

    qry = "SELECT * FROM `tbl_vegetables` WHERE `veg_id`  IN (SELECT `veg_id` FROM `tbl_ingredients` WHERE `reci_id`='" + recpid + "')"

    c = conn()
    res = c.jsonselectall(qry)

    return jsonify(status="ok", data=res)

@app.route('/andaddingredient',methods=["POST"])
def andaddingredient():
    recpid=request.form["rid"]
    vegid=request.form["vid"]

    c=conn()

    qry="INSERT INTO  `tbl_ingredients` (`reci_id`,`veg_id`)  VALUES ('"+recpid+"','"+vegid+"')"

    c.nonreturn(qry)

    return jsonify(status="ok")



@app.route('/adminviewstores')
def adminviewstores():
    c=conn()

    qry="select * from store where status='pending'"
    respend=c.selectall(qry)

    qry = "select * from store where status='approved'"
    resdone = c.selectall(qry)

    return render_template('adm_viewpendingstores.html',respend=respend,resdone=resdone)


@app.route('/approvestore/<sid>')
def approvestore(sid):
    c=conn()
    c.nonreturn("update store set status='approved' where storeid='"+sid+"'")
    return "<script>alert('Store Approved Successfully');window.location='/adminviewstores'</script>"

@app.route('/rejstore/<sid>')
def rejstore(sid):
    c=conn()
    c.nonreturn("update store set status='rejected' where storeid='"+sid+"'")
    return "<script>alert('Store Approved Successfully');window.location='/adminviewstores'</script>"


@app.route('/storeaddveg')
def storeaddveg():

    c=conn()
    qry="select * from tbl_vegetables where veg_id not in (select vegid from storevegitems where slogid='"+str(session["lgid"])+"')"
    res=c.selectall(qry)




    return render_template('Store/additems.html',res=res)

@app.route('/storeviewveg')
def storeviewveg():
    c=conn()
    qry="select tbl_vegetables.* ,storevegitems.*from tbl_vegetables inner join storevegitems on storevegitems.vegid=tbl_vegetables.veg_id where slogid='"+str(session["lgid"])+"'"
    res=c.selectall(qry)
    return render_template('Store/store_view_veg.html',data=res)


@app.route('/dels/<id>')
def dels(id):
    c=conn()
    qry="delete from storevegitems where svid='"+id+"'"
    c.nonreturn(qry)

    return "<Script>alert('Deleted Successfully');window.location='/storeviewveg'</script>"


@app.route('/storeaddveg_post',methods=['post'])
def storeaddveg_post():

    c=conn()
    id=request.form["select"]
    price=request.form["textfield"]

    c.nonreturn("insert into storevegitems (slogid,vegid,price) values ('"+str(session["lgid"])+"','"+id+"','"+price+"')")

    return "<script>alert('Added Successfully');window.location='/storeaddveg'</script>"


@app.route('/viewprofile')
def viewprofile():
    c=conn()
    q="select * from store where logid='"+str(session["lgid"])+"'"
    print(q)
    res=c.selectone(q)
    return render_template('/Store/viewprofile.html',data=res)



@app.route('/storesignup')
def storesignup():
    return render_template('Store/signup.html')
@app.route('/storesignuppost',methods=['post'])
def storesignuppost():
    name=request.form['textfield']
    place=request.form['textfield2']
    post=request.form['textfield3']
    pin=request.form['textfield4']
    lat=request.form['textfield5']
    longi=request.form['textfield6']
    email=request.form['textfield7']
    contact=request.form['textfield8']
    pswd=request.form['textfield9']

    c=conn()





    qry="insert into tbl_login(uname,password,type) values ('"+email+"','"+pswd+"','store')"
    id=c.nonreturn(qry)

    qry="insert into store(name,latitude,longitude,post,pin,email,phone,logid,status) values ('"+name+"','"+lat+"','"+longi+"','"+post+"','"+pin+"','"+email+"','"+contact+"','"+str(id)+"','pending')"
    c.nonreturn(qry)

    return "<script>alert('Account created successfully');window.location='/'</script>"








    return render_template('Store/signup.html')


@app.route('/user_signup')
def user_signup():
    return render_template('user/user_signup.html')


@app.route('/usersignuppost',methods=['post'])
def usersignuppost():
    name=request.form['textfield']
    house_nm=request.form['textfield2']
    street=request.form['textfield3']
    dis=request.form['textfield4']
    pin=request.form['textfield5']
    gender=request.form['gender']
    email=request.form['mail']
    contact=request.form['textfield7']
    pswd=request.form['textfield9']

    c=conn()
    qry="insert into tbl_login(uname,password,type) values ('"+email+"','"+pswd+"','user')"
    id=c.nonreturn(qry)

    qry="insert into tbl_user(name,house_nm,street,district,pin,gender,phone_no,email) values ('"+name+"','"+house_nm+"','"+street+"','"+dis+"','"+pin+"','"+gender+"','"+contact+"','"+email+"')"
    c.nonreturn(qry)
    return "<script>alert('Account created successfully');window.location='/'</script>"
    return render_template('user/user_signup.html')



@app.route('/user_viewprofile')
def user_viewprofile():
    c=conn()
    q="select * from tbl_user where email='"+str(session["emid"])+"'"
    print(q)
    res=c.selectone(q)
    print(res)
    return render_template('/user/user_profile.html',data=res)













@app.route('/user_addrecipe')
def user_addrecipe():
    return render_template("user_add_recipe.html")

# @app.route('/user_adrecipe_post',methods=["post"])
# def user_adrecipe_post():
#     rimage = request.files["file_rimage"]
#
#     rname = request.form["txt_rname"]
#     session["name"]=rname
#
#     descript=request.form["txta_description"]
#     session["des"]=descript
#
#     make=request.form["txta_make"]
#     session["making"]=make
#
#     date=str(datetime.datetime.now()).replace(" ","_").replace(":","_").replace("-","_")
#     rimage.save("E:\\project\\recipe_py\\recipe\\static\\recipe\\"+date+".jpg")
#     path="/static/recipe/"+date+".jpg"
#     session["image"] = path
#
#     j="select max(reci_id) from tbl_recipe"
#     obj = conn()
#     r=obj.mid(j)
#     i="insert into tbl_recipe(reci_id,name,description,how_to_make,type,author_id,photo,status)values('"+str(r)+"','" + rname + "','" + descript + "','"+make+"','admin','0','"+path+"','approved')"
#     obj.nonreturn(i)
#     session['rid']=r
#
#     return





if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)

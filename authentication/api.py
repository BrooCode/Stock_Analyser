from unittest import result
from fastapi import FastAPI, Request,Form
import new_user as user
import credentials as cred
import update as update
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates/")



@app.get("/add_user")
async def form_post(request: Request):
    result = "add_users"
    return templates.TemplateResponse('signup.html', context={'request': request, 'result': result}) 

# {
#     "user_name":"",
#     "name":"",
#     "password":"",
#     "mobile_num":""
# }

@app.post("/add_user")
async def form_post(request: Request,uname:str=Form(...),password:str=Form(...),name:str=Form(...),number:str=Form(...)):
    # req_info = await request.json()
    result = user.add_user(uname,name,password,number)
    return templates.TemplateResponse('signup.html', context={'request': request, 'result': result}) 


# {
#     "user_name":"",
#     "password":""
# }


@app.get("/user_login")
async def form_post(request: Request):
    result = "Login Credentials"
    return templates.TemplateResponse('login.html', context={'request': request, 'result': result}) 

@app.post("/user_login")
async def form_post(request: Request,uname:str=Form(...),password:str=Form(...)):
    # req_info = await request.json()
    # uname = req_info['user_name']
    # password = req_info['password']
    print("dfbsui")
    result = cred.login(uname,password)
    return result
    # return templates.TemplateResponse('login.html', context={'request': request, 'result': result}) 


@app.post("/update_cred")
async def form_post(request: Request):
    req_info = await request.json()
    uname = req_info['user_name']
    password = req_info['password']
    result = update.change_password(uname,password)
    return result

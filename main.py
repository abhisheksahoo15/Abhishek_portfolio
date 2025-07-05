from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# ✅ Mount static folder for CSS, JS, images, etc.
app.mount("/static", StaticFiles(directory="static"), name="static")

# ✅ HTML Templates Directory
templates = Jinja2Templates(directory="templates")

# ✅ Home Page Route
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("webpages/index.html", {
        "request": request,
        "title": "GetSetAI"
    })

# ✅ Certification Page Route
@app.get("/certificate", response_class=HTMLResponse)
async def certification(request: Request):
    return templates.TemplateResponse("webpages/certification.html", {
        "request": request,
        "title": "Certification"
    })

# ✅ Projects Page Route
@app.get("/projects", response_class=HTMLResponse)
async def projects(request: Request):
    project_list = [
        {
            "name": "Ai Resume Builder and Job Finder -HireFire AI ",
            "stack": "Python (FastAPI, HTML2PDF, Web Scraping, API Integration),Cloud Technology, HTML, CSS, JavaScript",
            "description": "A Complete End to End AI Resume Builder and Job Finder Platform. based on the Webscraping , API integration cloud Technology and lot more.",
            "link": "https://hirefireai.cloud"
        },
        {
            "name": "Student Marks Prediction ML Model",
            "stack": "Python (Pandas, Scikit-learn, Streamlit,matplotlib, seaborn)",
            "description": "A Complete end to end machine Learning Model which is trained over existing data and predict the new score - Supervised Machine learning."
        },
        # {
        #     "name": "GetSetAI Invoice Generator",
        #     "stack": "HTML2PDF, FastAPI",
        #     "description": "Automated invoice generation system for students using FastAPI backend."
        # }
    ]

    return templates.TemplateResponse("webpages/projects.html", {
        "request": request,
        "title": "Projects",
        "projects": project_list
    })



# ✅ Certification Page Route
@app.get("/contact", response_class=HTMLResponse)
async def certification(request: Request):
    return templates.TemplateResponse("webpages/contact.html", {
        "request": request,
        "title": "Certification"
    })
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
            "name": "Tourism Website",
            "stack": "Django, HTML/CSS, SQLite",
            "description": "A full-stack website to explore Indian destinations and manage tour bookings."
        },
        {
            "name": "Supermarket Data Analysis",
            "stack": "Python (Pandas, SQL, Power BI)",
            "description": "Analyzed 100k+ entries across 20+ metrics to create dynamic dashboards."
        },
        {
            "name": "GetSetAI Invoice Generator",
            "stack": "HTML2PDF, FastAPI",
            "description": "Automated invoice generation system for students using FastAPI backend."
        }
    ]

    return templates.TemplateResponse("webpages/projects.html", {
        "request": request,
        "title": "Projects",
        "projects": project_list
    })

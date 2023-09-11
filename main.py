from fastapi import FastAPI, status
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Profile(BaseModel):
    slack_name: str
    current_day: str
    utc_time: str
    track: str
    github_file_url: str
    github_repo_url: str
    status_code: int


@app.get("/api")
async def profile(slack_name: str = "Fortune_Mina", track: str = "backend"):
    
    current_utc_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    day = datetime.now().strftime("%A")
    file_url = "https://github.com/tonye0/HNGx/blob/master/main.py"
    repo_url = "https://github.com/tonye0/HNGx/tree/master.git"
    
    user_profile = Profile(
        slack_name = slack_name,
        current_day = day,
        utc_time = current_utc_time,
        track = track,
        github_file_url = file_url,
        github_repo_url = repo_url,
        status_code = 200,
    )
    
    return user_profile.dict()
    

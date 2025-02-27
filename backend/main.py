from fastapi import FastAPI
import psutil
import time
import datetime

# Krijimi i aplikacionit FastAPI
app = FastAPI()

# Ruajtja e kohës së nisjes së serverit për llogaritjen e uptime
start_time = time.time()

@app.get("/")
def home():
    return {"message": "Ultra Thinking Web API është online!"}

@app.get("/status")
def get_status():
    return {"status": "online", "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

@app.get("/metrics")
def get_metrics():
    return {
        "cpu_usage": f"{psutil.cpu_percent()}%",
        "memory_usage": f"{psutil.virtual_memory().percent}%",
        "disk_usage": f"{psutil.disk_usage('/').percent}%",
        "num_processes": len(psutil.pids())
    }

@app.get("/logs")
def get_logs():
    return {"logs": ["Log 1", "Log 2", "Log 3"]}

@app.get("/uptime")
def get_uptime():
    uptime_seconds = time.time() - start_time
    uptime_str = str(datetime.timedelta(seconds=int(uptime_seconds)))
    return {"uptime": uptime_str}
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)






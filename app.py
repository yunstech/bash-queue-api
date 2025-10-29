from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from redis import Redis
from rq import Queue
from tasks import run_bash_script

app = FastAPI(title="Bash Runner API")

# Connect Redis
redis_conn = Redis(host="localhost", port=6379)
queue = Queue("bash_queue", connection=redis_conn)

class BashRequest(BaseModel):
    file_path: str

@app.post("/run")
def run_command(req: BashRequest):
    """Queue a bash script execution."""
    job = queue.enqueue(run_bash_script, req.file_path)
    return {
        "job_id": job.id,
        "status": "queued",
        "file_path": req.file_path,
    }

@app.get("/status/{job_id}")
def get_status(job_id: str):
    """Check job status."""
    from rq.job import Job
    try:
        job = Job.fetch(job_id, connection=redis_conn)
        return {
            "job_id": job.id,
            "status": job.get_status(),
            "result": job.result,
        }
    except Exception as e:
        return {"error": str(e)}

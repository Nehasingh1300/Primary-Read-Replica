from fastapi import FastAPI, HTTPException
from app.terraform_generator import generate_terraform
from app.ansible_generator import generate_ansible
from app.executor import run_terraform, run_ansible

app = FastAPI()

@app.post("/generate-configs/")
def generate_configs(postgres_version: str, instance_type: str, num_replicas: int, max_connections: int, shared_buffers: str):
    try:
        generate_terraform(postgres_version, instance_type, num_replicas)
        generate_ansible(max_connections, shared_buffers)
        return {"message": "Configurations generated successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/apply-infrastructure/")
def apply_infrastructure():
    try:
        run_terraform()
        return {"message": "Infrastructure provisioned successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/configure-postgresql/")
def configure_postgresql():
    try:
        run_ansible()
        return {"message": "PostgreSQL configured successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

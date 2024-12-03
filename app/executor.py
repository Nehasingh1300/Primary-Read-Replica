import subprocess

def run_terraform():
    subprocess.run(["terraform", "init"], cwd="terraform/", check=True)
    subprocess.run(["terraform", "apply", "-auto-approve"], cwd="terraform/", check=True)

def run_ansible():
    subprocess.run(["ansible-playbook", "playbook.yml"], cwd="ansible/", check=True)

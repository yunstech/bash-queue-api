import subprocess

def run_bash_script(param1: str, param2: str):
    """Execute a bash script with parameters."""
    script_path = "./bash-script/run_me.sh"

    try:
        result = subprocess.run(
            [script_path, param1, param2],
            capture_output=True,
            text=True,
            check=True
        )
        return {
            "status": "success",
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "error",
            "stdout": e.stdout,
            "stderr": e.stderr,
            "returncode": e.returncode,
        }

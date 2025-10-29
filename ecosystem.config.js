module.exports = {
  apps: [
    {
      name: "bash-runner-api",
      cwd: "{path}/bash-queue-api",
      script: "./venv/bin/python3",
      args: "-m uvicorn app:app --host 0.0.0.0 --port 8668",
      watch: false,
      env: {
        REDIS_HOST: "localhost",
        REDIS_PORT: "6379"
      }
    },
    {
      name: "bash-runner-worker",
      cwd: "{path}/bash-queue-api",
      script: "./venv/bin/python3",
      args: "worker.py",
      watch: false,
      env: {
        REDIS_HOST: "localhost",
        REDIS_PORT: "6379"
      }
    }
  ]
};
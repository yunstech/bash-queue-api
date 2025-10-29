module.exports = {
  apps: [
    {
      name: "bash-runner-api",
      script: "uvicorn",
      args: "app:app --host 0.0.0.0 --port 8000",
      interpreter: "python3",
      watch: false,
      env: {
        REDIS_HOST: "localhost",
        REDIS_PORT: "6379"
      }
    },
    {
      name: "bash-runner-worker",
      script: "worker.py",
      interpreter: "python3",
      watch: false,
      env: {
        REDIS_HOST: "localhost",
        REDIS_PORT: "6379"
      }
    }
  ]
};

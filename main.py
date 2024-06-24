import subprocess
import time

if __name__ == "__main__":
    print('Running the script:::')
    server_process = subprocess.Popen(["prefect", "server", "start"])
    time.sleep(10)
    deployment_process = subprocess.run(["python3",
                                         "deployments/rick_morty_deployments"
                                         ".py"])
    server_process.wait()


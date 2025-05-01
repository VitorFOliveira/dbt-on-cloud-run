import asyncio

from google.cloud import run_v2


def run_job_sync(project_id, location, job_id, override_args):
    """
    Runs a job. Sync, waits for the whole cloud run job execution to complete
    """
    print(f"Begining sincronous execution of job {job_id}")
    
    # Create a client
    client = run_v2.JobsClient()

    # Initialize request argument(s)
    request = run_v2.RunJobRequest(
        name=f"projects/{project_id}/locations/{location}/jobs/{job_id}",
        overrides=run_v2.types.RunJobRequest.Overrides(
            container_overrides=[
                run_v2.types.RunJobRequest.Overrides.ContainerOverride(
                    args=override_args
                )
            ]
        )
    )

    # Make the request
    operation = client.run_job(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

    print(f"End of Sincrous execution of job {job_id}")


async def run_job_async(project_id, location, job_id, override_args):
    """
    Run a job asynchronously.
    """
    print(f"Begining assincronous execution of job {job_id}")

    # Create a client
    client = run_v2.JobsAsyncClient()

    # Initialize request argument(s)
    request = run_v2.RunJobRequest(
        name=f"projects/{project_id}/locations/{location}/jobs/{job_id}",
        overrides=run_v2.types.RunJobRequest.Overrides(
            container_overrides=[
                run_v2.types.RunJobRequest.Overrides.ContainerOverride(
                    args=override_args
                )
            ]
        )
    )

    # Make the request
    operation = client.run_job(request=request)

    print("Waiting for operation to complete...")

    response = (await operation).result()

    # Handle the response
    print(response)

    print(f"End of Assincrous execution of job {job_id}")

# Example usage
project_id = "projeto-academia-portfolio"
location = "us-east1"
job_id = "dbt-cloud-run-job-demo"

# override to do dbt debug
override_args = ["poetry", "run", "dbt", "debug", "--target", "dev"]

# Sync submission
run_job_sync(project_id, location, job_id, override_args=override_args)

# Async submission
override_args = ["poetry", "run", "dbt", "run", "--full-refresh", "--target", "dev"]
asyncio.run(run_job_async(project_id, location, job_id, override_args))

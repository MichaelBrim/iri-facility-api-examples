# Genesis Mission Hackathon

The DOE IRI APIs allow you to programmatically execute jobs on HPC systems, trigger filesystem operations, and view your current allocations. This demo focuses on the execution of simple jobs to demonstrate the overall capabilities.

## 1. Environment

In your environment of choice, install the dependencies for the exercises:
```
pip install -r requirements.txt
```

Create a `.env` file and add your configuration
```bash
# ----------------------------------
# ------ API URL (choose one) ------
# ----------------------------------

#BASE_URL=https://api.alcf.anl.gov/api/v1
#BASE_URL=https://api.iri.nersc.gov/api/v2
#BASE_URL=https://iri-dev.ppg.es.net


# ----------------------------
# ------ Authentication ------
# ----------------------------

IRI_API_TOKEN=""


# ----------------------------
# ------ Job Submission ------
# ----------------------------

NODES=1
WALLTIME_SEC=300
QUEUE=""
COMPUTE_ALLOCATION=""
STDOUT_PATH=""
STDERR_PATH=""
COMPUTE_RESOURCE_ID=""
```

Create a `.env.secret` file to store your IRI API token:
```bash
IRI_API_TOKEN=""
```


## 2. Authentication

### ALCF (with Globus Auth)

Install the ALCF token manager package:
```bash
pip install alcf-tokens
```

Authenticate **with your ALCF credentials**:
```bash
alcf-tokens login iri
```
The above command will print a URL that you must copy-paste to your browser. Follow the authentication flow, and copy-paste the resulting authorization code back to your terminal.

Test your ALCF IRI access token:
```bash
alcf-tokens test-token iri
```
If your token is valid and ready to use with the IRI API, you should see:
```json
{
    "ready": true, 
    "error": null
}
```

If you get an error, logout from Globus by visiting [https://app.globus.org/logout](https://app.globus.org/logout), open a new **incognito browser**, and restart the login command.

### NERSC 

... in construction ...

### OLCF

... in construction ...

# ESnet

... in construction ...

## 3. Main Exercises

### 3.a. View Resources and their Status

Execute the following script to view the metadata of ALCF resources:
```bash
python 01_get_resources.py
```
You can filter the list by adding the resource name as an argument.

For each resource, `current_status` reports whether the resource is *up* and ready to use, and `id` uniquely identifies the resource. To query a specific resource from its ID without going through a list, execute the following:

```bash
python 02_get_resource.py <your-target-id>
```

### 3.b. Submit Jobs

Look into `03_submit_job.py` and modify the `STDOUT_PATH` and `STDERR_PATH` paths to **include your ALCF username**. Then, execute the script to submit a job to Polaris (`RESOURCE_ID=55c1c993-1124-47f9-b823-514ba3849a9a`):
```bash
python 03_submit_job.py
```

If successful, the above command should return the PBS job ID (**keep this ID for the following steps**).
```json
{
  "id": "<your-job-id>",
  "status": {
    "state": "queued",
    "exit_code": 0
  }
}
```

The job will execute the content of the `COMMANDS` field defined in the python script. If you kept the default content, the job will run on 1 node and write your username and the compute node hostname in the `STDOUT_PATH` file (see `.env`).

Execute the following to query the state of your job:
```bash
python 04_get_job_state.py <your-job-id>
```

Once your job is `completed` or `failed`, continue to the next section.

### 3.c. View Job Results

You can view the result of your jobs with Filesystem operations. If your PBS job completed, execute the following:
```bash
python 05_view_file.py <your-absolute-path-to-your-stdout-file>
```

If your PBS job failed, execute the following:
```bash
python 05_view_file.py <your-absolute-path-to-your-stderr-file>
```

All filesystem operations are asynchronous, meaning you will always get back a `task_id` when using the Filesystem component. The `05_view_file.py` script automatically checks the status of your task in a loop until it is completed. 


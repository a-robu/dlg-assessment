
# Introduction

This repository holds Andrei's solution to DLG's software engineer assessment. The original problem description is available [further below](#original-problem-description).

# Running from Source

To serve the API endpoint from source, run the following commands to setup a _venv_ and run in source-reloading mode.

```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python -m bottle main --reload
```

A development server is now running. It is possible to preview the API response in a web browser at http://localhost:8080/total or by running the following command.

```bash
curl http://localhost:8080/total
```

# Original Problem Description

## Software Engineer Python Test

Create a REST endpoint that return the sum of a list of numbers e.g. `[1, 2, 3] => 1 + 2 + 3 = 6`. You are free to use any Python 3 framework, however, try and keep the usage of the third-party library to a minimum.

The list of numbers is expected to arrive from a backend service and for this test you can hard code the list using the following line.

```python
numbers_to_add = list(range(10000001))
```

The url of the endpoint and the sample response is as follows:

Request: http://localhost:5000/total

Response:

```json
{
    "total": 6
}
```

Please provide the source code, tests, documentationsand any assumptionsyou have made.

Note: We are looking for the candidate’s “Software Engineering”ability not just the Python programming skills.

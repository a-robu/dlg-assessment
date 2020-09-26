
# Introduction

This repository holds Andrei's solution to DLG's software engineer assessment. The original problem description is available [further below](#original-problem-description).

# Running from Source

To serve the API endpoint from source, run the following commands to setup a _venv_ and run in source-reloading mode.

```bash
python3 -m venv venv
. venv/bin/activate
pip install wheel
pip install -r requirements.txt -r requirements-dev.txt
python -m bottle main --reload
```

A development server is now running. It is possible to preview the API response in a web browser at http://localhost:8080/total or by running the following command.

```bash
curl http://localhost:8080/total
```

# Running the Tests

This project does not have many unit tests (because there is not much complex logic to test). Still, some assumptions are validated in automated tests. Enter the virtual environment and run _pytest_ to run the tests.

```bash
python3 -m venv venv
pytest
```

# Software Dependencies

This solution makes use of `bottle.py`, a minimalistic web framework to serve the API response. This framework is not as feature rich as others, but it _serves_ just fine for a smaller project. The documentation is available at http://bottlepy.org/docs/0.12/.

I chose to use the _Pytest_ testing framework because I like [the simplicity of assertions in pytest](https://docs.pytest.org/en/stable/assert.html).

# Assumptions & Limitations

This solution is a toy example of how a software project can work. Typically I find that my dependencies can become a bit more complex (such as needing software that can be conveniently installed with a distro's package manager) and I tend to then Docker-ize my projects. Here, that is not necessary as the dependencies are very simple and the software is still easy to run.

APIs often need to rate-limit clients, to ensure unintrerupted service. One reason why I have not implemented rate limiting in this solution is that, with caching, this API does not require a large amount of compute time to serve its response.

No way to execute the code in production is provided, although it would be trivial to, for example, [run this on Google AppEngine](https://github.com/GoogleCloudPlatform/appengine-bottle-skeleton/blob/master/app.yaml).

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

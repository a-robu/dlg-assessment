
# Introduction

This repository holds Andrei's solution to DLG's software engineer assessment. A copy of the original problem description is included [further below at the end of this README](#original-problem-description).

# Setting Up

Run the following commands to setup a _venv_ with the necessary dependencies.

```bash
python3 -m venv venv
. venv/bin/activate
pip install wheel
pip install -r requirements.txt -r requirements-dev.txt
```

# Running from Source

Run the following commands to enter the _venv_ and use _Bottle_ to serve the API endpoint in source-reloading mode.

```bash
. venv/bin/activate
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

Note that this command would be very comfortable inside the testing stage of a CI pipeline.

# Software Dependencies

This solution uses _Bottle_, a minimalistic web framework, to serve the API response. Bottle is not as feature rich as other frameworks, but it can serve a smaller project just fine. The documentation is available at http://bottlepy.org/docs/0.12/.

I chose to use the _Pytest_ testing framework because I like [the simplicity of assertions in pytest](https://docs.pytest.org/en/stable/assert.html).

The automated tests use _Boddle_ to verify teh _Bottle_ responses. I chose _Boddle_ because [this comment recommented it](https://stackoverflow.com/a/41270185) and because the source code of this small library does not seem malicious on first glance.

# Assumptions & Limitations

This solution is a toy example of how a software project can work.

Typically I find that in most projects, the management of dependencies can become more complex (such as when needing software that can be conveniently installed with a distro's package manager) and so, in time, I tend to containerize projects as they grow. Here, it was not necessary to containerize the code because dependencies are very simple and the software is still easy to run.

For very large datasets, it may be necessary to distribute the summation operaton across multiple workers. This distribuited computation is not implemented in this project.

APIs often need to rate-limit clients, to ensure unintrerupted service. One reason why I have not implemented rate limiting in this solution is that, with caching, this API does not require a large amount of compute time to serve its response.

No way to execute the code in production is provided, although it would be trivial to, for example, [run this on Google AppEngine](https://github.com/GoogleCloudPlatform/appengine-bottle-skeleton).

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

Note: We are looking for the candidate’s “Software Engineering” ability not just the Python programming skills.

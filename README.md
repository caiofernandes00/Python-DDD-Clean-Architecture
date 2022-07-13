# Clean Architecture and Domain Driven Design with Python

### Summary

Application for implementing clean architecture and domain driven design with Python. Just it, there is no other
purpose. I didn't make 100% of test coverage, but all the tests are passing.

### Execute the following command to install the dependencies:

```bash
pythom -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install "fastapi[all]"

# To execute the server to test the API
uvicorn src.infrastructure.api.server:app --reload
# To execute the tests
pytest
```

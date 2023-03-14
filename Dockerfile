FROM python:3.11.0 as test-project
COPY . /test-project
WORKDIR /test-project
RUN pip install pipenv
RUN pipenv install
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get -y install google-chrome-stable
RUN pipenv run python -m unittest api_tests.api_test_ip

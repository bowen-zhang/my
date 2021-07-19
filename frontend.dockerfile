FROM python:3
RUN /usr/local/bin/python -m pip install --upgrade pip
WORKDIR /deployed
ADD ./third_party/ third_party/
WORKDIR /deployed/third_party/intel
RUN make init
WORKDIR /deployed
ADD ./src/requirements.txt src/
RUN pip3 install -r src/requirements.txt --user
ADD ./src/ src/
ENV PYTHONPATH=/deployed/src:/deployed/third_party
ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python3
CMD ["python3", "frontend/main.py", "--log_to_file"]
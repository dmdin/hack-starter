FROM python:3.8-slim
ENV IS_PROD=true
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
WORKDIR backend/
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

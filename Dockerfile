FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY memory_usage_script.py .
CMD [ "python", "-u","memory_usage_script.py" ]
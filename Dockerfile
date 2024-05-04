FROM python:3.10.14

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","-u","app.py"]
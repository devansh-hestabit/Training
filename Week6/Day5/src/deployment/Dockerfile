FROM python:3.12.3-slim


WORKDIR /app

COPY requirements.prod.txt .

#only used required dependencies for production to keep the image size small
RUN pip install --no-cache-dir -r requirements.prod.txt 

COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.deployment.api:app", "--host", "0.0.0.0", "--port", "8000"]

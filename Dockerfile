FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "dom_u_morya.wsgi:application", "--bind", "0.0.0.0:8000"]

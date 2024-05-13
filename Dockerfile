FROM python:3.11

WORKDIR /a3_tech_test

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 90

CMD ["uvicorn", "a3_tech_test.app.main:app", "--reload", "--host", "0.0.0.0", "--port", "90", "--log-level", "info"]

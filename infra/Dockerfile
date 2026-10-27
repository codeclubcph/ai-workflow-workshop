# Container image for the orders API.
# Exercise 03 (Infra/DevOps): this image does not build/run correctly and
# breaks several best practices. Fix it with AI help - then review the fix!
FROM python:latest

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]

FROM python:3.12-alpine3.22

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app/

EXPOSE 12345

RUN chmod +x /app/scripts/comands.sh && \
pip install --no-cache-dir -r /app/requirements.txt

CMD ["sh", "/app/scripts/comands.sh"]
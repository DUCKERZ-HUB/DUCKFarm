FROM python:3.9-slim

ENV PYTHONPATH=/app:${PYTHONPATH}

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./docker/server/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r$//' /entrypoint.sh && chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]

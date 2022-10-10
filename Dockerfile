FROM python:3.8-slim as builder
COPY . /src
RUN pip install --user flask

FROM python:3.8-slim as app
COPY --from=builder /root/.local /root/.local
COPY --from=builder /src .

ENV PATH=/root/.local:$PATH
EXPOSE 8080

CMD ["python3", "app.py"]
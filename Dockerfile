FROM python:3.13.5-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --no-cache gcc musl-dev linux-headers \
    libffi-dev openssl-dev jpeg-dev zlib-dev python3-dev \
    mariadb-connector-c-dev build-base \
    musl-dev \
    gcc \
    python3-dev \
    libffi-dev \
    cairo-dev \
    pango-dev \
    gdk-pixbuf-dev \
    libxml2-dev \
    libxslt-dev \
    libjpeg-turbo-dev \
    zlib-dev \
    harfbuzz-dev \
    fontconfig \
    ttf-dejavu

WORKDIR /app

# Install uv (choose approach based on availability)
RUN pip install uv

COPY pyproject.toml uv.lock ./
RUN uv venv
RUN uv pip install -r pyproject.toml
# RUN uv add uvicorn
COPY . /app

RUN find /app/.venv/lib/ -type f -name "*.py" \
    -exec sed -i 's/from django\.utils\.encoding import smart_text/from django.utils.encoding import smart_str as smart_text/g' {} +

RUN find /app/.venv/lib/ -type f -name "*.py" \
    -exec sed -i -E "s/(=\s*)\"([^\"]*\\\.[^\"]*)\"/\1r\"\2\"/g" {} +


CMD ["uv", "run", "gunicorn", "TRM.wsgi:application", "--bind", "0.0.0.0:8000"]

FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /repo
WORKDIR /repo

ARG APP_VERSION
ARG GIT_REPO_URL
RUN git clone --depth 1 --branch ${APP_VERSION} ${GIT_REPO_URL} /repo

ADD ./app/.env /repo/app

WORKDIR /repo/app

RUN pip install -Ur requirements.txt

EXPOSE 8000

CMD ["python", "app.py", "0.0.0.0", "debug=True", "port=8000" ]
#CMD [ "gunicorn", "wsgi:app", "-w", "6", "--bind", "0.0.0.0:8000" ]
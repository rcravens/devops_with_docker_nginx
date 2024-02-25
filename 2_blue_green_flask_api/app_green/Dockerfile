FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /app_blue
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -Ur requirements.txt
ADD . /app/

EXPOSE 8000
CMD ["python", "app.py", "0.0.0.0", "debug=True", "port=8000" ]
#CMD [ "gunicorn", "wsgi:app_blue", "-w", "6", "--bind", "0.0.0.0:8000" ]
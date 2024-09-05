FROM python:3.12.2-bullseye
 
 
WORKDIR /app
 
 
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
 
 
COPY . /app/
 
 
RUN python manage.py makemigrations && \
    python manage.py migrate 
    
CMD python manage.py runserver 0.0.0.0:8000
 
 
EXPOSE 8000
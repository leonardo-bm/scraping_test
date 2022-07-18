FROM python:latest
WORKDIR /opt
COPY . ./

COPY scraping/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD python main.py
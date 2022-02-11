FROM ubuntu

RUN apt-get update && apt-get install && apt-get install wget -y
RUN apt install firefox -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip

RUN pip3 install selenium
RUN pip3 install beautifulsoup4

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz
RUN tar -xvzf geckodriver-v0.30.0-linux64.tar.gz
RUN mv geckodriver /usr/local/bin
RUN cd /usr/local/bin && chmod +x geckodriver; cd

COPY . .

ENTRYPOINT [ "python3", "Scrape.py" ]
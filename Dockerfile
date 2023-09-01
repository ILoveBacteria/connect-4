FROM ubuntu

WORKDIR /usr/src/app
COPY . .

RUN apt update
RUN yes | apt install curl
RUN yes | apt install "python3.10"
RUN yes | apt install npm

RUN curl -L https://bootstrap.pypa.io/get-pip.py > get-pip.py
RUN python3 get-pip.py

RUN pip install pipenv
RUN pipenv install
RUN npm install

RUN npm run build

EXPOSE 5000

CMD [ "pipenv", "run", "python", "main.py" ]

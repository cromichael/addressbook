FROM python:3.6
WORKDIR /app
COPY data /app/data
ADD *.py /app/
ADD config.yaml /app/
ADD requirements.txt /app/
RUN pip install -r /app/requirements.txt
ENTRYPOINT ["python", "address_book.py"]
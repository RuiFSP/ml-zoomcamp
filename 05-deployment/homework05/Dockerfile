FROM svizor/zoomcamp-model:3.11.5-slim

# Install pipenv
RUN pip install pipenv

# Create a directory and set it as the working directory
WORKDIR /app

# Install all the dependencies form the Pipenv file
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predict.py", "model1.bin", "dv.bin", "./"]

EXPOSE 9696

# Run it with Gunicorn
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]
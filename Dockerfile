FROM python:3.7-slim-buster

# set argument vars in docker-run command
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_DEFAULT_REGION

ENV AWS_ACCESS_KEY_ID $AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY $AWS_SECRET_ACCESS_KEY
ENV AWS_DEFAULT_REGION $AWS_DEFAULT_REGION

# copy in files
COPY . /app

# install streamlit
WORKDIR /app
RUN pip install streamlit
EXPOSE 8501

# run app
ENTRYPOINT ["streamlit","run"]
CMD ["app.py"]

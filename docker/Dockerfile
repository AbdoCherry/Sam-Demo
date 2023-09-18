##############################
#### Multistage - Stage I ####
##############################

# Base Image from public gallery of AWS ECR - Lambda Function - Python
FROM public.ecr.aws/lambda/python:3.11 AS builder

# Installing build dependencies for psutil (pyproject.toml)
RUN yum install -y gcc python3-devel gcc-c++

# Copying our requirements.txt for the necessary python modules
COPY requirements.txt .

# Installing our necessary modules at the var/tasks/
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt -t /tmp/python-deps

# Removing unnecessary dependencies (optional, but recommended)
RUN yum remove -y gcc python3-devel gcc-c++ && \
    yum clean all

##############################
#### Multistage - Stage II ####
##############################

# Base Image from public gallery of AWS ECR - Lambda Function - Python
FROM public.ecr.aws/lambda/python:3.11 AS final

# Copying the python dependencies from build stage 
COPY --from=builder /tmp/python-deps ${LAMBDA_TASK_ROOT}
COPY src ${LAMBDA_TASK_ROOT}

ARG ENV
ENV ENVIRNMENT=${ENV}
# Defining our entrypoint
CMD [ "app.lambda_handler" ]
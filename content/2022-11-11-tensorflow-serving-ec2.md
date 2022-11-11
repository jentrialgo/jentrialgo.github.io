Title: Installing Tensorflow Serving in Amazon EC2 Linux
Date: 2022-11-11 18:00
Category: tensorflow, ec2
Tags: tensorflow

How to install and test Tensorflow Serving in a Amazon EC2 instance running
Amazon EC2 Linux 2. We will use docker and we will serve a resnet image. These
are the commands:

    # Install docker
    sudo yum update
    sudo yum install docker
    sudo usermod -a -G docker ec2-user
    newgrp docker
    sudo systemctl enable docker.service
    sudo systemctl start docker.service

    # Prepare the resnet model
    rm -rf /tmp/resnet
    wget https://tfhub.dev/tensorflow/resnet_50/classification/1?tf-hub-format=compressed -o resnet.tar.gz
    mv 1?tf-hub-format=compressed resnet.tar.gz
    mkdir -p /tmp/resnet/123
    tar xvfz resnet.tar.gz -C /tmp/resnet/123/

    # Create and run a docker image with tensorflow serving using the resnet model
    docker run -d --name serving_base tensorflow/serving
    docker cp /tmp/resnet serving_base:/models/resnet
    docker commit --change "ENV MODEL_NAME resnet" serving_base $USER/resnet_serving
    docker kill serving_base
    docker rm serving_base
    docker run -p 8500:8500 -p 8501:8501 -t $USER/resnet_serving &

To test that the serving works, you can run

    sudo yum install git
    git clone https://github.com/tensorflow/serving
    cd serving/
    pip3.7 install numpy pillow requests
    python3.7 tensorflow_serving/example/resnet_client.py

FROM debian:latest AS build-env
 
# Install flutter dependencies
RUN apt-get update \
    && apt-get install -y \
        curl \
        git \
        wget \
        unzip \
        libgconf-2-4 \
        gdb \
        libstdc++6 \
        libglu1-mesa \
        fonts-droid-fallback \
        lib32stdc++6 \
        python3 \
        sed \
        gdebi-core \
        libnss3 \
        libgconf-2-4 \
    && apt-get clean

RUN apt-get update && apt-get install -y gnupg
 
# Install Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update && \
    apt-get install -y google-chrome-stable
 
WORKDIR /app
 
# Add chromedriver
ADD chromedriver .
RUN chmod +x chromedriver
 
RUN apt install nodejs npm -y
RUN node -v
RUN npm -v

RUN apt install python3
RUN python3 --version
# Clone the flutter repo
RUN git clone --depth 1 --branch 3.7.3 https://github.com/flutter/flutter.git /usr/local/flutter
RUN ls -lrt /usr/local/flutter
 
# Set flutter path
ENV PATH="${PATH}:/usr/local/flutter/bin:/usr/local/flutter/bin/cache/dart-sdk/bin"
 
RUN flutter --version
 
# Run flutter doctor
RUN flutter doctor -v
 
RUN flutter config --enable-web

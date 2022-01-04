FROM gitpod/workspace-full
                
USER root

RUN sudo apt-get update
RUN curl https://cli-assets.heroku.com/install.sh | sudo sh
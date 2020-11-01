#1 make sure that you dont have any old versions of docker running and remove them is you do
sudo apt-get remove docker docker-engine docker.io containerd runc

#2 update your apt-get repos
sudo apt-get update

#3 get and install all the dependecies
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

#4 make sure you add the docker repository to your database
#this also grabs the keys needed
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# use the following to verify the add succeeded
# sudo apt-key fingerprint 0EBFCD88

#5 get the lastest stable release of docker
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io

# https://hub.docker.com/r/06kellyjac/nyancat/
sudo docker run -it --rm --name nyancat 06kellyjac/nyancat
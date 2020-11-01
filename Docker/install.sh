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

#5 add the coker repository to our pat-get repo list  so we can get the lastest stable release of docker
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

#6 run an update on the apt-get repo
sudo apt-get update

#7 get and install docker (community edition cli and container io to run containers)
sudo apt-get install docker-ce docker-ce-cli containerd.io

#8 this is pulling down this nyancat image from docker hub as we going to use this in our tutorial
# https://hub.docker.com/r/06kellyjac/nyancat/
sudo docker run -it --rm --name nyancat 06kellyjac/nyancat
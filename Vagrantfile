# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.network "forwarded_port", guest: 8888, host: 8888
  config.vm.provision "shell", path: "./scripts/init.sh"
end

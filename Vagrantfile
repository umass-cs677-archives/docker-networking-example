Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.provision "docker" do |d|
    d.build_image "/vagrant -f /vagrant/Dockerfile.catalog -t catalog"
    d.build_image "/vagrant -f /vagrant/Dockerfile.front_end -t front_end"
  end
end

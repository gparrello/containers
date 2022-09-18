# Start
## Prepare environment
1. Set a host with docker ```
find how to instal docker and compose tool
```
1. Enable access to the API by adding to `/etc/systemd/system/docker.service.d/override.conf` the following ```
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock -H tcp://0.0.0.0:1111
```
1. Restart the docker service with ```
sudo systemctl restart docker.service docker.socket
```
## Deploy your containes
1. Deploy portainer Business Edition by running ```
cd portainer
docker compose up -d
```
1. Configure the rest of the stacks in `http://HOST_IP:9443`
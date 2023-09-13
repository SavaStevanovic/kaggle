docker build -t pytorch_playground .
xhost + 
docker run --rm --name play -e DISPLAY=$DISPLAY --ipc=host --gpus all -p 6006:6006 -p 5009:5009 -dit -v `pwd`/project:/app -v /mnt/FastData/Data/Data/:/Data -v /tmp/.X11-unix:/tmp/.X11-unix  pytorch_playground

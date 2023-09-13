FROM nvcr.io/nvidia/pytorch:23.03-py3
RUN apt-get update
RUN pip install --upgrade pip 
RUN apt-get install -y libsm6 libxext6 libxrender-dev libgl1-mesa-glx
ENV QT_X11_NO_MITSHM=1
RUN apt-get -y install libprotobuf* protobuf-compiler ninja-build
COPY ./project/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
CMD pip uninstall -y tensorboard-plugin-dlprof; bash

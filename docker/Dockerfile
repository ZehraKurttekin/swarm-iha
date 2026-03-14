# ROS2 Humble Masaüstü sürümünü temel alıyoruz (Gazebo dahil gelir)
FROM osrf/ros:humble-desktop

# Sistem paketlerini güncelle ve temel araçları yükle
RUN apt-get update && apt-get install -y \
    python3-pip \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Çalışma dizinini oluştur
WORKDIR /home/swarm_user/workspace

# Proje dosyalarını buraya kopyalamak istersen (ileride kullanırsın)
# COPY . .

# Başlangıçta ROS2 ortam değişkenlerini yükle
SHELL ["/bin/bash", "-c"]
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

RUN apt-get update && apt-get install -y \
    ros-humble-cv-bridge \
    ros-humble-vision-opencv \
    python3-opencv \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install qrcode[pil]
CMD ["python3", "create_qr.py"]
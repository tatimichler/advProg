# Kali Linux latest with useful tools by tsumarios
FROM kalilinux/kali-rolling

# Set working directory to /root
WORKDIR /root

# Update
RUN apt -y update && DEBIAN_FRONTEND=noninteractive apt -y dist-upgrade && apt -y autoremove && apt clean
RUN DEBIAN_FRONTEND=noninteractive apt -y install curl git

# Install ZSH shell with custom settings and set it as default shell
RUN apt -y install zsh
RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

ENTRYPOINT ["/bin/zsh"]

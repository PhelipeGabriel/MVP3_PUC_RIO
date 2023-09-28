# Define a imagem base no nginx
FROM nginx 

# O nginx é um servidor leve e de código fonte aberto
# Como nossa aplicação irá consultar requisições HTTP, então usaremos uma imagem do Ngnix

# Copia os arquivos de requisitos para o diretório de trabalho do ngnix
COPY . /usr/share/nginx/html

EXPOSE 80

# Define o comando de execução do Servidor nginx
CMD ["nginx" , "-g" , "daemon off;"]

## Comandos para gerar imagem

Geral

```sh
# Listagem
docker images                       # Listar todas as imagens locais
docker ps                           # Listar todos os containers ativos
docker ps -a                        # Listar todos os containers

# Detalhes
docker inspect ID_DO_CONTAINER      # Ver informações do container

# Exclusão
docker rm ID_DO_CONTAINER           # Remover container
docker rm ID_DO_CONTAINER --force   # Remover no brute force
docker rmi ID_DA_IMAGEM             # Remover imagem
```

Criar imagem

```sh
docker build --tag docker-python .
```

Incializar container com a imagem

```sh
docker run docker-python
docker run -d docker-python                                # Detached mode
docker run -p 2300:5000 -d docker-python                   # Mapeando porta 5000 do container para 2300 do host
docker run -p 3000:5000 --network mynet  docker-pythonv2   # Define uso da rede específica

```

Para parar a aplicação

```sh
docker stop ID_DO_CONTAINER
```

Caso seja finalizado, para subir o container novamente:

```sh
docker start ID_DO_CONTAINER
```

Para acessar o bash do container

```sh
docker exec -it ID_DO_CONTAINER bash
```

---

## Banco de dados

```sh
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=senha -d mysql:latest

docker run -e MYSQL_ROOT_PASSWORD=senha --name mysqldb --network mynet -v mysqlVolume:/var/lib/mysql -d mysql:latest

docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=senha -p 3308:3306 -v mysqlVolume:/var/lib/mysql -d mysql:latest

# --name           # define nome do container
# -e               # seta variáveis de ambiente, no caso MYSQL_ROOT_PASSWORD com valor senha
# -d               # entra em modo detached
# mysql:latest     # Define qual versão será usada pela tag
# -v               # Mapeia o diretorio /var/lib/mysql do container para o volume mysqlVolume
# --network mynet  # Define rede mynet. Usado para colocar serviços na mesma rede
```

Inserindo dados por arquivo no db (não é seguro, não faça)

```sh
# Dentro da pasta init
 docker exec -i ID_DO_CONTAINER mysql -u root -psenha <./schema.sql
```

Preferivel fazer:

```sh
docker exec -it ID_DO_CONTAINER bash
```

e dentro do bash do container:

```sh
bash-5.1# mysql -u root -psenha
show databases;
```

---

## Volumes

```sh
# Listar todos os volumes
docker volume ls

# Remover volume
docker volume rm mysqlVolume
```

## Network

```sh
# Listar todos as redes
docker network ls

# Criar rede mynet
docker network create mynet

#Remove network
docker network rm mynet

```

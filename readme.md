## _Environnement de developpement Python3 sous docker_

## Contruire le contener
```bash
[Windows] docker build -t dev-python3:1.00 .
[Linux] sudo docker build -t dev-python3:1.00 .
 ```

 ## Lancer le conteneur
```bash 
[Windows] docker run -it --rm -m 0.5g --name "dev-python3_1.00" -v "%cd%/source":/var/python3 dev-python3:1.00
[Linux] sudo docker run -it --rm -m 0.5g --name "dev-python3_1.00" -v "`pwd`/source":/var/python3 -v dev-python3:1.00
```
# Actividad de Git para el curso de Ingeniería de Software 

## Integrantes: 
Jaime Ramos y Sebastian Chu


# Comandos:
## Para crear el repositorio:
- ```git init```
- - ```git clone https://github.com/JaimeRamosT/test_github_1.git```

## Crear el branch feature1:>
- ```git checkout master```
- ```git branch feature1```
- ```git checkout feature1```
- ```git add .```
- ```git commit app.py -m "commit"```
- ```git push --set-upstream origin feature1```

## Crear el branch feature2:>
- ```git clone https://github.com/JaimeRamosT/test_github_1.git```
- ```git branch```    
- ```git status```    
- ```git checkout master```
- ```git pull origin master```
- ```git checkout -b feature2```
- ```git add .```
- ```git commit app.py -m "commit"```
- ```git push --set-upstream origin feature2```

## Merge el branch feature2 a master con la funcion suma:
- ``` git checkout master```
- ```git merge feature2```    
- ```git commit -m "Merge feature2 en master funcion suma"```    
- ```git push origin master```

## Merge el branch feature2 a master con la funcion multiplicación:
- ``` git rebase feature1```
- ```git merge feature1```    
- ```git commit -m "Merge feature1 en master funcion suma"```    
- ```git push origin master```
  

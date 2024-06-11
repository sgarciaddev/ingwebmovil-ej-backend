## Ejemplo de backend con Flask

<div align="center">

[![python-badge-sm]][python-web]

[![flask-badge-sm]][flask-web] [![sqlite3-badge-sm]][sqlite3-web] [![sqlalchemy-badge-sm]][sqlalchemy-web] 

[![git-badge-sm]][git-web] [![github-badge-sm]][github-web]

</div>

## Descripción

API REST desarrollada con Python y Flask que implementa un CRUD de documentos (API genérica) y se conecta a una base de datos SQLite a través de un **ORM**, *SQLAlchemy*.

**Nota:** Las rutas de la API REST están definidas en el README.md del directorio `backend`.

## Ejecución

Para ejecutar la API REST, primero se debe instalar las dependencias con el siguiente comando:

```bash
pip install -r requirements.txt
```

Luego, se puede ejecutar la API REST con el siguiente comando:

```bash
python main.py
```

**Nota:** Se debe tener instalado **Python** para poder ejecutar la API REST.

### Recomendación: venv

Se recomienda utilizar un entorno virtual de Python para instalar las dependencias y ejecutar la API REST. Para crear un entorno virtual, se puede utilizar el siguiente comando:

```bash
python -m venv venv
```

Luego, se debe activar el entorno virtual con el siguiente comando:

- **Linux/macOS**

```bash
source venv/bin/activate
```

- **Windows**

```bash
venv\Scripts\activate
```

Finalmente, se puede instalar las dependencias y ejecutar la API REST dentro del entorno virtual.

## Estructura de directorios

```
.
└── ./
    ├── app/                      # Directorio base de la aplicación
    │   ├── models                # Definición de modelos de SQLAlchemy
    │   ├── routes                # Manejo de rutas de la API (Flask)
    │   ├── static                # Archivos estáticos (Flask)
    │   └── templates             # Plantillas HTML (Flask)
    ├── config/                   # Configuración de la aplicación
    │   └── sqlalchemy_config.py  # Configuración de SQLAlchemy
    ├── app.py                    # Archivo principal de la aplicación
    ├── README.md                 # Documentación de la API REST
    └── requirements.txt          # Archivo de dependencias de Python
```

[ts-badge-sm]: https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=fff&style=flat
[ts-web]: https://www.typescriptlang.org/
[nodejs-badge-sm]: https://img.shields.io/badge/Node.js-339933?logo=node.js&logoColor=fff&style=flat
[nodejs-web]: https://nodejs.org/
[express-badge-sm]: https://img.shields.io/badge/Express.js-000000?logo=express&logoColor=fff&style=flat
[express-web]: https://expressjs.com/
[git-badge-sm]: https://img.shields.io/badge/Git-F05032?logo=git&logoColor=fff&style=flat
[git-web]: https://git-scm.com/
[github-badge-sm]: https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=fff&style=flat
[github-web]: https://github.com
[npm-badge-sm]: https://img.shields.io/badge/npm-CB3837?logo=npm&logoColor=fff&style=flat
[npm-web]: https://www.npmjs.com/
[yarn-badge-sm]: https://img.shields.io/badge/Yarn-2C8EBB?logo=yarn&logoColor=fff&style=flat
[yarn-web]: https://yarnpkg.com/
[vscode-badge-sm]: https://img.shields.io/badge/Visual_Studio_Code-007ACC?logo=visual-studio-code&logoColor=fff&style=flat
[vscode-web]: https://code.visualstudio.com/
[ionic-badge-sm]: https://img.shields.io/badge/Ionic-3880FF?logo=ionic&logoColor=fff&style=flat
[ionic-web]: https://ionicframework.com/
[ios-development-badge-sm]: https://img.shields.io/badge/iOS_Development-000000?logo=ios&logoColor=fff&style=flat
[ios-development-web]: https://developer.apple.com/ios/
[android-development-badge-sm]: https://img.shields.io/badge/Android_Development-3DDC84?logo=android&logoColor=fff&style=flat
[android-development-web]: https://developer.android.com/
[sqlite3-badge-sm]: https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=fff&style=flat
[sqlite3-web]: https://www.sqlite.org/index.html
[typeorm-badge-sm]: https://img.shields.io/badge/TypeORM-F37626?logo=typeorm&logoColor=fff&style=flat
[typeorm-web]: https://typeorm.io/
[sqlalchemy-badge-sm]: https://img.shields.io/badge/SQLAlchemy-333?logo=sqlalchemy&logoColor=fff&style=flat
[sqlalchemy-web]: https://www.sqlalchemy.org/
[flask-badge-sm]: https://img.shields.io/badge/Flask-000?logo=flask&logoColor=fff&style=flat
[flask-web]: https://flask.palletsprojects.com/
[python-badge-sm]: https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=flat
[python-web]: https://www.python.org/

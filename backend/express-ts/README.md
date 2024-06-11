## Ejemplo de backend con Express.js

<div align="center">

[![ts-badge-sm]][ts-web]

[![express-badge-sm]][express-web] [![nodejs-badge-sm]][nodejs-web] [![sqlite3-badge-sm]][sqlite3-web] [![typeorm-badge-sm]][typeorm-web] 

[![git-badge-sm]][git-web] [![github-badge-sm]][github-web] [![npm-badge-sm]][npm-web] [![yarn-badge-sm]][yarn-web] [![vscode-badge-sm]][vscode-web]

</div>

## Descripción

API REST desarrollada con Express.js y TypeScript que implementa un CRUD de documentos (API genérica) y se conecta a una base de datos SQLite a través de un **ORM**, *TypeORM*.

**Nota:** Las rutas de la API REST están definidas en el README.md del directorio `backend`.

## Ejecución

Para ejecutar la API REST, primero se debe instalar las dependencias con el siguiente comando:

```bash
npm install
```

Luego, se puede ejecutar la API REST con el siguiente comando:

```bash
npm run start
```

**Nota:** Se debe tener instalado **Node.js** para poder ejecutar la API REST.

## Estructura de directorios

```
.
└── ./
    ├── src            # Directorio base de la aplicación
    │   ├── api/       # Manejo de rutas de la API
    │   ├── data/      # Manejo de datos con TypeORM
    │   └── main.ts    # Archivo principal de la aplicación
    ├── .env           # Archivo de variables de entorno
    ├── package.json   # Archivo de configuración de Node
    └── tsconfig.json  # Archivo de configuración de TypeScript
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

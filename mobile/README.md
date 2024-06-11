## Aplicación frontend de ejemplo

<div align="center">

[![ts-badge-sm]][ts-web]

[![ionic-badge-sm]][ionic-web]

[![ios-development-badge-sm]][ios-development-web] [![android-development-badge-sm]][android-development-web]

</div>

## Descripción

Aplicación de Ionic con React de ejemplo para mostrar cómo se puede integrar un frontend con un backend desarrollado con Express.js o Flask. La aplicación se conecta a una API REST que implementa un CRUD de documentos (api genérica) y se conecta a una base de datos SQLite a través de un **ORM**, *TypeORM* en el caso de Express.js y *SQLAlchemy* en el caso de Flask.

La aplicación es **agnóstica al framework de backend**, lo que significa que puede conectarse a cualquiera de las dos API REST utilizando el mismo código.

## Ejecución

Para ejecutar la aplicación, primero se debe instalar las dependencias con el siguiente comando:

```bash
npm install
```

Luego, se puede ejecutar la aplicación con el siguiente comando:

```bash
ionic serve
```

**Nota:** Se debe tener instalado **Node.js** y **Ionic CLI** para poder ejecutar la aplicación.

[ts-badge-sm]: https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=fff&style=flat
[ts-web]: https://www.typescriptlang.org/
[ionic-badge-sm]: https://img.shields.io/badge/Ionic-3880FF?logo=ionic&logoColor=fff&style=flat
[ionic-web]: https://ionicframework.com/
[ios-development-badge-sm]: https://img.shields.io/badge/iOS_Development-000000?logo=ios&logoColor=fff&style=flat
[ios-development-web]: https://developer.apple.com/ios/
[android-development-badge-sm]: https://img.shields.io/badge/Android_Development-3DDC84?logo=android&logoColor=fff&style=flat
[android-development-web]: https://developer.android.com/

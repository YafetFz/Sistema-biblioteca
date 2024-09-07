# Servidor

## Requisitos previos

- Tener Python instalado en tu computadora.
  - Puedes descargarlo e instalarlo desde: [Python.org](https://www.python.org/downloads/)

## Pasos para ejecutar el servidor

### 1. Crear y activar un entorno virtual (`venv`)

1. Abre la terminal de Windows (puedes buscar "cmd" o "PowerShell" en el menú de inicio).
2. Navega al directorio de tu proyecto utilizando el siguiente comando:

   ```bash
   cd ruta/del/proyecto
   ```

3. Crea un entorno virtual en tu proyecto con el siguiente comando:

   ```bash
   python -m venv .venv
   ```

4. Activa el entorno virtual. En Windows, usa este comando:

   ```bash
   .venv\Scripts\activate
   ```

   Si todo está correcto, deberías ver `(venv)` al principio de tu línea de comandos.

### 2. Instalar los paquetes necesarios

Instala las librerías automáticamente ejecutando el siguiente comando:
```bash
pip install -r requirements.txt
```

### 3. Ejecutar el servidor

Una vez que estés en el entorno virtual y en el directorio donde está el script de tu servidor (por ejemplo, `server.py`), ejecuta el servidor con:

```bash
python ./src/index.py
```

Esto iniciará el servidor en tu máquina.

### 4. Cómo detener el servidor

Para detener el servidor, utiliza la combinación de teclas:

```bash
Ctrl + C
```

Esto finalizará el proceso del servidor en la terminal.

### 5. Desactivar el entorno virtual

Cuando hayas terminado de trabajar, puedes desactivar el entorno virtual con el siguiente comando:

```bash
deactivate
```


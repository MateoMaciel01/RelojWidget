# 🕐 Reloj Widget

Aplicación de escritorio para Windows desarrollada en **Python y Tkinter**.

Reloj digital minimalista para utilizar directamente sobre el escritorio, con ventana sin bordes, fondo transparente y diferentes opciones de personalización.

## ✨ Características

- 🕐 Visualización de hora.
- 📅 Visualización de fecha.
- 🖱️ Reloj desplazable por el escritorio.
- 🎨 Personalización del color.
- 🔠 Selección de tipografía.
- 📏 Ajuste del tamaño.
- 🕐 Formato de 12 o 24 horas.
- 👁️ Mostrar u ocultar la fecha.
- 💾 Guardado de configuración.
- 🖥️ Fondo transparente.
- 🚫 Evita ejecutar múltiples instancias simultáneamente.
- 🪟 Ejecutable `.exe` para Windows.

## 🛠️ Tecnologías

- **Python**
- **Tkinter**
- **JSON**
- **PyInstaller**

## 📂 Estructura

```text
RelojWidget/
├── Reloj.py
├── config.json
├── logo.ico
├── fuentes/
│   └── Archivos .ttf
├── dist/
│   └── Reloj.exe
└── .gitignore
```

## ▶️ Uso

No es necesario instalar Python para utilizar la versión ejecutable.

Ejecutá:

```text
dist/Reloj.exe
```

El reloj aparecerá directamente en el escritorio.

### Controles

- **Clic izquierdo + arrastrar:** mover el reloj.
- **Clic derecho:** abrir el menú de configuración.
- **Configuración:** modificar tamaño, color, tipografía, formato de hora y visibilidad de la fecha.

## ⚙️ Configuración

Las preferencias se almacenan en:

```text
config.json
```

De esta manera, la configuración se mantiene al volver a iniciar la aplicación.

## 📌 Estado del proyecto

**En desarrollo.**

El proyecto cuenta actualmente con las principales funcionalidades del reloj y su sistema de personalización.

## 👨‍💻 Autor

**Mateo Maciel**


# 🛒 Sistema POS (Punto de Venta)

Este proyecto es una aplicación de sistema POS (Punto de Venta) desarrollada con **Streamlit** (frontend) y **Flask** (backend). Permite a los usuarios autenticarse, gestionar un carrito de compras, seleccionar métodos de pago, ganar o canjear puntos de fidelización, y generar facturas en PDF.

## 🚀 Tecnologías

- **Frontend**: Streamlit
- **Backend**: Flask
- **Base de datos**: SQLite
- **PDF**: ReportLab
- **API de prueba productos/clientes**: JSONPlaceholder (para pruebas)

---

## ⚙️ Funcionalidades

### 🔐 Login
- Autenticación de clientes usando email y username.
- Gestión de sesiones con token JWT.

### 📦 Productos
- Visualización de productos desde API externa.
- Agregar productos al carrito.
- Manejo de cantidades y subtotal.

### 🛍️ Carrito de Compras
- Visualización de productos añadidos.
- Aplicación de puntos de fidelización como descuento.
- Selección de métodos de pago:
  - Efectivo
  - Tarjeta de crédito/débito
  - Transferencia bancaria

### 💳 Fidelización
- Sistema de puntos: 1 punto por cada $10 gastados.
- Canje de puntos como descuento.
- Actualización de puntos del cliente en base de datos.

### 🧾 Factura PDF
- Generación de factura con datos del cliente, productos comprados, método de pago y resumen total.
- Creación automática del PDF usando ReportLab.

---

## 📁 Estructura del Proyecto

sistema-pos/
│
├── backend/
│   ├── app.py                      # App principal Flask
|   ├── src/ 
|   |    ├── routes/
|   |        └──auth.py                   
│   |    ├── utils/
│   │       └── compra.py            # Lógica para guardar puntos, generar factura, etc.
│   └── .env                        # Variables de entorno (token secret, etc.)
|   └── ConnectDB.py
|   └── data_clientes.py            # Logica para guardar clientes
|   └── data_productos.py           # Logica para guardar productos
|   └── populate_db.py              # Logica para llenar las tablas
│
├── frontend/
│   ├── app.py                      # Punto de entrada de 
Streamlit
│   ├── components/
│   │   └── header.py              # Cabecera con carrito, 
│   ├── viewmodels/
│   │   ├── products_vm.py         # Lógica de productos
│   │   └── cart_vm.py             # Lógica de carrito y pagos
|   |   └── clientes_vm.py         # Lógica de clientes
|   |   └── compras.py             # Lógica de compras
│   ├── utils/
│   │   ├── auth.py               # URLs de backend, helpers
│   │   └── config.py 
|   |   └── factura.py              # Manejo de sesión, token, usuario
│   ├── views/
│   │   ├── products_page.py     # Vista de productos
│   │   └── cart_page.py         # Vista del carrito
|   |   └── clientes_page.py     # Vista de  clientes
|   |   └── home_page.py         # Vista de  home
|   |   └── login_page.py        # Vista login
│   └── .env                      # BACKEND_URL y otras configuraciones
│
├── facturas/                     # Para guardar las facturas
│
├── README.md                      # Documentación del proyecto
└── requirements.txt               # Dependencias del frontend y backend


📄 Licencia

Este proyecto es de uso libre con fines educativos. Puedes adaptarlo o ampliarlo según tus necesidades. 🚀

✨ Créditos
Desarrollado por RobARC con ❤️, café ☕ y muchas líneas de código.



---

## ▶️ Instrucciones

### 🔧 Instalación

```bash
git clone https://github.com/tu_usuario/sistema-pos.git
cd sistema-pos
pip install -r requirements.txt


🔐 Configurar Variables de Entorno
Crea un archivo .env en frontend/ y backend/ con:

BACKEND_URL=http://localhost:5000
SSK=secreto_super_seguro

🚀 Ejecutar el Backend

cd backend
python app.py

🖥️ Ejecutar el Frontend

cd frontend
streamlit run app.py


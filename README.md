# 🇳🇮 NICWA: Nicaraguan Financial Assistant (Telegram Bot)

**NICWA** es un asistente financiero automatizado en formato de bot para Telegram. Su objetivo principal es resolver un problema cotidiano en Nicaragua: centralizar, comparar y calcular el tipo de cambio del dólar (USD/NIO) de manera rápida, sencilla y sin salir de tu aplicación de mensajería.

---

## 💡 ¿Por qué existe este proyecto? (El Problema Real)

En Nicaragua, el tipo de cambio del dólar frente al córdoba cambia constantemente y varía significativamente entre los principales bancos del país. Para una persona común o un comercio, comparar tasas de cambio implica ingresar manualmente a los sitios web de múltiples bancos (BAC, Banpro, Lafise, etc.), buscar la sección de divisas y realizar cálculos matemáticos manuales en la calculadora del teléfono.

**NICWA automatiza este proceso:**
1. **Centraliza la información:** Muestra en una sola pantalla las tasas de los bancos más importantes de Nicaragua.
2. **Elimina el error humano:** El usuario no tiene que decidir si debe multiplicar o dividir por el tipo de cambio; el bot hace la conversión exacta de forma automática utilizando lógica financiera real.

---

## 🧮 Lógica Financiera del Algoritmo

Este bot no es una simple calculadora que multiplica números al azar; el sistema implementa **reglas de negocio financieras reales** basándose en la intención de la transacción del usuario:

* **De Dólares a Córdobas (USD ➡️ NIO):** El algoritmo detecta que el usuario "tiene dólares" y, por lo tanto, el banco se los va a comprar. Aplica automáticamente la **tasa de Compra (Buy rate)** de la entidad seleccionada.
* **De Córdobas a Dólares (NIO ➡️ USD):** El algoritmo detecta que el usuario "necesita dólares" y, por lo tanto, el banco se los va a vender. Aplica automáticamente la **tasa de Venta (Sell rate)** de la entidad seleccionada.

---

## ✨ Características Principales

* **🏦 Cobertura de Bancos Locales:** Soporte diseñado para procesar tasas de BAC, Banpro, Lafise, Ficohsa, BDF y la tasa oficial del Banco Central de Nicaragua (BCN).
* **📱 Interfaz de Usuario Avanzada (UX):** Navegación 100% interactiva mediante botones dinámicos en los mensajes (`InlineKeyboardMarkup`). El usuario realiza consultas completas con toques de pantalla, sin necesidad de memorizar o escribir comandos complejos de texto.
* **🔁 Flujo de Usuario Continuo:** Gestión del estado de la conversación para que el usuario pueda encadenar múltiples cálculos consecutivos sin tener que reiniciar el bot desde cero.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3
* **Biblioteca Principal:** `pyTelegramBotAPI` (Telebot)

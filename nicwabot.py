import os
import telebot
from telebot import types
# Importamos dotenv para cargar las variables de entorno de un archivo .env local
from dotenv import load_dotenv

# Cargamos el archivo .env
load_dotenv()

# 1. CONFIGURACIÓN SEGURA
# El bot buscará una variable de entorno llamada 'TELEGRAM_TOKEN'
TOKEN = os.getenv('AQUI TU TOKEN')

if not TOKEN:
    raise ValueError("❌ ERROR: No se encontró el TOKEN de Telegram. Asegúrate de configurar tu archivo .env")

bot = telebot.TeleBot(TOKEN)

# Memoria temporal para guardar en qué paso va cada usuario
datos_usuarios = {}

# 2. SIMULACIÓN DE API (MOCK)
def obtener_tasas_bancos():
    """
    En un entorno real, se conectarías a tu propia API o 
    Web Scraping a las páginas del BAC, Banpro, etc.
    Por ahora, se usa un diccionario con tasas simuladas.
    """
    return {
        "BAC": {"compra": 36.40, "venta": 36.80},
        "Banpro": {"compra": 36.42, "venta": 36.78},
        "Lafise": {"compra": 36.35, "venta": 36.85},
        "Ficohsa": {"compra": 36.40, "venta": 36.82},
        "BDF": {"compra": 36.41, "venta": 36.79},
        "BCN (Oficial)": {"compra": 36.6243, "venta": 36.6243} 
    }

# 3. FUNCIÓN DE BIENVENIDA (Reutilizable para el bucle)
def enviar_inicio(chat_id):
    texto = (
        "🇳🇮 *¡Bienvenido a NICWA!* 🇳🇮\n\n"
        "Tu Asistente de Tasa de Cambio Profesional para Nicaragua.\n\n"
        "Elige una opción para comenzar:"
    )
    markup = types.InlineKeyboardMarkup()
    btn_bancos = types.InlineKeyboardButton("🏦 Lista de Bancos en Nicaragua", callback_data="ver_bancos")
    markup.add(btn_bancos)
    
    bot.send_message(chat_id, texto, parse_mode="Markdown", reply_markup=markup)

# 4. INICIO DEL BOT (Comando /start)
@bot.message_handler(commands=['start'])
def cmd_start(message):
    enviar_inicio(message.chat.id)

# 5. MANEJADOR DE BOTONES INLINE (El corazón interactivo del bot)
@bot.callback_query_handler(func=lambda call: True)
def manejar_botones(call):
    chat_id = call.message.chat.id
    
    # --- SI PRESIONA "VER BANCOS" ---
    if call.data == "ver_bancos":
        texto = "🏦 *LISTA DE BANCOS EN NICARAGUA*\n\nSelecciona el banco que utilizas:"
        markup = types.InlineKeyboardMarkup(row_width=2)
        
        bancos = obtener_tasas_bancos()
        botones = []
        for nombre_banco in bancos.keys():
            botones.append(types.InlineKeyboardButton(nombre_banco, callback_data=f"banco_{nombre_banco}"))
        
        markup.add(*botones)
        bot.edit_message_text(texto, chat_id, call.message.message_id, parse_mode="Markdown", reply_markup=markup)
        
    # --- SI PRESIONA UN BANCO ESPECÍFICO ---
    elif call.data.startswith("banco_"):
        banco_elegido = call.data.split("_")[1]
        
        if chat_id not in datos_usuarios:
            datos_usuarios[chat_id] = {}
        datos_usuarios[chat_id]['banco'] = banco_elegido
        
        tasas = obtener_tasas_bancos()[banco_elegido]
        
        texto = (
            f"🏛 *{banco_elegido}*\n\n"
            f"📉 *Compra:* {tasas['compra']} NIO\n"
            f"📈 *Venta:* {tasas['venta']} NIO\n\n"
            f"¿Qué conversión deseas hacer?"
        )
        
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("💵 USD a NIO (Vendes tus Dólares)", callback_data="conv_USD_NIO"),
            types.InlineKeyboardButton("🇳🇮 NIO a USD (Compras Dólares)", callback_data="conv_NIO_USD"),
            types.InlineKeyboardButton("⬅️ Volver a la lista", callback_data="ver_bancos")
        )
        bot.edit_message_text(texto, chat_id, call.message.message_id, parse_mode="Markdown", reply_markup=markup)
        
    # --- SI PRESIONA EL TIPO DE CONVERSIÓN ---
    elif call.data.startswith("conv_"):
        direccion = call.data.replace("conv_", "")
        datos_usuarios[chat_id]['direccion'] = direccion
        
        bot.edit_message_text("⏳ Preparando calculadora...", chat_id, call.message.message_id)
        
        texto = "✍️ *Ingresa el monto a convertir:*\n_(Escribe solo números, usa punto para decimales. Ej: 150.50)_"
        msg = bot.send_message(chat_id, texto, parse_mode="Markdown")
        
        bot.register_next_step_handler(msg, calcular_conversion)

# 6. FUNCIÓN DE CÁLCULO Y BUCLE
def calcular_conversion(message):
    chat_id = message.chat.id
    try:
        monto = float(message.text.replace(',', '.'))
        
        user_data = datos_usuarios.get(chat_id, {})
        banco = user_data.get('banco')
        direccion = user_data.get('direccion')
        
        if not banco or not direccion:
            bot.send_message(chat_id, "⚠️ La sesión expiró. Reiniciando...")
            enviar_inicio(chat_id)
            return
            
        tasas = obtener_tasas_bancos()[banco]
        
        if direccion == "USD_NIO":
            tasa_usada = tasas['compra']
            resultado = monto * tasa_usada
            mensaje_resultado = (
                f"✅ *Cálculo en {banco}*\n\n"
                f"💵 Entregas: `{monto:.2f} USD`\n"
                f"🇳🇮 Recibes: `{resultado:.2f} NIO`\n\n"
                f"_(Se aplicó la tasa de COMPRA: {tasa_usada})_"
            )
        else:
            tasa_usada = tasas['venta']
            resultado = monto / tasa_usada
            mensaje_resultado = (
                f"✅ *Cálculo en {banco}*\n\n"
                f"🇳🇮 Entregas: `{monto:.2f} NIO`\n"
                f"💵 Recibes: `{resultado:.2f} USD`\n\n"
                f"_(Se aplicó la tasa de VENTA: {tasa_usada})_"
            )
        
        bot.send_message(chat_id, mensaje_resultado, parse_mode="Markdown")
        enviar_inicio(chat_id)
        
    except ValueError:
        msg = bot.send_message(chat_id, "❌ Error: Solo debes ingresar números. Intenta de nuevo:")
        bot.register_next_step_handler(msg, calcular_conversion)

# 7. ENCENDIDO
if __name__ == "__main__":
    print("Bot NICWA encendido y esperando usuarios...")
    bot.polling()

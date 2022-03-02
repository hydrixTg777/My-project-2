from pyrogram import Client


Client = Client(
    "PyrogramBot",
    api_hash="7d120384f48b2a86fa2b9e9772a28af6",
    api_id="18891187",
    bot_token="5259490489:AAFZuTQ2PcQdrYG8_N2eZMfESgUWHsJtDWo",
    plugins=dict(root="PyrogramBot")
)

Client.run()

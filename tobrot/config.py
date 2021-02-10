from tobrot.sample_config import Config

#read readme too before filling these stuffs

class Config(Config):
    TG_BOT_TOKEN= "1658143488:AAHv7HKl9Tyz20VjrzBz1HkDrKQ3NKMnddg" #imp
    APP_ID = 1244657 #imp
    API_HASH = "b0fb3b798db670add65ae064006a856d" #imp
    AUTH_CHANNEL = [-1001405974567, 873537185] #imp replace your_id with your id from telegram or delete
    INDEX_LINK = "https://torrentleech.torrentleech-gdrive.workers.dev"
    GLEECH_COMMAND = "gleech@TorrentUpBot"
    YTDL_COMMAND = 'ytdl@TorrentUpBot'
    TELEGRAM_LEECH_COMMAND_G = "tleech@TorrentUpBot"
    CLONE_COMMAND_G = "gclone@groupname"
    PYTDL_COMMAND_G = "pytdl@groupname"
    DESTINATION_FOLDER = "TorrentUpBot"
    LEECH_COMMAND = "leech@TorrentUpBot"
    CANCEL_COMMAND_G = "cancel@TorrentUpBot"
    RCLONE_CONFIG = """type = drive\nscope = drive\ntoken = {"access_token":"ya29.A0AfH6SMC77_jG23q5CWp-tnvDuBOAvmaOMJOlam4pef7zVeLivIUVJvY_vrpsKvnrxefc5sYCMS0Q4D5cOccNEpYEwvSiYeOo4eKe9ru-T5cEj_aAyyQdl0Lek-QnnCMWj61TB_-eli0q0V6MEDXTBrHJovlE","token_type":"Bearer","refresh_token":"1//04J9D1WvLhkERCgYIARAAGAQSNwF-L9IrKMxyzsG96G0agfwWu7pTyssNyXu-0xUUINciWQKW1sZiJ1mAOv4kjbbyKQ8DsgIxP3E","expiry":"2021-02-10T14:32:49.972607642+07:00"}\nteam_drive = 0AP-celMwOXo9Uk9PVA"""
    #put your config(replacing new lines with \n) in triple quote like above: """<your one liner config>"""

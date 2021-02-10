from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "1658143488:AAHv7HKl9Tyz20VjrzBz1HkDrKQ3NKMnddg"
    APP_ID = 1244657
    API_HASH = "b0fb3b798db670add65ae064006a856d"
    OWNER_ID = 873537185
    AUTH_CHANNEL = [-1001405974567]
    DESTINATION_FOLDER = "TorrentUpBot" #Name of your folder read readme(not id of the folder)
    #Just don't fill RCLONE_CONFIG vars, insted copy your rclone.conf file in root directory
    #if your wanted to fill -- fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    RCLONE_CONFIG = """
[DRIVE]
type = drive
client_id = 202264815644.apps.googleusercontent.com
client_secret = X4Z3ca8xfWDb1Voo-F9a7ZxJ
scope = drive
root_folder_id =
token = {"access_token":"ya29.A0AfH6SMC77_jG23q5CWp-tnvDuBOAvmaOMJOlam4pef7zVeLivIUVJvY_vrpsKvnrxefc5sYCMS0Q4D5cOccNEpYEwvSiYeOo4eKe9ru-T5cEj_aAyyQdl0Lek-QnnCMWj61TB_-eli0q0V6MEDXTBrHJovlE","token_type":"Bearer","refresh_token":"1//04J9D1WvLhkERCgYIARAAGAQSNwF-L9IrKMxyzsG96G0agfwWu7pTyssNyXu-0xUUINciWQKW1sZiJ1mAOv4kjbbyKQ8DsgIxP3E","expiry":"2021-02-10T14:32:49.972607642+07:00"}
team_drive = 0AP-celMwOXo9Uk9PVA
"""

import dropbox
class Storage:
    def __init__(self,access_token):
        self.access_token=access_token
    def uploadFile(self,file_from, file_to):
        dbx= dropbox.Dropbox(self.access_token)
        F = open(file_from,'rb')
        dbx.files_upload(F.read(),file_to)
def main():
    access_token = 'sl.Auc1X6JjB3JxcGNVv9NrZV1uT6Jh4feYaekqckTfGAu4e5NE6PmK2djt16BDh3_xD6IuBy0-EVH9bxRgr8x4g2wuFDmhJIvEiJzu9jQDHwE01PnR-wN7mJhyeuDdREG7rG2zGfs'
    storage1 = Storage(access_token)
    file_from = input("enter the path of the file you want to upload:   ")
    file_to = input("enter the path name to upload to dropbox:   ")
    storage1.uploadFile(file_from, file_to)
    print("file is uploaded")

dbx = dropbox.Dropbox('sl.Auc1X6JjB3JxcGNVv9NrZV1uT6Jh4feYaekqckTfGAu4e5NE6PmK2djt16BDh3_xD6IuBy0-EVH9bxRgr8x4g2wuFDmhJIvEiJzu9jQDHwE01PnR-wN7mJhyeuDdREG7rG2zGfs')
print(dbx.users_get_current_account())
f = open('C:/Users/ayushman.puri/Documents/other stuff/whj/ConnectToDropbox/storage.py','rb')
#dbx.files_upload(f.read(),'/storage.py')
print(f.read())
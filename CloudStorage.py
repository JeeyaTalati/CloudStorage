import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
       dbx=dropbox.Dropbox(self.access_token) 
       with open(file_from,'rb') as f:
           dbx.files_upload(f.read(),file_to)
def main():
    access_token="LgWmF8De57UAAAAAAAAAAUqhKUquJUTePdeSW7uKhcCWkEeKGqQwDCddjz3i9-2t"
    transferData=TransferData(access_token)
    file_from=input("Enter The File Name to be Moved")
    file_to=input("The Final Destination")
    transferData.upload_file(file_from,file_to)
if __name__ == '__main__':
    main()
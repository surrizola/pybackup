#pip install PyDrive


# Cliend id 975707925996-cbpk6vnrvhkooorubcsog86e71b3i9l2.apps.googleusercontent.com
# Secret B4iLh6ms_xstt-M4gqhVEIi1

from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

def backupFile(file):
	print "UPLOAD FILE "+file
	gauth = GoogleAuth()
	# Try to load saved client credentials
	gauth.LoadCredentialsFile("mycreds.txt")
	if gauth.credentials is None:		
		gauth.LocalWebserverAuth()
	elif gauth.access_token_expired:    	
		gauth.Refresh()
	else:
		gauth.Authorize()
	gauth.SaveCredentialsFile("mycreds.txt")

	drive = GoogleDrive(gauth)

	textfile = drive.CreateFile()
	textfile.SetContentFile(file)
	textfile.Upload()
	print textfile

	drive.CreateFile({'id':textfile['id']}).GetContentFile('eng-dl.txt')


#backupFile('test.txt')
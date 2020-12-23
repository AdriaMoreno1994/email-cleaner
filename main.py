from imapclient import IMAPClient
mail = IMAPClient('imap.gmail.com', ssl=True, port=993)
mail.login("***********", "***********")
totalMail = mail.select_folder('Inbox')
#print the total amount of messages
print('You have total %d messages in your folder' % totalMail[b'EXISTS'])
delMsg = mail.search(('UNSEEN'))
mail.delete_messages(delMsg)
#print the number of mails unseen in the inbox
print('%d unread messages in your folder have been deleted' % len(delMsg))
mail.logout()
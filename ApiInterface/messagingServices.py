from .models import Message


def UpdateIsRead(pk):
    message = Message.objects.get(pk=pk)
    message.IsRead = True
    message.save()

def GetUnreadMessages():
    messages = Message.objects.filter(IsRead = False).order_by('MessageDate')
    return messages

def DeleteMessage(pk):
    Message.objects.filter(pk=pk).delete()

def GetMessage(pk):
    message = Message.objects.filter(pk=pk)
    return message

def GetMessagesList():
    messages = Message.objects.all().order_by('MessageDate')
    return messages

#def UpdateMessage(pk):

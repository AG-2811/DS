# def vote(age): 
#     if age > 18:
#         print('You can vote.')
#     else:
#         print('Your are minor.')
# vote(17)
def sound_box(amount,platform='Paytm'):
    from gtts import gTTS
    text = f'''{platform} par {amount} prapt hue.'''
    audio = gTTS(text)
    audio.save('paytm.mp3')
    import pygame as p
    p.init()
    music = p.mixer.Sound('paytm.mp3')
    music.play()
sound_box('500','Phonepe')

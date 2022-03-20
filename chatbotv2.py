import discord
from discord import message
from discord.ext import commands
import random
import pickle

bot = commands.Bot(command_prefix = '~')

#Variables
happy_words = ['happy']
sad_words = ['sad']
funny_words = ['funny']
angry_words = ['angry']
romantic_words = ['romantic']
bored_words = ['bored']
excited_words = ['excited']
greetings_words = ['greetings']
farewell_words = ['farewell']
scared_words = ['scared']
happy_responses = []
sad_responses = []
funny_responses = []
angry_responses = []
romantic_responses = []
bored_responses = []
excited_responses = []
greetings_responses = []
farewell_responses = []
scared_responses = []
moods = ['happy', 'sad', 'funny', 'angry', 'romantic', 'bored', 'excited', 'greetings', 'farewell', 'scared']
word_mood = ''
new_response_command_mood = ''
chosen_response_list = ''
unknown_responses = False
waiting_new_response = False
waiting_new_response_c = False
new_keyword_command_mood = ''
waiting_new_keyword_c = False

quote_counter = 41
quote = ''
quote_author = ''
quote_date = ''

def saveData(Mood):
    if Mood == 'happy':
        happyresp = open("happyresp.dat", "wb")
        pickle.dump(happy_responses, happyresp)
        happyresp.close()
        happykey = open("happykey.dat", "wb")
        pickle.dump(happy_words, happykey)
        happykey.close()
    elif Mood == 'sad':
        sadresp = open("sadresp.dat", "wb")
        pickle.dump(sad_responses, sadresp)
        sadresp.close()
        sadkey = open("sadkey.dat", "wb")
        pickle.dump(sad_words, sadkey)
        sadkey.close()
    elif Mood == 'funny':
        funnyresp = open("funnyresp.dat", "wb")
        pickle.dump(funny_responses, funnyresp)
        funnyresp.close()
        funnykey = open("funnykey.dat", "wb")
        pickle.dump(funny_words, funnykey)
        funnykey.close()
    elif Mood == 'angry':
        angryresp = open("angryresp.dat", "wb")
        pickle.dump(angry_responses, angryresp)
        angryresp.close()
        angrykey = open("angrykey.dat", "wb")
        pickle.dump(angry_words, angrykey)
        angrykey.close()
    elif Mood == 'romantic':
        romanticresp = open("romanticesp.dat", "wb")
        pickle.dump(romantic_responses, romanticresp)
        romanticresp.close()
        romantickey = open("romantickey.dat", "wb")
        pickle.dump(romantic_words, romantickey)
        romantickey.close()
    elif Mood == 'bored':
        boredresp = open("boredresp.dat", "wb")
        pickle.dump(bored_responses, boredresp)
        boredresp.close()
        boredkey = open("boredkey.dat", "wb")
        pickle.dump(bored_words, boredkey)
        boredkey.close()
    elif Mood == 'excited':
        excitedresp = open("excitedresp.dat", "wb")
        pickle.dump(excited_responses, excitedresp)
        excitedresp.close()
        excitedkey = open("excitedkey.dat", "wb")
        pickle.dump(excited_words, excitedkey)
        excitedkey.close()
    elif Mood == 'greetings':
        greetingsresp = open("greetingsresp.dat", "wb")
        pickle.dump(greetings_responses, greetingsresp)
        greetingsresp.close()
        greetingskey = open("greetingskey.dat", "wb")
        pickle.dump(greetings_words, greetingskey)
        greetingskey.close()
    elif Mood == 'farewell':
        farewellresp = open("farewellresp.dat", "wb")
        pickle.dump(farewell_responses, farewellresp)
        farewellresp.close()
        farewellkey = open("farewellkey.dat", "wb")
        pickle.dump(farewell_words, farewellkey)
        farewellkey.close()
    elif Mood == 'scared':
        scaredresp = open("scaredresp.dat", "wb")
        pickle.dump(scared_responses, scaredresp)
        scaredresp.close()
        scaredkey = open("scaredkey.dat", "wb")
        pickle.dump(scared_words, scaredkey)
        scaredkey.close()

#Bot Ready
@bot.event
async def on_ready():
    print('Bot is ready')

    global happy_words
    global sad_words
    global funny_words
    global angry_words
    global romantic_words
    global bored_words
    global excited_words
    global greetings_words
    global farewell_words
    global scared_words
    global happy_responses
    global sad_responses
    global funny_responses
    global angry_responses
    global romantic_responses
    global bored_responses
    global excited_responses
    global greetings_responses
    global farewell_responses
    global scared_responses

    happykeyread = open("happykey.dat", "rb")
    happy_words = pickle.load(happykeyread)
    happykeyread.close()
    sadkeyread = open("sadkey.dat", "rb")
    sad_words = pickle.load(sadkeyread)
    sadkeyread.close()
    funnykeyread = open("funnykey.dat", "rb")
    funny_words = pickle.load(funnykeyread)
    funnykeyread.close()
    angrykeyread = open("angrykey.dat", "rb")
    angry_words = pickle.load(angrykeyread)
    angrykeyread.close()
    romantickeyread = open("romantickey.dat", "rb")
    romantic_words = pickle.load(romantickeyread)
    romantickeyread.close()
    boredkeyread = open("boredkey.dat", "rb")
    bored_words = pickle.load(boredkeyread)
    boredkeyread.close()
    excitedkeyread = open("excitedkey.dat", "rb")
    excited_words = pickle.load(excitedkeyread)
    excitedkeyread.close()
    greetingskeyread = open("greetingskey.dat", "rb")
    greetings_words = pickle.load(greetingskeyread)
    greetingskeyread.close()
    farewellkeyread = open("farewellkey.dat", "rb")
    farewell_words = pickle.load(farewellkeyread)
    farewellkeyread.close()
    scaredkeyread = open("scaredkey.dat", "rb")
    scared_words = pickle.load(scaredkeyread)
    scaredkeyread.close()

    happyrespread = open("happyresp.dat", "rb")
    happy_responses = pickle.load(happyrespread)
    happyrespread.close()
    sadrespread = open("sadresp.dat", "rb")
    sad_responses = pickle.load(sadrespread)
    sadrespread.close()
    funnyrespread = open("funnyresp.dat", "rb")
    funny_responses = pickle.load(funnyrespread)
    funnyrespread.close()
    angryrespread = open("angryresp.dat", "rb")
    angry_responses = pickle.load(angryrespread)
    angryrespread.close()
    romanticrespread = open("romanticesp.dat", "rb")
    romantic_responses = pickle.load(romanticrespread)
    romanticrespread.close()
    boredrespread = open("boredresp.dat", "rb")
    bored_responses = pickle.load(boredrespread)
    boredrespread.close()
    excitedrespread = open("excitedresp.dat", "rb")
    excited_responses = pickle.load(excitedrespread)
    excitedrespread.close()
    greetingsrespread = open("greetingsresp.dat", "rb")
    greetings_responses = pickle.load(greetingsrespread)
    greetingsrespread.close()
    farewellrespread = open("farewellresp.dat", "rb")
    farewell_responses = pickle.load(farewellrespread)
    farewellrespread.close()
    scaredrespread = open("scaredresp.dat", "rb")
    scared_responses = pickle.load(scaredrespread)
    scaredrespread.close()

#Maintenance Commands
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def interact(ctx):
    pass

#Help Command
@bot.command()
async def chatbot(ctx):
    await ctx.send('List of commands:\n*~response mood* - Creates a new response for a mood.\n*~deleteresp mood responsenumber* - Deletes a response from a mood.\n*~listresp mood* - Lists responses for a mood.\n*~keyword mood* - Creates a new keyword for a mood.\n*~deletekey mood keywordnumber* - Deletes a keyword from a mood.\n*~listkey mood* - Lists keywords for a mood.\n*~listmoods* - Lists moods.\n*~quote* - Quotes a channel member.')

#Add Response to Mood
@bot.command()
async def response(ctx, mood):
    global new_response_command_mood
    global waiting_new_response_c
    if mood == 'happy':
        new_response_command_mood = 0
        waiting_new_response_c = True
        await ctx.send("The next sent message will be added to the list of responses for the mood: " + mood)
    elif mood == 'sad':
        new_response_command_mood = 1
        waiting_new_response_c = True
        await ctx.send("The next sent message will be added to the list of responses for the mood: " + mood)
    elif mood == 'funny':
        new_response_command_mood = 2
        waiting_new_response_c = True
        await ctx.send("The next sent message will be added to the list of responses for the mood: " + mood)
    elif mood == 'angry':
        new_response_command_mood = 3
        waiting_new_response_c = True
        await ctx.send("The next sent message will be added to the list of responses for the mood: " + mood)
    elif mood == 'romantic':
        new_response_command_mood = 4
        waiting_new_response_c = True
        await ctx.send("The next sent message will be added to the list of responses for the mood: " + mood)
    elif mood == 'bored':
        new_response_command_mood = 5
        waiting_new_response_c = True
        await ctx.send("The next sent message will be added to the list of responses for the mood: " + mood)
    elif mood == 'excited':
        new_response_command_mood = 6
        waiting_new_response_c = True
        await ctx.send("The next sent message will be added to the list of responses for the mood: " + mood)
    elif mood == 'greetings':
        new_response_command_mood = 7
        waiting_new_response_c = True
        await ctx.send("The next sent message will be added to the list of responses for the mood: " + mood)
    elif mood == 'farewell':
        new_response_command_mood = 8
        waiting_new_response_c = True
        await ctx.send("The next sent message will be added to the list of responses for the mood: " + mood)
    elif mood == 'scared':
        new_response_command_mood = 9
        waiting_new_response_c = True
        await ctx.send("The next sent message will be added to the list of responses for the mood: " + mood)

#Delete Response from Mood
@bot.command()
async def deleteresp(ctx, mood, number):
    if mood == 'happy':
        await ctx.send('\'' + happy_responses[int(number)-1] + '\' has been removed from the list of responses for the mood: ' + mood)
        happy_responses.pop(int(number)-1)
        saveData('happy')
    elif mood == 'sad':
        await ctx.send('\'' + sad_responses[int(number)-1] + '\' has been removed from the list of responses for the mood: ' + mood)
        sad_responses.pop(int(number)-1)
        saveData('sad')
    elif mood == 'funny':
        await ctx.send('\'' + funny_responses[int(number)-1] + '\' has been removed from the list of responses for the mood: ' + mood)
        funny_responses.pop(int(number)-1)
        saveData('funny')
    elif mood == 'angry':
        await ctx.send('\'' + angry_responses[int(number)-1] + '\' has been removed from the list of responses for the mood: ' + mood)
        angry_responses.pop(int(number)-1)
        saveData('angry')
    elif mood == 'romantic':
        await ctx.send('\'' + romantic_responses[int(number)-1] + '\' has been removed from the list of responses for the mood: ' + mood)
        romantic_responses.pop(int(number)-1)
        saveData('romantic')
    elif mood == 'bored':
        await ctx.send('\'' + bored_responses[int(number)-1] + '\' has been removed from the list of responses for the mood: ' + mood)
        bored_responses.pop(int(number)-1)
        saveData('bored')
    elif mood == 'excited':
        await ctx.send('\'' + excited_responses[int(number)-1] + '\' has been removed from the list of responses for the mood: ' + mood)
        excited_responses.pop(int(number)-1)
        saveData('excited')
    elif mood == 'greetings':
        await ctx.send('\'' + greetings_responses[int(number)-1] + '\' has been removed from the list of responses for the mood: ' + mood)
        greetings_responses.pop(int(number)-1)
        saveData('greetings')
    elif mood == 'farewell':
        await ctx.send('\'' + farewell_responses[int(number)-1] + '\' has been removed from the list of responses for the mood: ' + mood)
        farewell_responses.pop(int(number)-1)
        saveData('farewell')
    elif mood == 'scared':
        await ctx.send('\'' + scared_responses[int(number)-1] + '\' has been removed from the list of responses for the mood: ' + mood)
        scared_responses.pop(int(number)-1)
        saveData('scared')
    
#Display Responses for Mood
@bot.command()
async def listresp(ctx, mood):
    if mood == 'happy':
        await ctx.send('Happy responses: ' + str(happy_responses))
    elif mood == 'sad':
        await ctx.send('Sad responses: ' + str(sad_responses))
    elif mood == 'funny':
        await ctx.send('Funny responses: ' + str(funny_responses))
    elif mood == 'angry':
        await ctx.send('Angry responses: ' + str(angry_responses))
    elif mood == 'romantic':
        await ctx.send('Romantic responses: ' + str(romantic_responses))
    elif mood == 'bored':
        await ctx.send('Bored responses: ' + str(bored_responses))
    elif mood == 'excited':
        await ctx.send('Excited responses: ' + str(excited_responses))
    elif mood == 'greetings':
        await ctx.send('Greetings responses: ' + str(greetings_responses))
    elif mood == 'farewell':
        await ctx.send('Farewell responses: ' + str(farewell_responses))
    elif mood == 'scared':
        await ctx.send('Scared responses: ' + str(scared_responses))

#Add Keyword for Mood
@bot.command()
async def keyword(ctx, mood):
    global new_keyword_command_mood
    global waiting_new_keyword_c
    if mood == 'happy':
        new_keyword_command_mood = 0
        waiting_new_keyword_c = True
        await ctx.send("The next sent message will be added to the list of keywords for the mood: " + mood)
    elif mood == 'sad':
        new_keyword_command_mood = 1
        waiting_new_keyword_c = True
        await ctx.send("The next sent message will be added to the list of keywords for the mood: " + mood)
    elif mood == 'funny':
        new_keyword_command_mood = 2
        waiting_new_keyword_c = True
        await ctx.send("The next sent message will be added to the list of keywords for the mood: " + mood)
    elif mood == 'angry':
        new_keyword_command_mood = 3
        waiting_new_keyword_c = True
        await ctx.send("The next sent message will be added to the list of keywords for the mood: " + mood)
    elif mood == 'romantic':
        new_keyword_command_mood = 4
        waiting_new_keyword_c = True
        await ctx.send("The next sent message will be added to the list of keywords for the mood: " + mood)
    elif mood == 'bored':
        new_keyword_command_mood = 5
        waiting_new_keyword_c = True
        await ctx.send("The next sent message will be added to the list of keywords for the mood: " + mood)
    elif mood == 'excited':
        new_keyword_command_mood = 6
        waiting_new_keyword_c = True
        await ctx.send("The next sent message will be added to the list of keywords for the mood: " + mood)
    elif mood == 'greetings':
        new_keyword_command_mood = 7
        waiting_new_keyword_c = True
        await ctx.send("The next sent message will be added to the list of keywords for the mood: " + mood)
    elif mood == 'farewell':
        new_keyword_command_mood = 8
        waiting_new_keyword_c = True
        await ctx.send("The next sent message will be added to the list of keywords for the mood: " + mood)
    elif mood == 'scared':
        new_keyword_command_mood = 9
        waiting_new_keyword_c = True
        await ctx.send("The next sent message will be added to the list of keywords for the mood: " + mood)

#Display Keywords for Mood
@bot.command()
async def listkey(ctx, mood):
    if mood == 'happy':
        await ctx.send('Happy keywords: ' + str(happy_words))
    elif mood == 'sad':
        await ctx.send('Sad keywords: ' + str(sad_words))
    elif mood == 'funny':
        await ctx.send('Sad keywords: ' + str(funny_words))
    elif mood == 'angry':
        await ctx.send('Sad keywords: ' + str(angry_words))
    elif mood == 'romantic':
        await ctx.send('Sad keywords: ' + str(romantic_words))
    elif mood == 'bored':
        await ctx.send('Sad keywords: ' + str(bored_words))
    elif mood == 'excited':
        await ctx.send('Sad keywords: ' + str(excited_words))
    elif mood == 'greetings':
        await ctx.send('Sad keywords: ' + str(greetings_words))
    elif mood == 'farewell':
        await ctx.send('Farewell keywords: ' + str(farewell_words))
    elif mood == 'scared':
        await ctx.send('Scared keywords: ' + str(scared_words))

#Delete Keywords from Mood
@bot.command()
async def deletekey(ctx, mood, number):
    if mood == 'happy':
        await ctx.send('\'' + happy_words[int(number)-1] + '\' has been removed from the list of keywords for the mood: ' + mood)
        happy_words.pop(int(number)-1)
        saveData('happy')
    elif mood == 'sad':
        await ctx.send('\'' + sad_words[int(number)-1] + '\' has been removed from the list of keywords for the mood: ' + mood)
        sad_words.pop(int(number)-1)
        saveData('sad')
    elif mood == 'funny':
        await ctx.send('\'' + funny_words[int(number)-1] + '\' has been removed from the list of keywords for the mood: ' + mood)
        funny_words.pop(int(number)-1)
        saveData('funny')
    elif mood == 'angry':
        await ctx.send('\'' + angry_words[int(number)-1] + '\' has been removed from the list of keywords for the mood: ' + mood)
        angry_words.pop(int(number)-1)
        saveData('angry')
    elif mood == 'romantic':
        await ctx.send('\'' + romantic_words[int(number)-1] + '\' has been removed from the list of keywords for the mood: ' + mood)
        romantic_words.pop(int(number)-1)
        saveData('romantic')
    elif mood == 'bored':
        await ctx.send('\'' + bored_words[int(number)-1] + '\' has been removed from the list of keywords for the mood: ' + mood)
        bored_words.pop(int(number)-1)
        saveData('bored')
    elif mood == 'excited':
        await ctx.send('\'' + excited_words[int(number)-1] + '\' has been removed from the list of keywords for the mood: ' + mood)
        excited_words.pop(int(number)-1)
        saveData('excited')
    elif mood == 'greetings':
        await ctx.send('\'' + greetings_words[int(number)-1] + '\' has been removed from the list of keywords for the mood: ' + mood)
        greetings_words.pop(int(number)-1)
        saveData('greetings')
    elif mood == 'farewell':
        await ctx.send('\'' + farewell_words[int(number)-1] + '\' has been removed from the list of keywords for the mood: ' + mood)
        farewell_words.pop(int(number)-1)
        saveData('farewell')
    elif mood == 'scared':
        await ctx.send('\'' + scared_words[int(number)-1] + '\' has been removed from the list of keywords for the mood: ' + mood)
        scared_words.pop(int(number)-1)
        saveData('scared')
    
#List Moods
@bot.command()
async def listmoods(ctx):
    await ctx.send('All moods: ' + str(moods))

#Give a Quote
@bot.command()
async def quote(ctx):
    await ctx.send('\'' + str(quote) + '\'\n-' + str(quote_author) + ', ' + str(quote_date))

#On Message Events
@bot.event
async def on_message(message):
    global word_mood
    global waiting_new_response
    global unknown_responses
    global waiting_new_response_c
    global waiting_new_keyword_c
    global quote_counter
    global quote
    global quote_author
    global quote_date

    if message.author == bot.user:
        return

    msg = message.content

    if not '~' in msg:
        if not '!' in msg:
            if not waiting_new_response:
                if not waiting_new_response_c:
                    if not waiting_new_keyword_c:
                        quote_counter -= 1
    
                        if any(word in msg for word in happy_words):
                            word_mood = 0
                            chooseResponse()
                            if not unknown_responses:  
                                await message.channel.send(random.choice(chosen_response_list))
                            else:
                                await message.channel.send('I do not know how to respond to this. Please respond to this message with an appropriate response so I can respond to future messages that are similar to this one.')
                        elif any(word in msg for word in sad_words):
                            word_mood = 1
                            chooseResponse()
                            if not unknown_responses:  
                                await message.channel.send(random.choice(chosen_response_list))
                            else:
                                await message.channel.send('I do not know how to respond to this. Please respond to this message with an appropriate response so I can respond to future messages that are similar to this one.')
                        elif any(word in msg for word in funny_words):
                            word_mood = 2
                            chooseResponse()
                            if not unknown_responses:  
                                await message.channel.send(random.choice(chosen_response_list))
                            else:
                                await message.channel.send('I do not know how to respond to this. Please respond to this message with an appropriate response so I can respond to future messages that are similar to this one.')
                        elif any(word in msg for word in angry_words):
                            word_mood = 3
                            chooseResponse()
                            if not unknown_responses:  
                                await message.channel.send(random.choice(chosen_response_list))
                            else:
                                await message.channel.send('I do not know how to respond to this. Please respond to this message with an appropriate response so I can respond to future messages that are similar to this one.')
                        elif any(word in msg for word in romantic_words):
                            word_mood = 4
                            chooseResponse()
                            if not unknown_responses:  
                                await message.channel.send(random.choice(chosen_response_list))
                            else:
                                await message.channel.send('I do not know how to respond to this. Please respond to this message with an appropriate response so I can respond to future messages that are similar to this one.')
                        elif any(word in msg for word in bored_words):
                            word_mood = 5
                            chooseResponse()
                            if not unknown_responses:  
                                await message.channel.send(random.choice(chosen_response_list))
                            else:
                                await message.channel.send('I do not know how to respond to this. Please respond to this message with an appropriate response so I can respond to future messages that are similar to this one.')
                        elif any(word in msg for word in excited_words):
                            word_mood = 6
                            chooseResponse()
                            if not unknown_responses:  
                                await message.channel.send(random.choice(chosen_response_list))
                            else:
                                await message.channel.send('I do not know how to respond to this. Please respond to this message with an appropriate response so I can respond to future messages that are similar to this one.')
                        elif any(word in msg for word in greetings_words):
                            word_mood = 7
                            chooseResponse()
                            if not unknown_responses:  
                                await message.channel.send(random.choice(chosen_response_list))
                            else:
                                await message.channel.send('I do not know how to respond to this. Please respond to this message with an appropriate response so I can respond to future messages that are similar to this one.')
                        elif any(word in msg for word in farewell_words):
                            word_mood = 8
                            chooseResponse()
                            if not unknown_responses:  
                                await message.channel.send(random.choice(chosen_response_list))
                            else:
                                await message.channel.send('I do not know how to respond to this. Please respond to this message with an appropriate response so I can respond to future messages that are similar to this one.')
                        elif any(word in msg for word in scared_words):
                            word_mood = 9
                            chooseResponse()
                            if not unknown_responses:  
                                await message.channel.send(random.choice(chosen_response_list))
                            else:
                                await message.channel.send('I do not know how to respond to this. Please respond to this message with an appropriate response so I can respond to future messages that are similar to this one.')
                        
                        if quote_counter == 40:
                            quote = msg
                            quote_author = message.author.name
                            quote_date = message.created_at
                        if quote_counter <= 0:
                            await message.channel.send('\'' + str(quote) + '\'\n-' + str(quote_author) + ', ' + str(quote_date))
                            botroomchnl = bot.get_channel(954534613022306324)
                            await botroomchnl.send('\'' + str(quote) + '\'\n-' + str(quote_author) + ', ' + str(quote_date))
                            percussbuschnl = bot.get_channel(954546231806414869)
                            await percussbuschnl.send('\'' + str(quote) + '\'\n-' + str(quote_author) + ', ' + str(quote_date))
                            quote_counter = 41
                    else:
                        if new_keyword_command_mood == 0:
                            happy_words.append(msg)
                            saveData('happy')
                        elif new_keyword_command_mood == 1:
                            sad_words.append(msg)
                            saveData('sad')
                        elif new_keyword_command_mood == 2:
                            funny_words.append(msg)
                            saveData('funny')
                        elif new_keyword_command_mood == 3:
                            angry_words.append(msg)
                            saveData('angry')
                        elif new_keyword_command_mood == 4:
                            romantic_words.append(msg)
                            saveData('romantic')
                        elif new_keyword_command_mood == 5:
                            bored_words.append(msg)
                            saveData('bored')
                        elif new_keyword_command_mood == 6:
                            excited_words.append(msg)
                            saveData('excited')
                        elif new_keyword_command_mood == 7:
                            greetings_words.append(msg)
                            saveData('greetings')
                        elif new_keyword_command_mood == 8:
                            farewell_words.append(msg)
                            saveData('farewell')
                        elif new_keyword_command_mood == 9:
                            scared_words.append(msg)
                            saveData('scared')
                        await message.channel.send("Keyword created!")
                        waiting_new_keyword_c = False
                else:
                    if new_response_command_mood == 0:
                        happy_responses.append(msg)
                        saveData('happy')
                    elif new_response_command_mood == 1:
                        sad_responses.append(msg)
                        saveData('sad')
                    elif new_response_command_mood == 2:
                        funny_responses.append(msg)
                        saveData('funny')
                    elif new_response_command_mood == 3:
                        angry_responses.append(msg)
                        saveData('angry')
                    elif new_response_command_mood == 4:
                        romantic_responses.append(msg)
                        saveData('romantic')
                    elif new_response_command_mood == 5:
                        bored_responses.append(msg)
                        saveData('bored')
                    elif new_response_command_mood == 6:
                        excited_responses.append(msg)
                        saveData('excited')
                    elif new_response_command_mood == 7:
                        greetings_responses.append(msg)
                        saveData('greetings')
                    elif new_response_command_mood == 8:
                        farewell_responses.append(msg)
                        saveData('farewell')
                    elif new_response_command_mood == 9:
                        scared_responses.append(msg)
                        saveData('scared')
                    await message.channel.send("Response created!")
                    waiting_new_response_c = False
            else:
                if word_mood == 0:
                    happy_responses.append(msg)
                    saveData('happy')
                elif word_mood == 1:
                    sad_responses.append(msg)
                    saveData('sad')
                elif word_mood == 2:
                    funny_responses.append(msg)
                    saveData('funny')
                elif word_mood == 3:
                    angry_responses.append(msg)
                    saveData('angry')
                elif word_mood == 4:
                    romantic_responses.append(msg)
                    saveData('romantic')
                elif word_mood == 5:
                    bored_responses.append(msg)
                    saveData('bored')
                elif word_mood == 6:
                    excited_responses.append(msg)
                    saveData('excited')
                elif word_mood == 7:
                    greetings_responses.append(msg)
                    saveData('greetings')
                elif word_mood == 8:
                    farewell_responses.append(msg)
                    saveData('farewell')
                elif word_mood == 9:
                    scared_responses.append(msg)
                    saveData('scared')
                await message.channel.send("Response created!")
                waiting_new_response = False
                unknown_responses = False
        else:
            bot_interact_words = [
                f"Hugs {message.author.mention}",
                f"Punches {message.author.mention}",
                f"Brutally murders {message.author.mention}",
                f"High-fives {message.author.mention}",
                f"Beats the crap out of {message.author.mention}",
                f"Rewards {message.author.mention} with nine and one half gold bars.",
                f"Gives all universal knowledge to {message.author.mention}",
                f"Awkwardly asks {message.author.mention} out on a date.",
                f"Sends all of {message.author.mention}\'s personal data to Steve the scam artist.",
                f"Does homework for {message.author.mention}",
                f"Gives {message.author.mention} candy.",
                f"Feeds {message.author.mention}",
                f"Insults the mother of {message.author.mention}",
                f"Eats {message.author.mention}",
                f"Gets mad at {message.author.mention}",
                f"Places bounty on {message.author.mention}\'s head.",
                f"Rick-rolls {message.author.mention}",
                f"Plays the McDonald\'s theme song to {message.author.mention}",
                f"Celebrates the life of {message.author.mention}",
                f"Causes depression in {message.author.mention}",
                f"Sends {message.author.mention} to his grandmother\'s house in the mail.",
                f"Annihilates {message.author.mention}",
                f"Destroys {message.author.mention}",
                f"Deletes {message.author.mention}",
                f"Copies and pastes {message.author.mention}",
                f"Bothers {message.author.mention} with the chat bot.",
                f"Says hello to {message.author.mention}",
                f"Says goodbye to {message.author.mention}",
                f"Turns {message.author.mention} into sausage.",]
    
            if message.content.startswith('~interact'):
                await message.channel.send(random.choice(bot_interact_words))
    
    await bot.process_commands(message)

#Choose Response for Bot to Say Function
def chooseResponse():
    global mood
    global chosen_response_list
    global unknown_responses
    global waiting_new_response

    mood = moods[word_mood]
    if mood == 'happy':
        chosen_response_list = happy_responses
        if len(happy_responses) == 0:
            unknown_responses = True
            waiting_new_response = True
    elif mood == 'sad':
        chosen_response_list = sad_responses
        if len(sad_responses) == 0:
            unknown_responses = True
            waiting_new_response = True
    elif mood == 'funny':
        chosen_response_list = funny_responses
        if len(funny_responses) == 0:
            unknown_responses = True
            waiting_new_response = True
    elif mood == 'angry':
        chosen_response_list = angry_responses
        if len(angry_responses) == 0:
            unknown_responses = True
            waiting_new_response = True
    elif mood == 'romantic':
        chosen_response_list = romantic_responses
        if len(romantic_responses) == 0:
            unknown_responses = True
            waiting_new_response = True
    elif mood == 'bored':
        chosen_response_list = bored_responses
        if len(bored_responses) == 0:
            unknown_responses = True
            waiting_new_response = True
    elif mood == 'excited':
        chosen_response_list = excited_responses
        if len(excited_responses) == 0:
            unknown_responses = True
            waiting_new_response = True
    elif mood == 'greetings':
        chosen_response_list = greetings_responses
        if len(greetings_responses) == 0:
            unknown_responses = True
            waiting_new_response = True
    elif mood == 'farewell':
        chosen_response_list = farewell_responses
        if len(farewell_responses) == 0:
            unknown_responses = True
            waiting_new_response = True
    elif mood == 'scared':
        chosen_response_list = scared_responses
        if len(scared_responses) == 0:
            unknown_responses = True
            waiting_new_response = True

#Command Errors
@response.error
async def response_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("The format of this command should be *~response mood*.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("The format of this command should be *~response mood*.")

@deleteresp.error
async def delete_resp_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("The format of this command should be *~deleteresp mood responsenumber*.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("The format of this command should be *~deleteresp mood responsenumber*.")

@listresp.error
async def list_resp_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("The format of this command should be *~listresp mood*.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("The format of this command should be *~listresp mood*.")

@keyword.error
async def keyword_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("The format of this command should be *~keyword mood.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("The format of this command should be *~keyword mood.")

@listkey.error
async def list_key_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("The format of this command should be *~listkey mood*.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("The format of this command should be *~listkey mood*.")

@deletekey.error
async def delete_key_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("The format of this command should be *~deletekey mood keywordnumber*.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("The format of this command should be *~deletekey mood keywordnumber*.")

bot.run("OTMwMTA1NjQxODQ1MDIyNzUw.YdxCYQ.b6f2x_jy1fpx0QFo1QRnIpHJT_M")
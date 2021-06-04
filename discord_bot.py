import discord
from discord.ext import commands

client = commands.Bot(command_prefix='/')


def read_token():
    with open(".env", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()


@client.event
async def on_ready():
    print('Houston, {0.user} has landed, over.'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)

    if message.content.startswith('$hello'):
        await message.channel.send('Houston, what is going on?!')

    # if message.content.startswith('/shutdown'):
    #     await message.channel.send("Houston, I'm coming home...")
    #     exit()


@client.command(pass_context=True)
async def poll(ctx, *, message):
    emb = discord.Embed(title='Question', description=f'{message}')
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction('✅')
    await msg.add_reaction('❎')
    await ctx.message.delete()


@client.command()
async def schedule(ctx):
    await ctx.message.delete()
    await ctx.channel.send(
        """
            Schedule for 6/3
            Stand up form <https://airtable.com/shrsjXvrV9edrD0Pu?prefill_Course=SEQ3-199>
            9:30am - 10:00am Standup in Facilitator Rooms
            JT: <https://kenzie.zoom.us/j/4643938852>
            Joseph: <https://kenzie.zoom.us/j/91302681693>
            Marcus: <https://kenzie.zoom.us/my/marcuscroom>
            10:00am - 12:00pm Zoom 1:1 (<https://kenzie.zoom.us/j/97862629405>)
            12:00pm - 1:00pm Lunch
            1:00pm - 3:00pm Checkpoint 3A (<https://kenzie.zoom.us/j/97862629405>)
            """
            #  10:00am - 11:00am Demo (<https://kenzie.zoom.us/j/97862629405>)
            #  1:00pm - 3:00pm Jai's Career Class (<https://Kenzie.zoom.us/my/jaicook>) # noqa
    )


@client.command()
async def study(ctx):
    await ctx.message.delete()
    await ctx.channel.send(
        """
            Studyhall schedule:
            Tuesdays 7:00pm - 10:00pm EST
            Wednesday 10:00pm - 1:00am EST
            Thursdays 7:00pm - 10:00pm EST
            Every other Saturday 2:00pm - 5:00pm EST
            Studyhall: <https://kenzie.zoom.us/my/studyhall>
        """
    )


@client.command(pass_content=True)
async def hyde(ctx):
    await ctx.channel.send('Have you tried setting it to Wumbo? You know I wumbo, you wumbo, he/she wumbo, wumboing? Its first grade!') # noqa


@client.command()
async def manny(ctx):
    await ctx.message.delete()
    await ctx.channel.send("Manny's schedule: <https://calendly.com/leftyxiv>")


@client.command()
async def mysite(ctx):
    await ctx.message.delete()
    await ctx.channel.send('<https://darkcloudb.github.io/portfolio/>')


@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.message.delete()
    await ctx.channel.send("Houston, I'm coming home...")
    await ctx.bot.logout()

client.run(token)

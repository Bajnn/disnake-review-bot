import disnake
from disnake.ext import commands
from dotenv import load_dotenv
import os
load_dotenv()

intents = disnake.Intents.all()
activity = disnake.Activity(
    name="Simple review bot",
    type=disnake.ActivityType.playing,
)
bot = commands.Bot(intents=intents, command_prefix="!", activity=activity)



stars = ["⭐","⭐⭐","⭐⭐⭐","⭐⭐⭐⭐","⭐⭐⭐⭐⭐",]
@bot.slash_command(name="review")
async def review(
    interaction: disnake.ApplicationCommandInteraction,
    title: str,
    comment: str,
    stars: str = commands.Param(autocomplete=stars),
    file: disnake.Attachment = None
):
    embed = disnake.Embed(
        title=title,
        description=comment
    )
    embed.add_field(name="Rating", value=stars)

    if file:
        if file.content_type.startswith('image/'):
            embed.set_image(url=file.url)
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message(content="Please attach a valid image file.", ephemeral=True)
    else:
        await interaction.response.send_message(embed=embed)


bot.run(os.getenv("TOKEN"))


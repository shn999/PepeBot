"""command
.chod
"""

from telethon import events
import asyncio


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "chod":

        await event.edit(input_str)

        animation_chars = [
        
            "`Randi Founded`",
            "`You are Going To Fuck By\n` someone",
            "`Fucking You \n\n\nYour Pussy Get Red\n Spanking Your Ass\nCumming On Pussy\n\nAlmost Done... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "` Fucking You \n\n\nYour Pussy Get Red\n Spanking Your Ass\nCumming On Pussy\n\nAlmost Done... \n\nFucked Percentage... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "` Fucking You \n\n\nYour Pussy Get Red\n Spanking Your Ass\nCumming On Pussy\n\nAlmost Done... \n\nFucked Percentage... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "` Fucking You \n\n\nYour Pussy Get Red\n Spanking Your Ass\nCumming On Pussy\n\nAlmost Done... \n\nFucked Percentage... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "` Fucking You \n\n\nYour Pussy Get Red\n Spanking Your Ass\nCumming On Pussy\n\nAlmost Done... \n\nFucked Percentage... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "` Fucking You \n\n\nYour Pussy Get Red\n Spanking Your Ass\nCumming On Pussy\n\nAlmost Done... \n\nFucked Percentage... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "` Fucking You \n\n\nYour Pussy Get Red\n Spanking Your Ass\nCumming On Pussy\n\nAlmost Done... \n\nFucked Percentage... 84%\n█████████████████████▒▒▒▒ `",
            "` Fucking You \n\n\nYour Pussy Get Red\n Spanking Your Ass\nCumming On Pussy\n\nAlmost Done... \n\nFucked Percentage... 100%\n█████████████████████████ `",
            "`Fucking You \n\n\nYour Pussy Get Red\nCumming On Pussy\n\nYou get Pregnant\n\nResult: Now You Have 1 More Younger Son\nAnd His Father Name Is` only you know"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])

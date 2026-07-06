from pathlib import Path

data_path = Path(__file__).parent.joinpath("Data").absolute()

async def IGNORE_RESPONSE(interaction):
    await interaction.response.defer()
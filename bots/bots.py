import uvicorn

from unibots import Bot, Request

bot = Bot()
app = bot.app


@bot.script
def start(r: Request):
    yield 'Hello!'


if __name__ == '__main__':
    uvicorn.run('bots:app', port=8001, reload=True, use_colors=True)

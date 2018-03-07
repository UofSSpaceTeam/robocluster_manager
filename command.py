from robocluster import Device
import asyncio
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.contrib.completers import WordCompleter

SQLCompleter=WordCompleter(['STARTPROCESS', 'STOP PROCESS','STATUSQUERY'], ignore_case=True)

client=Device('client', 'rover')
while 1:
	inp=prompt(u'>',
			history=FileHistory('history.txt'),
			auto_suggest=AutoSuggestFromHistory(),
			completer=SQLCompleter)
	@client.task
	async def send_command():
	      await client.publsih('SQLCompleter', value)


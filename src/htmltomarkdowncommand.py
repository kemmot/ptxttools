import re

import commandparser

class HtmlToMarkdownCommandParser(commandparser.CommandParser):
    def fill_command(self, args):
        return HtmlToMarkdownCommand()

class HtmlToMarkdownCommand(commandparser.Command):
    @property
    def expects_input(self):
        return True
    def begin(self):
        self.__anchor_re = re.compile(r'<a href="([^"]+)">([^<]+)</a>') 
        return None
    def process(self, input):
        if '<h1>' in input:
            input = '# ' + input.replace('<h1>', '').replace('</h1>', '')
        if '<h2>' in input:
            input = '## ' + input.replace('<h2>', '').replace('</h2>', '')
        if '<h3>' in input:
            input = '### ' + input.replace('<h3>', '').replace('</h3>', '')
        if '<li>' in input:
            input = '- ' + input.replace('<li>', '').replace('</li>', '')
        if '<ul>' in input:
            input = input.replace('<ul>', '')
        if '</ul>' in input:
            input = input.replace('</ul>', '')
        if '<p>' in input:
            input = '\n' + input.replace('<p>', '')
        if '</p>' in input:
            input = input.replace('</p>', '') + '\n'
        
        input = re.sub(r'<a href="([^"]+)">([^<]+)</a>', r'[\2](\1)', input)
        input = input.replace('<strong>', '**').replace('</strong>', '**')
        input = input.replace('<br />', '\n')
        input = input.replace('&amp;', '&')
        return input
    def end(self):
        return None

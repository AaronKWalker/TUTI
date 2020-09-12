import urwid


def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()


palette = [
    ('background', 'white', 'black'),
    ('card_hd', 'light red', 'light gray'),
    ('card_sc', 'black', 'light gray'),
    ('card_border', 'white', 'light gray')
]

hearts = {
    'ace': {'value': 'A', 'suit': '♥'},
    'king': {'value': 'K', 'suit': '♥'},
    'queen': {'value': 'Q', 'suit': '♥'},
    'jack': {'value': 'J', 'suit': '♥'},
    'ten': {'value': '10', 'suit': '♥'},
    'nine': {'value': '9', 'suit': '♥'},
    'eight': {'value': '8', 'suit': '♥'},
    'seven': {'value': '7', 'suit': '♥'},
    'six': {'value': '6', 'suit': '♥'},
    'five': {'value': '5', 'suit': '♥'},
    'four': {'value': '4', 'suit': '♥'},
    'three': {'value': '3', 'suit': '♥'},
    'two': {'value': '2', 'suit': '♥'}
}

diamonds = {
    'ace': {'value': 'A', 'suit': '♦'},
    'king': {'value': 'K', 'suit': '♦'},
    'queen': {'value': 'Q', 'suit': '♦'},
    'jack': {'value': 'J', 'suit': '♦'},
    'ten': {'value': '10', 'suit': '♦'},
    'nine': {'value': '9', 'suit': '♦'},
    'eight': {'value': '8', 'suit': '♦'},
    'seven': {'value': '7', 'suit': '♦'},
    'six': {'value': '6', 'suit': '♦'},
    'five': {'value': '5', 'suit': '♦'},
    'four': {'value': '4', 'suit': '♦'},
    'three': {'value': '3', 'suit': '♦'},
    'two': {'value': '2', 'suit': '♦'}
}

clubs = {
    'ace': {'value': 'A', 'suit': '♣'},
    'king': {'value': 'K', 'suit': '♣'},
    'queen': {'value': 'Q', 'suit': '♣'},
    'jack': {'value': 'J', 'suit': '♣'},
    'ten': {'value': '10', 'suit': '♣'},
    'nine': {'value': '9', 'suit': '♣'},
    'eight': {'value': '8', 'suit': '♣'},
    'seven': {'value': '7', 'suit': '♣'},
    'six': {'value': '6', 'suit': '♣'},
    'five': {'value': '5', 'suit': '♣'},
    'four': {'value': '4', 'suit': '♣'},
    'three': {'value': '3', 'suit': '♣'},
    'two': {'value': '2', 'suit': '♣'}
}

spades = {
    'ace': {'value': 'A', 'suit': '♠'},
    'king': {'value': 'K', 'suit': '♠'},
    'queen': {'value': 'Q', 'suit': '♠'},
    'jack': {'value': 'J', 'suit': '♠'},
    'ten': {'value': '10', 'suit': '♠'},
    'nine': {'value': '9', 'suit': '♠'},
    'eight': {'value': '8', 'suit': '♠'},
    'seven': {'value': '7', 'suit': '♠'},
    'six': {'value': '6', 'suit': '♠'},
    'five': {'value': '5', 'suit': '♠'},
    'four': {'value': '4', 'suit': '♠'},
    'three': {'value': '3', 'suit': '♠'},
    'two': {'value': '2', 'suit': '♠'}
}

def card_text(card):
    return card['value'] + '\n' + card['suit']

a_h = card_text(hearts['ace'])
a_s = card_text(spades['ace'])
a_d = card_text(diamonds['ace'])
a_c = card_text(clubs['ace'])

txtbox1 = urwid.Text(a_h)
txtbox2 = urwid.Text(a_s)
txtbox3 = urwid.Text(a_d)
txtbox4 = urwid.Text(a_c)

txtmap1 = urwid.AttrMap(txtbox1, 'card_hd')
txtmap2 = urwid.AttrMap(txtbox2, 'card_sc')
txtmap3 = urwid.AttrMap(txtbox3, 'card_hd')
txtmap4 = urwid.AttrMap(txtbox4, 'card_sc')

padding1 = urwid.Padding(txtmap1, width=20)
padding2 = urwid.Padding(txtmap2, width=20)
padding3 = urwid.Padding(txtmap3, width=20)
padding4 = urwid.Padding(txtmap4, width=20)

filler1 = urwid.Filler(padding1, height=60)
filler2 = urwid.Filler(padding2, height=60)
filler3 = urwid.Filler(padding3, height=60)
filler4 = urwid.Filler(padding4, height=60)

linebox1 = urwid.LineBox(filler1, tlcorner='╔', trcorner='╗', blcorner='╚', brcorner='╝', tline='═', bline='═', lline='║', rline='║')
linebox2 = urwid.LineBox(filler2, tlcorner='╔', trcorner='╗', blcorner='╚', brcorner='╝', tline='═', bline='═', lline='║', rline='║')
linebox3 = urwid.LineBox(filler3, tlcorner='╔', trcorner='╗', blcorner='╚', brcorner='╝', tline='═', bline='═', lline='║', rline='║')
linebox4 = urwid.LineBox(filler4, tlcorner='╔', trcorner='╗', blcorner='╚', brcorner='╝', tline='═', bline='═', lline='║', rline='║')

lineboxmap1 = urwid.AttrMap(linebox1, 'card_hd')
lineboxmap2 = urwid.AttrMap(linebox2, 'card_sc')
lineboxmap3 = urwid.AttrMap(linebox3, 'card_hd')
lineboxmap4 = urwid.AttrMap(linebox4, 'card_sc')

borderpadding1 = urwid.Padding(lineboxmap1, width=1, left=5, right=5)
borderpadding2 = urwid.Padding(lineboxmap2, width=1, left=5, right=5)
borderpadding3 = urwid.Padding(lineboxmap3, width=1, left=5, right=5)
borderpadding4 = urwid.Padding(lineboxmap4, width=1, left=5, right=5)

borderfiller1 = urwid.Filler(borderpadding1, height=1, top=5, bottom=5)
borderfiller2 = urwid.Filler(borderpadding2, height=1, top=5, bottom=5)
borderfiller3 = urwid.Filler(borderpadding3, height=1, top=5, bottom=5)
borderfiller4 = urwid.Filler(borderpadding4, height=1, top=5, bottom=5)

column1 = urwid.Columns([borderfiller1, borderfiller2, borderfiller3, borderfiller4])

main_map = urwid.AttrMap(column1, 'background')

loop = urwid.MainLoop(main_map, palette, unhandled_input=exit_on_q)
loop.screen.set_terminal_properties(colors=256)
loop.run()
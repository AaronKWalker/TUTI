import config
import urwid
from todoist import TodoistAPI
import pprint


token = config.todoist_api_key
api = TodoistAPI(token)
api.sync()
states = api.state
filters = api.state['filters']
items = api.state['items']
lables = api.state['labels']
projects = api.state['projects']
reminders = api.state['reminders']
sections = api.state['sections']


print('== STATES =====================================================')
for state in states:
    pprint.pprint(state, indent=4)

print('== FILTERS ====================================================')
for filt in filters:
    pprint.pprint(filt, indent=4)

print('== ITEMS ======================================================')
pprint.pprint('!Items Length: ' + str(len(items)))
for item in items:
    pprint.pprint(item, indent=4)
    # print('++++++++++++++++++++++++++++++++++')
    # pprint.pprint('Content: ' + item['content'], indent=4)
    # pprint.pprint('Date Completed: ' + str(item['date_completed']), indent=4)
    # pprint.pprint('Checked: ' + str(item['checked']), indent=4)
    # # pprint.pprint('Due Date: ' + item['due']['date'], indent=4)
    # print('////////////////////////////////////////////////////////////////////////////////////\n')

print('== LABELS ===================================================')
for label in lables:
    pprint.pprint(label, indent=4)

print('== PROJECTS =================================================')
for project in projects:
    pprint.pprint(project, indent=4)


def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()


palette1 = [
    ('tl_txt_pal', 'light magenta', 'black'),
    ('tr_txt_pal', 'light blue', 'black'),
    ('bl_txt_pal', 'light cyan', 'black'),
    ('br_txt_pal', 'white', 'black'),
    ('top_outerbox', 'dark red', 'white'),
    ('btm_outerbox', 'light cyan', 'brown'),
    ('bg', 'light cyan', 'black'),
    ('div', 'yellow', 'black')
]

palette2 = [
    ('tl_txt_pal', '', '', '', '#999', '#42ecf5'),
    ('tr_txt_pal', '', '', '', '#850309', '#e0da14'),
    ('bl_txt_pal', '', '', '', '#000', '#f5af18'),
    ('br_txt_pal', '', '', '', '#7fdb8b', '#410385'),
    ('top_outerbox', 'dark red', 'white'),
    ('btm_outerbox', 'light cyan', 'brown'),
    ('main_linebox', '', '', '', '#F21', '#0b5'),
    ('outermost_box', 'black', 'yellow'),
    ('pile_pal', 'light gray', 'dark green')
]


tl_txt1 = 'Top Left 1'
tr_txt1 = 'Top Right 1'
bl_txt1 = 'Bottom Left 1'
br_txt1 = 'Bottom Right 1'

tl_txtbox1 = urwid.Text(tl_txt1)
tr_txtbox1 = urwid.Text(tr_txt1)
bl_txtbox1 = urwid.Text(bl_txt1)
br_txtbox1 = urwid.Text(br_txt1)

tl_txtmap1 = urwid.AttrMap(tl_txtbox1, 'tl_txt_pal')
tr_txtmap1 = urwid.AttrMap(tr_txtbox1, 'tr_txt_pal')
bl_txtmap1 = urwid.AttrMap(bl_txtbox1, 'bl_txt_pal')
br_txtmap1 = urwid.AttrMap(br_txtbox1, 'br_txt_pal')

right_pile1 = urwid.Pile([tl_txtmap1, bl_txtmap1])
left_pile1 = urwid.Pile([tr_txtmap1, br_txtmap1])

column1 = urwid.Columns([right_pile1, left_pile1])

padding1 = urwid.Padding(column1, left=10, right=3)






tl_txt2 = 'Top Left 2'
tr_txt2 = 'Top Right 2'
bl_txt2 = 'Bottom Left 2'
br_txt2 = 'Bottom Right 2'

tl_txtbox2 = urwid.Text(tl_txt2)
tr_txtbox2 = urwid.Text(tr_txt2)
bl_txtbox2 = urwid.Text(bl_txt2)
br_txtbox2 = urwid.Text(br_txt2)

tl_txtmap2 = urwid.AttrMap(tl_txtbox2, 'tl_txt_pal')
tr_txtmap2 = urwid.AttrMap(tr_txtbox2, 'tr_txt_pal')
bl_txtmap2 = urwid.AttrMap(bl_txtbox2, 'bl_txt_pal')
br_txtmap2 = urwid.AttrMap(br_txtbox2, 'br_txt_pal')

right_pile2 = urwid.Pile([tl_txtmap2, bl_txtmap2])
left_pile2 = urwid.Pile([tr_txtmap2, br_txtmap2])

column2 = urwid.Columns([right_pile2, left_pile2])

padding2 = urwid.Padding(column2, left=10, right=3)

main_div = urwid.Divider('_', bottom=1)
div_map = urwid.AttrMap(main_div, 'div')
div_padding = urwid.Padding(div_map, left=10, right=3)


main_pile = urwid.Pile([padding1, div_padding, padding2])
main_filler = urwid.Filler(main_pile, valign='top', top=1)
main_linebox = urwid.LineBox(main_filler, 'TEST 02', title_align='left', tlcorner='╔', trcorner='╗', blcorner='╚',brcorner='╝', tline='═', bline='═', lline='║', rline='║')
main_map = urwid.AttrMap(main_linebox, 'bg')

loop = urwid.MainLoop(main_map, palette2, unhandled_input=exit_on_q)
loop.screen.set_terminal_properties(colors=256)
# loop.run()
import urwid


def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()



palette = [
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


# task_content = ['Wash bed sheets', 'Laundry', 'Find new job', 'Update Postman']
# task_due_date = ['12/25/2020', '11/27/2020', '10/10/2020', '']
# task_label = ['Chores', 'Chores', 'Job Search', 'Blocked']
# task_project = ['Personal', 'Personal', 'Personal', 'Professional']
# tasks = [task_content, task_due_date, task_label, task_project]
tasks = [
    {
        'content': 'Wash bed sheets',
        'due_date': '12/25/2020',
        'label': 'Chores',
        'project': 'Personal'
    },{
        'content': 'Laundry',
        'due_date': '11/27/2020',
        'label': 'Chores',
        'project': 'Personal'
    },{
        'content': 'Find new job',
        'due_date': '10/10/2020',
        'label': 'Job Search',
        'project': 'Personal'
    },{
        'content': 'Update Postman',
        'due_date': None,
        'label': 'Blocked',
        'project': 'Professional'
    }
]

for task in tasks:
    content_text = urwid.Text(task['content'])
    duedate_text = urwid.Text(task['due_date'])
    label_text = urwid.Text(task['label'])
    project_text = urwid.Text(task['project'])








# tl_txtmap1 = urwid.AttrMap(tl_txtbox1, 'tl_txt_pal')
# tr_txtmap1 = urwid.AttrMap(tr_txtbox1, 'tr_txt_pal')
# bl_txtmap1 = urwid.AttrMap(bl_txtbox1, 'bl_txt_pal')
# br_txtmap1 = urwid.AttrMap(br_txtbox1, 'br_txt_pal')

# right_pile1 = urwid.Pile([tl_txtmap1, bl_txtmap1])
# left_pile1 = urwid.Pile([tr_txtmap1, br_txtmap1])

# column1 = urwid.Columns([right_pile1, left_pile1])

# padding1 = urwid.Padding(column1, left=10, right=3)






# tl_txt2 = 'Top Left 2'
# tr_txt2 = 'Top Right 2'
# bl_txt2 = 'Bottom Left 2'
# br_txt2 = 'Bottom Right 2'

# tl_txtbox2 = urwid.Text(tl_txt2)
# tr_txtbox2 = urwid.Text(tr_txt2)
# bl_txtbox2 = urwid.Text(bl_txt2)
# br_txtbox2 = urwid.Text(br_txt2)

# tl_txtmap2 = urwid.AttrMap(tl_txtbox2, 'tl_txt_pal')
# tr_txtmap2 = urwid.AttrMap(tr_txtbox2, 'tr_txt_pal')
# bl_txtmap2 = urwid.AttrMap(bl_txtbox2, 'bl_txt_pal')
# br_txtmap2 = urwid.AttrMap(br_txtbox2, 'br_txt_pal')

# right_pile2 = urwid.Pile([tl_txtmap2, bl_txtmap2])
# left_pile2 = urwid.Pile([tr_txtmap2, br_txtmap2])

# column2 = urwid.Columns([right_pile2, left_pile2])

# padding2 = urwid.Padding(column2, left=10, right=3)

# main_div = urwid.Divider('_', bottom=1)
# div_map = urwid.AttrMap(main_div, 'div')
# div_padding = urwid.Padding(div_map, left=10, right=3)

# # tlc = u'\u256D'.encode('utf-8')
# # trc = u'\u256E'.encode('utf-8')
# # blc = u'\u2570'.encode('utf-8')
# # brc = u'\u256F'.encode('utf-8')

# tlc = u'\u2469'.encode('utf-8')
# trc = u'\u2620'.encode('utf-8')
# blc = u'\u2620'.encode('utf-8')
# brc = u'\u2620'.encode('utf-8')

# main_pile = urwid.Pile([padding1, div_padding, padding2])
# main_filler = urwid.Filler(main_pile, valign='top', top=1)
# main_linebox = urwid.LineBox(main_filler, 'TEST 01', title_align='left', tlcorner=tlc, trcorner=trc, blcorner=blc,brcorner=brc, tline='═', bline='═', lline='│', rline='║')
# main_map = urwid.AttrMap(main_linebox, 'bg')

loop = urwid.MainLoop(main_map, palette, unhandled_input=exit_on_q)
loop.screen.set_terminal_properties(colors=256)
loop.run()
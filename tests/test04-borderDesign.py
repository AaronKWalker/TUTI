import urwid


def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()



palette = [
    ('content_pal', 'yellow', 'black', '', '', ''),
    ('duedate_pal', 'light red', 'black', '', '', ''),
    ('label_pal', 'yellow', 'black', '', '', ''),
    ('project_pal', 'yellow', 'black', '', '', ''),
    ('main_pal', 'white', 'black', '', '', '')
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

task_pile = []

for task in tasks:
    content_text = urwid.Text(task['content'])
    if (task['due_date'] is None):
        duedate_text = urwid.Text('None')
    else:
        duedate_text = urwid.Text(task['due_date'])
    label_text = urwid.Text(task['label'])
    project_text = urwid.Text(task['project'])

    content_textmap = urwid.AttrMap(content_text, 'content_pal')
    duedate_textmap = urwid.AttrMap(duedate_text, 'duedate_pal')
    label_textmap = urwid.AttrMap(label_text, 'label_pal')
    project_textmap = urwid.AttrMap(project_text, 'project_pal')

    duedate_pad = urwid.Padding(duedate_textmap, width=('relative', 20), left=8, right=3)
    label_pad = urwid.Padding(label_textmap, width=('relative', 40), right=2)
    project_pad = urwid.Padding(project_textmap, width=('relative', 40), right=2)
    content_pad = urwid.Padding(content_textmap, left=8)

    duedate_linebox = urwid.LineBox(duedate_pad, tlcorner='', trcorner='┌', blcorner='┌',brcorner=u'\u256F'.encode('utf-8'), tline='', bline='─', lline='', rline='│')
    label_linebox = urwid.LineBox(label_pad, tlcorner='', trcorner='', blcorner='',brcorner='', tline='─', bline='', lline='', rline='')
    project_linebox = urwid.LineBox(project_pad, tlcorner='', trcorner='┐', blcorner='',brcorner='', tline='─', bline='', lline='', rline='│')

    dlp_col = urwid.Columns([duedate_linebox, label_linebox, project_linebox])
    
    content_linebox = urwid.LineBox(content_pad, tlcorner='', trcorner='', blcorner='└',brcorner='┘', tline='', bline='─', lline='│', rline='│')

    c_col = urwid.Columns([content_linebox])

    cdlp_pile = urwid.Pile([dlp_col, c_col])

    task_pile.append(cdlp_pile)

main_pile = urwid.Pile(task_pile)
main_map = urwid.AttrMap(main_pile, 'main_pal')

loop = urwid.MainLoop(main_map, palette, unhandled_input=exit_on_q)
loop.screen.set_terminal_properties(colors=256)
loop.run()


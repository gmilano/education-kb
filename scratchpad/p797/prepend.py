import sys, io
def prepend(path, section):
    s = open(path).read()
    lines = s.split('\n')
    # frontmatter: --- ... --- at the very top
    assert lines[0].strip() == '---', path
    end = lines.index('---', 1)
    head = '\n'.join(lines[:end+1])
    rest = '\n'.join(lines[end+1:])
    open(path, 'w').write(head + '\n\n' + section.strip('\n') + '\n\n' + rest.lstrip('\n'))
    print('prepended %d chars to %s' % (len(section), path))

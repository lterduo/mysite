from datetime import datetime


def test1(content):

    filename = str(datetime.now())
    with open(filename+'.html', 'wt') as f:
        f.writelines('<html><head><meta charset="utf-8"></head><body>')
        f.write(content)
        f.writelines('</body></html>')
        f.close()

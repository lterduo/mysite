from datetime import datetime


def toPdf(content):

    filename = str(datetime.now()).replace(':', '_')
    finame = 'toPdf/' + filename
    with open(filename+'.html', 'wt') as f:
        # f.writelines('<html><head><meta charset="UTF-8" /></head><body>')
        f.write(content)
        # f.writelines('</body></html>')
        f.close()

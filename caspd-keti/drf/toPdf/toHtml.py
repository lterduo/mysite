from jinja2 import Environment, FileSystemLoader
import sys
from datetime import date


def generate_html(fileList, pid, project, leader, member):
    env = Environment(loader=FileSystemLoader('./'))

    # 封面下方的时间
    pdate = {'date': date.today().strftime('%Y年%m月')}

    for filename in fileList:
        # django调用，注意当前路径
        path = 'toPdf/'

        template = env.get_template(path + filename)

        # encoding="utf-8",不加乱码，傻逼
        with open(path + pid + filename, 'w+', encoding="utf-8") as fOut:
            member_len = len(member)
            html_content = template.render(
                project=project, leader=leader, member=member, pdate=pdate, member_len=member_len)
            fOut.write(html_content)


# if __name__ == "__main__":
#     # body = []
#     # result = {'cabID': 1, 'shijian': 2019, 'final_result': "正常", 'info': "无",
#     #           'image_path': "test.jpg"}
#     # body.append(result)
#     project = {'id': 17, 'pid': 'adminfeng1610262415650', 'name': '课题2', 'category': 59,
#                'category_direction': '23', 'leader': 'adminfeng', 'create_time': '2021.12'}
#     leader = {'userid': 'adminfeng', 'username': '冯颖1', 'password': '1234'}
#     member = {'name': 'aa'}

#     generate_html(project, leader, member)
